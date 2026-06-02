# This is a sample Python script.
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    p = '110000'
    regex_alternating_repetitive_digit_pair = r"(?=([0-9])[0-9]\1)"
    print(re.findall(regex_alternating_repetitive_digit_pair, p))
    print()

    n = int('5')
    arr = list(map(int, '2 3 6 6 5'.split()))
    arr.sort(reverse=True)
    for i in arr[1::]:
        if i != arr[0]:
            print(i)
            break
    print(str(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
