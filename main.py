def make_numbers_to_10():
    for i in range(11):
        yield i


def make_numbers_to_20():
    for i in range(11, 21):
        yield i


def make_numbers():
    yield from make_numbers_to_10()
    yield from make_numbers_to_20()


if __name__ == '__main__':
    for number in make_numbers():
        print(number)