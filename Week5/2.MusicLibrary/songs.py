class Song:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        if self.is_not_valid_length(self.length):
            raise ValueError("The format is invalid!")

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (
            self.artist == other.artist and
            self.title == other.title and
            self.album == other.album and
            self.length == other.length)

    def __hash__(self):
        return hash("{}{}".format(self.artist, self.title))

    def _length(self, seconds=False, minutes=False, hours=False):
        splitted_length = self.length.split(':')
        if seconds:
            return self.get_seconds(splitted_length)
        elif minutes:
            return self.get_minutes(splitted_length)
        elif hours:
            return self.get_hours(splitted_length)
        else:
            str(self.length)

    def get_seconds(self, length):
        if len(length) >= 1:
            return int(length[-1])
        else:
            return 0

    def get_minutes(self, length):
        if len(length) >= 2:
            return int(length[-2])
        else:
            return 0

    def get_hours(self, length):
        if len(length) >= 3:
            return int(length[0])
        else:
            return 0

    @staticmethod
    def is_not_valid_length(string):
        return len(string.split(':')) > 4

if __name__ == '__main__':
    main()
