#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    for i in range(length):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])
    print(sequence)
