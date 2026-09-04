def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_water = width * current_height
        max_water = max(max_water, current_water)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1 
    return max_water
if __name__ == "__main__":
    # Input a space-separated list of numbers (e.g., 1 8 6 2 5 4 8 3 7)
    user_input = input("Enter the heights separated by spaces: ")
    heights = [int(x) for x in user_input.split()]
    
    result = maxArea(heights)
    print("Maximum water capacity:", result)
