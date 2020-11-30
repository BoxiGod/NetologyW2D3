import datetime
import hashlib


def logger(path):
    def _logger(logged_function):
        def logging(*args, **kwargs):
            start_date = datetime.date.today().strftime("%d/%m/%Y")
            start_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            result = logged_function(*args, **kwargs)
            with open(path, 'a') as log:
                log.write(f'start: {start_date, start_time}, name: {logged_function.__name__},'
                          f' args: {args, kwargs}, returned: {result}\n')
            return result
        return logging
    return _logger


@logger('function_logger.log')
def print_hi(name):
    print("Hi ", name)
    return 3


@logger('function_logger.log')
def md5_hash(some_file):
    i = 0
    lines = some_file.readlines()
    while i < len(lines):
        yield hashlib.md5(lines[i].encode())
        i += 1


if __name__ == '__main__':
    print_hi('PyCharm')
    some_f = open('function_logger.log', 'r')
    for line in md5_hash(some_f):
        print(line.hexdigest())