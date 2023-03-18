def maxArea(height):
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        result = max(min(height[left], height[right]) * (right - left), result)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return result

print(maxArea([1,8,6,2,5,4,8,3,7]))

