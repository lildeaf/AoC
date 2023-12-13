import time

digits2 = [
    "one",
    "1",
    "two",
    "2",
    "three",
    "3",
    "four",
    "4",
    "five",
    "5",
    "six",
    "6",
    "seven",
    "7",
    "eight",
    "8",
    "nine",
    "9"
]


def p1():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    sum = 0
    for line in lines:
        only_digits = "".join(filter(str.isdigit, line))
        number = int(only_digits[0] + only_digits[-1])
        sum += number

    print(f"T1: {sum}")


def p2():
    input_file = open('input.txt' if not testing else 'example2.txt', 'r')
    lines = input_file.readlines()

    sum = 0
    for line in lines:
        first, last = "", ""
        length = len(line)
        for i in range(length):
            if not first and any(line.startswith(match := item, i) for item in digits2):
                first = [digits2[i + 1] for i in range(0, len(digits2) - 1, 2) if match == digits2[i]][
                    0] if not match.isdigit() else match
            if not last and any(line.endswith(match := item, 0, length - i) for item in digits2):
                last = [digits2[i + 1] for i in range(0, len(digits2) - 1, 2) if match == digits2[i]][
                    0] if not match.isdigit() else match
            if first and last:
                break
        number = int(first + last)
        # print(number)
        sum += number

    print(f"T2: {sum}")


if __name__ == '__main__':
    testing = False
    start = time.time()
    p1()
    print(time.time() - start)
    start = time.time()
    p2()
    print(time.time() - start)
