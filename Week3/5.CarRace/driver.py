from car import Car

class Driver:
    def __init__(self, name, car):
        if type(name) is not str:
            raise TypeError("{} is not valid string!".format(name))
        if type(car) is not Car:
            raise TypeError("The type of {} is not Car!".format(car))

        self.name = name
        self.car = car

    def __str__(self):
        return '{} and driver {}'.format(str(self.car), self.name)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    main()
