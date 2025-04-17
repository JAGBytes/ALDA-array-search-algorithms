import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import binary_search, jump_search, linear_search

class TestSearchAlgorithms(unittest.TestCase):
    
    # --------------------------
    # LINEAR SEARCH TESTS (No Order Required)
    # --------------------------
    def test_linear_search(self):
        """Test linear search algorithm with ordered/unordered arrays and edge cases."""
        test_cases = [
            # Format: (array, target, expected_exists)
            ([3, 7, 2, 9, 5], 9, True),     # Target in middle (unordered array)
            ([], 5, False),                  # Empty array
            ([1, 1, 1, 1], 1, True),         # All elements are the target (first occurrence)
            ([10, 20, 30], 25, False),       # Target does not exist
            ([4], 4, True),                  # Single-element array (target exists)
            ([-99, -50, -10, 0, 10], -10, True),  # Negative target (unordered array)
            ([5, 4, 3, 2, 1], 3, True),      # Target in inverted array
            ([3, 1, 4, 1, 5], 1, True),      # Duplicates (first occurrence in unordered array)
            ([10, 30, 20, 50], 50, True),    # Target at end (unordered array)
        ]

        for arr, target, exists in test_cases:
            result = linear_search.linear_search(arr, target)
            if exists:
                self.assertNotEqual(result, -1, f"Failed for {arr}: {target} should exist at index {result}")
                self.assertEqual(arr[result], target, f"Value mismatch at index {result} (expected {target}, got {arr[result]})")
            else:
                self.assertEqual(result, -1, f"Failed: {target} should not exist in {arr}")

    # --------------------------
    # BINARY SEARCH TESTS (Requires Sorted Arrays)
    # --------------------------
    def test_binary_search(self):
        """Test binary search algorithm with sorted arrays and edge cases."""
        test_cases = [
            # Format: (sorted_array, target, expected_exists)
            ([1, 2, 3, 4, 5], 3, True),       # Target in middle
            ([], 5, False),                    # Empty array
            ([1, 2, 3, 4, 5], 6, False),       # Target out of range
            ([1, 1, 2, 2], 1, True),           # Duplicates (any occurrence)
            ([5], 5, True),                    # Single-element array
            ([-99, -50, -10, 0, 10], -50, True),  # Negative target
            ([2, 4, 6, 8, 10], 8, True),       # Target at index 3
            ([10, 20, 30, 40, 50], 30, True), # Target in large array
            ([5, 5, 5, 5, 5], 5, True),       # All elements identical
            ([1, 2, 3, 4], 1, True),          # Target at start (even-length array)
            ([1, 2, 3, 4], 4, True),           # Target at end (even-length array)
            ([-5, -3, 0, 2, 4], 0, True),     # Zero in mixed array
            ([1, 3, 5, 7, 9, 11], 7, True),   # Target in middle (even-length array)
        ]

        for arr, target, exists in test_cases:
            result = binary_search.binary_search(arr, target)
            if exists:
                self.assertNotEqual(result, -1, f"Failed for {arr}: {target} should exist at index {result}")
                self.assertEqual(arr[result], target, f"Value mismatch at index {result} (expected {target}, got {arr[result]})")
            else:
                self.assertEqual(result, -1, f"Failed: {target} should not exist in {arr}")

    # --------------------------
    # JUMP SEARCH TESTS (Requires Sorted Arrays)
    # --------------------------
    def test_jump_search(self):
        """Test jump search algorithm with sorted arrays and edge cases."""
        test_cases = [
            # Format: (sorted_array, target, expected_exists)
            ([2, 4, 6, 8, 10], 8, True),      # Target in middle block
            ([], 5, False),                   # Empty array
            ([1, 3, 5, 7], 9, False),         # Target exceeds maximum
            ([1, 1, 2, 3], 1, True),          # Duplicates in first block
            ([10, 20, 30, 40], 40, True),     # Target at last element
            ([-99, -50, -10, 0, 10], -10, True),  # Negative target
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, True),  # Large array
            ([2, 4, 6, 8, 10, 12], 12, True), # Target at end (even-length array)
            ([5], 5, True),                   # Single-element array
            ([1, 2, 3, 4], 1, True),          # Target in first block
            ([10, 20, 30, 40, 50], 35, False), # Target between blocks
            ([-5, -3, 0, 2, 4], 2, True),     # Positive target in mixed array
            ([1, 3, 5, 7, 9], 1, True),       # Target at start (odd-length array)
            ([2, 4, 6, 8, 10, 12], 6, True),  # Target before a jump
            ([1, 4, 7, 10, 13], 10, True),    # Target at block boundary
        ]

        for arr, target, exists in test_cases:
            result = jump_search.jump_search(arr, target)
            if exists:
                self.assertNotEqual(result, -1, f"Failed for {arr}: {target} should exist at index {result}")
                self.assertEqual(arr[result], target, f"Value mismatch at index {result} (expected {target}, got {arr[result]})")
            else:
                self.assertEqual(result, -1, f"Failed: {target} should not exist in {arr}")

if __name__ == "__main__":
    unittest.main(verbosity=2)