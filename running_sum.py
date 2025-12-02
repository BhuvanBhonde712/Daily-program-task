def runningSum(nums):
    result = []
    current_sum = 0
    for n in nums:
        current_sum += n
        result.append(current_sum)
    return result

# Example test
print(runningSum([1, 2, 3, 4]))   # Output: [1, 3, 6, 10]
