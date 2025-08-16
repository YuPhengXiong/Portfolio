"""
Implement a backtracking algorithm
    Given a collection of amount values (A) and a target sum (S), find all unique combinations in
    A where the amount values sum up to S. Return these combinations in the form of a list.
    Each amount value may be used only the number of times it occurs in list A. The solution set
    should not contain duplicate combinations. Amounts will be positive numbers.
    Return an empty list if no possible solution exists.
    Example: A = [11,1,3,2,6,1,5]; Target Sum = 8
    Result = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]


a. Describe a backtracking algorithm to solve this problem.
    We want to first have


b. Implement the solution in a function amount(A, S). Name your file Amount.py


c. What is the time complexity of your implementation, you may find time complexity in
detailed or state whether it is linear/polynomial/exponential. etc.?

"""


def amount(A, S):
    result = []

    def backtrack(position, total, subset):
        if total > S:
            return result
        if total == S:
            result.append(subset[:])
            return result
        for index in range(position, len(A)):
            backtrack(index+1, total+A[index], subset + [A[index]])

    backtrack(0, 0, [])
    return result


print(amount([11, 1, 3, 2, 6, 1, 5], 8))

