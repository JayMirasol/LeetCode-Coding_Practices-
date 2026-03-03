def runTests(solution, test_cases):
    """
    Run a list of test cases against a solution function.

    Each test case is a dict with:
      - 'input': a list of arguments to unpack into the solution
      - 'expected': the expected return value
    """
    passed = 0
    failed = 0

    for i, tc in enumerate(test_cases):
        args = tc["input"] if isinstance(tc["input"], list) else [tc["input"]]
        result = solution(*args)
        if result == tc["expected"]:
            print(f"Test {i + 1} PASSED: input={tc['input']} -> {repr(result)}")
            passed += 1
        else:
            print(f"Test {i + 1} FAILED: input={tc['input']} -> expected {repr(tc['expected'])}, got {repr(result)}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed.")
