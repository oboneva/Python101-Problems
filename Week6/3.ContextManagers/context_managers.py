from datetime import datetime
import traceback
from contextlib import contextmanager


class performance:
    def __init__(self, filename):
        self.filename = filename
        self.time_start = None
        self.time_end = None

    def __enter__(self):
        self.time_start = datetime.now()
        return self

    def performance_time(self):
        execution_time = self.time_end - self.time_start
        return "Date {}. Execution time: {}\n".format(self.time_start, execution_time)

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.time_end = datetime.now()
        with open(self.filename, 'r+') as f:
            f.write(self.performance_time())


class assertRaises:
    def __init__(self, exception, msg=None):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type == self.exception and self.msg == str(exc_value):
            return True
        elif exc_type == self.exception and self.msg != str(exc_value):
            return
        elif exc_type is None:
            raise AssertionError('{} was not raised!'.format(self.exception))
        else:
            traceback.print_tb(exc_tb)


@contextmanager
def performance1(filename):
    start = datetime.now()
    yield
    end = datetime.now()
    with open(filename, 'r+') as f:
        exec_time = end - start
        f.write("Date {}. Execution time: {}\n".format(start, exec_time))


@contextmanager
def assertRaises1(exception, msg=None):
    try:
        yield
    except BaseException as e:
        if type(e) == type(exception):
            return True
        elif type(2) is not None:
            return False
    raise AssertionError('{} was not raised!'.format(exception))


if __name__ == '__main__':
    main()
