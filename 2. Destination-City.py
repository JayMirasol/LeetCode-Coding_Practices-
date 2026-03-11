# Title: Destination City 
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi and cityBi. 
# Return the destination city, that is, the city without any path outgoing to another city. 
# Example1: 
# Input: paths = [["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]] 
# Output: "Sao Paulo Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
# Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

import test

def Solution(paths: list[list[str]]) -> str:
    outgoingCity = set()
    incomingCity = set()

    for a,b in paths:
        outgoingCity.add(a)
        incomingCity.add(b)
   
    return [b for b in incomingCity if b not in outgoingCity][0]

#Testing
test_cases = [
    {"input": [ [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]] ], "expected": "Sao Paulo"},
    {"input": [ [["B", "C"], ["D", "B"], ["C", "A"]] ], "expected": "A"},
    {"input": [ [["A", "Z"]] ], "expected": "Z"},
]
test.runTests(Solution, test_cases)