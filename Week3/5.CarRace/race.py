from driver import Driver
from random import randint
import json
import sys


class Race:
    points_for_winners = [8, 6, 4]

    def __init__(self, drivers, crash_chance):
        for driver in drivers:
            if type(driver) is not Driver:
                raise TypeError('{} must be of type Driver!'.format(driver))

        if crash_chance > 1.0 or crash_chance < 0:
            raise ValueError("The crash chance must be between 0 and 1!")

        self.drivers = drivers
        self.crash_chance = crash_chance

    def start(self, championship_name, race_number):
        print('###### START ######')
        result = self.result()

        if '8' in result.keys():
            print('{} - 8'.format(result['8']))
        if '6' in result.keys():
            print('{} - 6'.format(result['6']))
        if '4' in result.keys():
            print('{} - 4'.format(result['4']))

        for crashed in result['crashed']:
            print('Unfortunately, {} has crashed.'.format(crashed))

        self.save_result_to_json(result, championship_name, race_number)

    def result(self):
        ranking_points = {}

        for driver in self.drivers:
            personal_crash_chance = randint(0, 100)
            if personal_crash_chance > 80:
                ranking_points[driver.name] = 0
            elif personal_crash_chance < 20:
                ranking_points[driver.name] = driver.car.max_speed
            else:
                ranking_points[driver.name] = driver.car.max_speed * self.crash_chance

        result = {'crashed': [], '0': []}
        i = 0
        for name, points in sorted(ranking_points.items(), key=lambda k: k[1], reverse=True):
            if i == 0 and points != 0:
                result['8'] = name
            elif i == 1 and points != 0:
                result['6'] = name
            elif i == 2 and points != 0:
                result['4'] = name
            elif points == 0:
                result['crashed'].append(name)
            else:
                result['0'].append(name)
            i += 1

        return result

    def save_result_to_json(self, result, championship_name, race_number):
        try:
            with open('result.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        if race_number == 1:
            data[championship_name] = {}

        data[championship_name]['Race{}'.format(race_number)] = result

        with open('result.json', 'w') as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()
