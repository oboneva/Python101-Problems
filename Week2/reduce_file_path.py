def reduce_file_path(path):
    reduced_path = []
    path += '/'

    dir = ''
    for i in path[1:]:
        if i != '/':
            dir += i
        elif dir == '.' or dir == '/':
            dir = ''
            continue
        elif dir == '..' and len(reduced_path) != 0:
            reduced_path.pop()
            dir = ''
        elif dir != '' and dir != '..':
            reduced_path.append(dir)
            dir = ''

    file_path = '/'
    file_path += '/'.join(reduced_path)

    return file_path
