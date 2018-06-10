import json
import xml.etree.ElementTree as ET
from xml import etree


class Jsonable:
    basic_serializable_types = (int, float, str, list, bool, dict, type(None))

    def to_json(self, indent=4):
        return json.dumps(self.prepare_json(), indent=4)

    def prepare_json(self):
        json_dict = {"dict": {}}
        json_dict["class_name"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if type(value) in Jsonable.basic_serializable_types:
                json_dict["dict"][key] = value
            elif isinstance(value, Jsonable):
                json_dict["dict"][key] = value.prepare_json()
            else:
                raise ValueError("{} is not serializable!".format(value))

        return json_dict

    @classmethod
    def from_json(cls, json_string):
        data_dict = json.loads(json_string)

        if data_dict['class_name'] != cls.__name__:
            raise ValueError('{} must be {}'.format(data_dict['class_name'], cls.__name__))

        if not issubclass(cls, Jsonable):
            ValueError("{} is not deserializable!".format(cls))

        attributes = []
        for k, v in data_dict['dict'].items():
            if type(v) is dict and 'class_name' not in v.keys():
                attributes.append(v)
            elif type(v) is not dict and type(v) in cls.basic_serializable_types:
                attributes.append(v)
            else:
                attributes.append(globals()[v['class_name']].from_json(json.dumps(v)))

        return cls(*attributes)


class Xmlable:
    xmlable_types = (int, float, str, bool, type(None))

    def prepare_xml(self):
        root = ET.Element(self.__class__.__name__)

        for k, v in self.__dict__.items():
            new_element = ET.Element(k)
            if isinstance(v, Xmlable):
                new_element.append(v.prepare_xml())
            elif type(v) in self.xmlable_types:
                new_element.text = str(v)
            else:
                raise ValueError("{} is not serializable!".format(v))
            root.append(new_element)

        return root

    def to_xml(self):
        return ET.tostring(self.prepare_xml())

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)

        if not issubclass(cls, Xmlable):
            ValueError("{} is not deserializable!".format(cls))

        if root.tag != cls.__name__:
            raise ValueError('{} must be {}'.format(root.tag, cls.__name__))

        attributes = []
        for i in root.itertext():
            if type(i) in cls.xmlable_types:
                attributes.append(i)
            else:
                attributes.append(globals[str(i.getroot())].from_xml(ET.tostring(i)))

        return cls(*attributes)
