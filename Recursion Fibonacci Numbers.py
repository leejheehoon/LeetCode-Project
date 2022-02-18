""" https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem """"""Python demo for sorting using VS Code Debug Visualizer."""

"""Fibonacci Sequence:
     Sequence of numbers where a number is the sum of the 2 numbers that came before it"""
     
     
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    # Write your code here.

n = int(input())
print(fibonacci(n)).py