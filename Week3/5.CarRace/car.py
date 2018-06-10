class Car():
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        if max_speed <= 0:
            raise ValueError("Invalid value for max speed!")
        self.max_speed = max_speed

    def __str__(self):
        return '{} {} with maximum speed - {}'.format(self.car, self.model, self.max_speed)

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    main()
