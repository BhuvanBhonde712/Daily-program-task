def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

# Example usage
print(shuffle([2, 5, 1, 3, 4, 7], 3))
