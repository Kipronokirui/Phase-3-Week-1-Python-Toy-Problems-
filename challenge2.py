
def digit_sum(number):
    # Function to calculate the sum of digits in a number
    return sum(int(digit) for digit in str(number))

def getMaximumSumOfTwoNumbers(A):
    sum_dict = {}

    # Iterate through the input array and organize numbers by their digit sums
    for num in A:
        digit_sum_value = digit_sum(num)

        if digit_sum_value in sum_dict:
            sum_dict[digit_sum_value].append(num)
        else:
            sum_dict[digit_sum_value] = [num]

    max_sum = -1

    for key in sum_dict:
        # Check if there are at least two numbers with the same digit sum
        if len(sum_dict[key]) >= 2:
            # Calculate the sum of the two largest numbers in the group
            pair_sum = sum(sorted(sum_dict[key])[-2:])
            max_sum = max(max_sum, pair_sum)

    return max_sum

print(getMaximumSumOfTwoNumbers([51, 71, 17, 42]))
print(getMaximumSumOfTwoNumbers([42, 33, 60]))
print(getMaximumSumOfTwoNumbers([51, 32, 43]))
