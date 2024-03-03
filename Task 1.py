#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_numbers = fibonacci_sequence(n_terms)
print("Fibonacci sequence:", fibonacci_numbers)

