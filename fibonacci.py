def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two terms

    # Generate subsequent terms
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)

    return fib_sequence


# Example usage:
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fib_seq = fibonacci(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fib_seq)
