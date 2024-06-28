#!/usr/bin/env python3

def print_fibonacci(length):
    # The case when length is 0
    if length == 0:
        print([])
        return
    
    # Initialize the sequence with the first two Fibonacci numbers
    sequence = [0, 1]
    
    # If length is 1, we should return just the first number
    if length == 1:
        print([0])
        return
    
    # Use a for loop to generate the Fibonacci sequence numbers
    for i in range(2, length):
        # The next number in the sequence is the sum of the two previous numbers
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    
    # Print the first "length" numbers in the sequence
    print(sequence[:length])

# Define the length of the Fibonacci sequence
length = 10
print_fibonacci(length)
    
    