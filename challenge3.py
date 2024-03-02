print("Challenge 3")
def generate_string(N):
    # Ensure N is within the specified range
    if not (1 <= N <= 200000):
        raise ValueError("N should be an integer within the range [1..200,000]")

    max_letters = min(N, 26)

    # Calculate the number of times each letter should occur
    occurrences_per_letter = N // max_letters

    # Generate the string by repeating each letter the required number of times
    result = ''.join(chr(ord('a') + i) * occurrences_per_letter for i in range(max_letters))

    return result

# Examples:
print(generate_string(3))
print(generate_string(5))   
print(generate_string(30)) 
