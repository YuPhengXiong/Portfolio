"""
You are a pet store owner, and you own few dogs. Each dog has a specific hunger level given
    by array hunger_level [1..n] (ith dog has hunger level of hunger_level [i]). You have a couple of
    dog biscuits of size given by biscuit_size [1...m]. Your goal to satisfy maximum number of
    hungry dogs. You need to find the number of dogs we can satisfy.
    If a dog has hunger hunger_level[i], it can be satisfied only by taking a biscuit of size
    biscuit_size [j] >= hunger_level [i] (i.e biscuit size should be greater than or equal to hunger
    level to satisfy a dog. If no dog can be satisfied return 0.
    Conditions:
    You cannot give same biscuit to two dogs.
    Each dog can get only one biscuit.
    Example 1:
    Input: hunger_level[1,2,3], biscuit_size[1,1]
    Output: 1
    Explanation: Only one dog with hunger level of 1 can be satisfied with one cookie of
    size 1.
    Example 2:
    Input: hunger_level[2, 1], biscuit_size[1,3,2]
    Output: 2
    Explanation: Two dogs can be satisfied. The biscuit sizes are big enough to satisfy the
    hunger level of both the dogs.
a. Describe a greedy algorithm to solve this problem
b. Write an algorithm implementing the approach. Your function signature should be
feedDog(hunger_level, biscuit_size); hunger_level, biscuit_size both are one
dimention arrays . Name your file FeedDog.py
c. Analyse the time complexity of the approach.
"""


def feedDog(hunger_level, biscuit_size):
    num_dogs = 0    # counts the number of dogs that were fed.
    a = 0           # index of dog
    b = 0           # index of biscuit
    while (a < len(hunger_level)) and (b < len(biscuit_size)):
        if hunger_level[a] == biscuit_size[b] == 0:
            return num_dogs
        if hunger_level[a] < biscuit_size[b]:
            num_dogs += 1
            a += 1
            b += 1
        else:
            b += 1

    return num_dogs


print(feedDog([1, 2, 3], [1, 1]))
print(feedDog([2, 1], [1, 3, 2]))

