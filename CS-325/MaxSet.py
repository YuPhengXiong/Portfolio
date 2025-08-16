# a. Implement the solution of this problem using dynamic Programming. Name your function max_independent_set(nums).
#    Name your file MaxSet.py

def max_independent_set(nums):
    """Solve Dynamic Programming Problem and find its optimal solution.
        Given a list of numbers, return a subsequence of non-consecutive numbers in the form of a
        list that would have the maximum sum. When the numbers are all negatives your code
        should return []; and when your maximum sum is 0 you could return [] or [0]

            Example 1: Input: [7,2,5,8,6]
                Output: [7,5,6] (This will have sum of 18)
            Example 2: Input: [-1, -1, 0]
                Output: [] or [0] (Both are acceptable)
            Example 3: Input: [-1, -1, -10, -34]
                Output: []
            Example 4: Input: [10, -3, 0]
                Output: [10]
    """
    elements = []
    n = len(nums)
    value = True
    # Checks for any negative numbers and if so will return an empty set.
    for i in range(n):
        if nums[i] > 0:
            value = False
        if value == True:
            return elements
    # Creates a new list to hold the added values
    maxSum = [0] * len(nums)
    maxSum[0] = nums[0]
    index = last_index = len(nums) + 1
    for i in range(1, len(nums)):
        num_1 = maxSum[1]
        if i == 1:
            num_2 = 0
        else:
            num_2 = maxSum[2]
        maxSum[i] = max(num_1, num_1 + num_2)
        if index - last_index > 1 or i == 1:
            elements.append(nums[i-1])
        last_index = index
    return elements

