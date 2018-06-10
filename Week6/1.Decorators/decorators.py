from datetime import datetime
import time


def accepts(*type_args):
    def accepter(func):
        def decorated(*args):
            for i in range(len(args)):
                if type(args[i]) is not type_args[i]:
                    raise TypeError("Argument {} is not {}".format(i, type_args[i]))
            return func(*args)
        return decorated
    return accepter


def encrypt(key):
    def accepter(func):
        def decorated():
            string = func()
            list_str = list(string)

            encrypted_str_list = []
            for i in list_str:
                if i == ' ':
                    encrypted_str_list.append(i)
                else:
                    encrypted_str_list.append(chr(ord(i) + key))

            return ''.join(encrypted_str_list)
        return decorated
    return accepter


def log(file_name):
    def accepter(func):
        def decorated():
            with open(file_name, 'a') as f:
                line = "{} was called at {}\n".format(func.__name__, datetime.now())
                f.write(line)
            return func()
        return decorated
    return accepter


def performance(file_name):
    def accepter(func):
        def decorated():
            with open(file_name, 'a') as f:
                before_func_time = datetime.now()
                func()
                after_func_time = datetime.now()
                delta = after_func_time - before_func_time
                line = "{} was called and took {} seconds to complete\n".format(func.__name__, delta)
                f.write(line)
        return decorated
    return accepter
