import csv


def get_key(key, option):
    return key[:len(key) - len(option)]


def filter_by_many_arguments(data, **arguments):
    pure_key = ''
    for key in arguments:
        if key.endswith('__startswith'):
            pure_key = get_key(key, '__startswith')
            data = filter_by_one_argument_startswith(data, pure_key, arguments[key])
        elif key.endswith('__contains'):
            pure_key = get_key(key, '__contains')
            data = filter_by_one_argument_contains(data, pure_key, arguments[key])
        elif key.endswith('__gt'):
            pure_key = get_key(key, '__gt')
            data = filter_by_one_argument_greater_than(data, pure_key, arguments[key])
        elif key.endswith('__lt'):
            pure_key = get_key(key, '__lt')
            data = filter_by_one_argument_less_than(data, pure_key, arguments[key])
        elif key == 'order_by':
            data = sorted(data, key=lambda k: k[arguments[key]])
        else:
            data = filter_by_one_argument_pure(data, key, arguments[key])

    return data


def filter_by_one_argument_pure(data, argument_name, argument_value):
    try:
        return [line for line in data if line[argument_name] == argument_value]
    except KeyError:
        print("Invalid key!")


def filter_by_one_argument_startswith(data, argument_name, argument_value):
    try:
        return [line for line in data if line[argument_name].startswith(argument_value)]
    except KeyError:
        print("Invalid key!")


def filter_by_one_argument_contains(data, argument_name, argument_value):
    try:
        return [line for line in data if argument_value in line[argument_name]]
    except KeyError:
        print("Invalid key!")


def filter_by_one_argument_greater_than(data, argument_name, argument_value):
    try:
        return [line for line in data if line[argument_name] > argument_value]
    except KeyError:
        print("Invalid key!")


def filter_by_one_argument_less_than(data, argument_name, argument_value):
    try:
        return [line for line in data if line[argument_name] < argument_value]
    except KeyError:
        print("Invalid key!")


def filter(file_name, **kwargs):
    with open(file_name, 'r') as f:
        data = csv.DictReader(f)

    filtered_data = filter_by_many_arguments(data, kwargs)
    print(filtered_data)


def count(file_name, **kwargs):
    with open(file_name, 'r') as f:
        data = csv.DictReader(f)

    filtered_data = filter_by_many_arguments(data, kwargs)
    print(len(filtered_data))


def first(file_name, **kwargs):
    with open(file_name, 'r') as f:
        data = csv.DictReader(f)

    filtered_data = filter_by_many_arguments(data, kwargs)
    print(filtered_data[0])


def last(file_name, **kwargs):
    with open(file_name, 'r') as f:
        data = csv.DictReader(f)

    filtered_data = filter_by_many_arguments(data, kwargs)
    print(filtered_data[-1])

if __name__ == '__main__':
    main()
