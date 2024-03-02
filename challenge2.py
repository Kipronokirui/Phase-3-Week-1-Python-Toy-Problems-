print("Challenge 2")
def digit_sum(number):
    # Function to calculate the sum of digits in a number
    return sum(int(digit) for digit in str(number))

def solution(A):
    # Dictionary to store numbers grouped by their digit sums
    sum_dict = {}

    # Iterate through the input array and organize numbers by their digit sums
    for num in A:
        digit_sum_value = digit_sum(num)

        if digit_sum_value in sum_dict:
            sum_dict[digit_sum_value].append(num)
        else:
            sum_dict[digit_sum_value] = [num]

    # Initialize the maximum sum variable
    max_sum = -1

    # Iterate through digit sum groups and find the maximum sum for each group
    for key in sum_dict:
        # Check if there are at least two numbers with the same digit sum
        if len(sum_dict[key]) >= 2:
            # Calculate the sum of the two largest numbers in the group
            pair_sum = sum(sorted(sum_dict[key])[-2:])
            # Update the maximum sum if the current pair sum is greater
            max_sum = max(max_sum, pair_sum)

    # Return the maximum sum or -1 if no such pair is found
    return max_sum

# Examples:
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))      # Output: 102
print(solution([51, 32, 43]))      # Output: -1
