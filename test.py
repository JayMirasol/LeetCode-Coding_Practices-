def runTests(solution):
    test_cases = [
        {
            "input": [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
            "expected": "Sao Paulo"
        },
        {
            "input": [["B", "C"], ["D", "B"], ["C", "A"]],
            "expected": "A"
        },
        {
            "input": [["A", "Z"]],
            "expected": "Z"
        },
    ]

    passed = 0
    failed = 0

    for i, tc in enumerate(test_cases):
        result = solution(tc["input"])
        if result == tc["expected"]:
            print(f"Test {i + 1} PASSED: input={tc['input']} -> '{result}'")
            passed += 1
        else:
            print(f"Test {i + 1} FAILED: input={tc['input']} -> expected '{tc['expected']}', got '{result}'")
            failed += 1

    print(f"\n{passed} passed, {failed} failed.")
