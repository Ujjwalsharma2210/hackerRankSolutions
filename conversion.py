# This program takes an integer input and returns octal, hexadecimal and binary
# Values till that integer.
def print_formatted(number):
    for i in range(1, number+1):
        print(i, oct(i), hex(i), bin(i))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
