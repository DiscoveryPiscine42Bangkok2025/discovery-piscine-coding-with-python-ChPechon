#!/usr/bin/env python3

def main():
    print("Enter the first number:")
    num1 = int(input())
    print("Enter the second number:")
    num2 = int(input())

    result = num1 * num2
    print(f"%d x %d = %d" % (num1, num2, result))

    if (result > 0):
        print("This number is positive.")
    elif (result < 0):
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")
    
main()