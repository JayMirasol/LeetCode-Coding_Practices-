# Title: Maximum Score From Removing Stones:
# You are playing a solitaire game with three piles of stones of sizes a, b, and c respectively. 
# Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. 
# The game stops when there are fewer than two non-empty piles (meaning there are no more available moves). 
# Given three integers a, b, and c, return the maximum score you can get.
import test

def Solution(a: int, b: int, c: int) -> int:
    l = sorted([a,b,c])
    l = [x for x in l if x > 0]
    res = 0
    while len(l) > 1:
        l[0] -= 1
        l[-1] -= 1
        res += 1
        l = sorted([x for x in l if x > 0])
    return res    
#Testing
test_cases = [
    {"input": [2, 4, 6], "expected": 6},
    {"input": [2, 3, 3], "expected": 4},
    {"input": [1, 8, 8], "expected": 8},
    {"input": [0, 0, 5], "expected": 0},
]
test.runTests(Solution, test_cases)


# Explained Solution:

# Iterations of [2, 4, 6] 

# 6 iteration | Max Score : 6 | res = 6
# [1, 4, 5]
# [0, 4, 4]
# [0, 3, 3]
# [0, 2, 2]
# [0, 1, 1]
# [0, 0, 0]

# Iterations of [2, 3, 3] 

# 4 iteration | Max Score : 4 | res = 4
# [2, 2, 2]
# [2, 1, 1]
# [1, 1, 0]
# [0, 0, 0]

# Iterations of [1, 8, 8] 

# 8 iteration | Max Score : 8 | res = 8
# [1, 7, 7]
# [1, 6, 6]
# [1, 5, 5]
# [1, 4, 4]
# [1, 3, 3]
# [1, 2, 2]
# [0, 1, 1]
# [0, 0, 0]