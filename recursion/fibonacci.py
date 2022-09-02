# A fibonacci sequence is a sequence of numbers in which each number is the sum of the 2 preceeding numbers. The sequence starts with 0 and 1 (i.e 0, 1, 1, 2, 3, 5.....)

def fibonacci(n):
    assert n >=0 and int(n) == n, 'The number must be a positive integer '
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))