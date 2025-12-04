def kids_with_candies(candies, extraCandies):
    max_candy = max(candies)
    result = []
    
    for candy in candies:
        result.append(candy + extraCandies >= max_candy)
    
    return result

# Example usage
print(kids_with_candies([2, 3, 5, 1, 3], 3))
