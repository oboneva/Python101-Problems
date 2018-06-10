from race import Race
from driver import Driver
from car import Car
import json
from random import randint


class Championship:
    def __init__(self, name, races_count):
        self.name = name

        if races_count <= 0:
            raise ValueError("The count must be positive!")
        if type(races_count) is not int:
            raise TypeError("The count must be integer!")

        self.races_count = races_count

    def load_drivers(self):
        with open('cars.json', 'r') as f:
            data = json.load(f)

        drivers = []
        for driver in data['people']:
            car = Car(driver['car'], driver['model'], driver['max_speed'])
            drivers.append(Driver(driver['name'], car))

        return drivers

    @staticmethod
    def total_ranking(data, championship_name):
        total = {}

        for race, result in data[championship_name].items():
            if result['8'] not in total.keys():
                total[result['8']] = 0
            if result['6'] not in total.keys():
                total[result['6']] = 0
            if result['4'] not in total.keys():
                total[result['4']] = 0

            total[result['8']] += 8
            total[result['6']] += 6
            total[result['4']] += 4

        print('Total championship standings:\n')
        for name, points in sorted(total.items(), key=lambda k: k[1], reverse=True):
            if points > 0:
                print('{} - {}'.format(name, points))

    def start(self, championship_name):
        print('Starting a new championship called {} with {} races.'.format(self.name, self. races_count))
        print('Running {} races...'.format(self.races_count))
        print('')

        for i in range(self.races_count):
            crash_chance = randint(0, 100) / 100.0
            r = Race(self.load_drivers(), crash_chance)
            print('Race #{}'.format(i + 1))
            r.start(championship_name, i + 1)
            print('')

        with open('result.json', 'r') as f:
            data = json.load(f)
        Championship.total_ranking(data, self.name)

    def top3(self):
        pass
