isWinner = __import__('0-prime_game').isWinner

def run_tests():
    test_cases = [
        # Test Case 1
        {"x": 1, "nums": [1], "expected": "Ben"},
        # Test Case 2
        {"x": 1, "nums": [2], "expected": "Maria"},
        # Test Case 3
        # {"x": 1, "nums": [3], "expected": "Maria"},
        # Test Case 4
        {"x": 1, "nums": [4], "expected": "Ben"},
        # Test Case 5
        {"x": 2, "nums": [4, 5], "expected": "Maria"},
        # Test Case 6
        {"x": 2, "nums": [1, 10], "expected": "Ben"},
        # Test Case 7
        {"x": 3, "nums": [1, 2, 3], "expected": "Maria"},
        # Test Case 8
        {"x": 3, "nums": [4, 5, 6], "expected": "Ben"},
        # Test Case 9
        {"x": 3, "nums": [7, 8, 9], "expected": "Maria"},
        # Test Case 10
        {"x": 4, "nums": [1, 2, 3, 4], "expected": "Maria"},
        # Test Case 11
        {"x": 4, "nums": [10, 11, 12, 13], "expected": "Maria"},
        # Test Case 12
        {"x": 5, "nums": [14, 15, 16, 17, 18], "expected": "Ben"},
        # Test Case 13
        {"x": 5, "nums": [19, 20, 21, 22, 23], "expected": "Maria"},
        # Test Case 14
        {"x": 3, "nums": [3, 6, 9], "expected": "Maria"},
        # Test Case 15
        {"x": 3, "nums": [8, 12, 15], "expected": "Ben"},
        # Test Case 16
        {"x": 2, "nums": [30, 31], "expected": "Maria"},
        # Test Case 17
        {"x": 4, "nums": [6, 10, 14, 18], "expected": "Ben"},
        # Test Case 18
        {"x": 5, "nums": [25, 26, 27, 28, 29], "expected": "Maria"},
        # Test Case 19
        {"x": 1, "nums": [100], "expected": "Ben"},
        # Test Case 20
        {"x": 3, "nums": [1, 100, 7], "expected": "Maria"},
    ]
    
    for i, test in enumerate(test_cases):
        result = isWinner(test["x"], test["nums"])
        assert result == test["expected"], f"Test case {i + 1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i + 1} passed!")

# Call the function to run tests
run_tests()
