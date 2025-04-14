import unittest
from exercise2 import sort_by_priority


class TestSortByPriority(unittest.TestCase):
    def test_filter_and_sort_priority(self):
        data = [
            {"id": 1, "weight": 3, "width": 1, "height": 1,
                "length": 1, "cost": 100, "priority": 2},
            {"id": 2, "weight": 3, "width": 1, "height": 1,
                "length": 1, "cost": 100, "priority": 5},
            {"id": 3, "weight": 2, "width": 1, "height": 1,
                "length": 1, "cost": 100, "priority": 3}
        ]
        criteria = [("weight", "=", 3)]

        result = sort_by_priority(data, criteria)
        expected_order = [2, 1, 3]  # IDs in the expected order

        self.assertEqual([item["id"] for item in result], expected_order)

    def test_no_match(self):
        data = [
            {"id": 1, "weight": 1, "width": 1, "height": 1,
                "length": 1, "cost": 100, "priority": 1},
            {"id": 2, "weight": 2, "width": 1, "height": 1,
                "length": 1, "cost": 100, "priority": 3}
        ]
        criteria = [("weight", "=", 3)]

        result = sort_by_priority(data, criteria)

        # Should return the same original order
        self.assertEqual([item["id"] for item in result], [1, 2])

    def test_multiple_criteria(self):
        data = [
            {"id": 1, "weight": 3, "width": 3, "height": 1,
                "length": 10, "cost": 100, "priority": 4},
            {"id": 2, "weight": 3, "width": 1, "height": 1,
                "length": 10, "cost": 100, "priority": 8},
            {"id": 3, "weight": 3, "width": 1, "height": 1,
                "length": 10, "cost": 100, "priority": 2}
        ]
        criteria = [
            ("weight", "=", 3),
            ("width", ">=", 1),
            ("length", "<=", 10)
        ]

        result = sort_by_priority(data, criteria)
        expected_order = [2, 1, 3]  # sorted by priority descending

        self.assertEqual([item["id"] for item in result], expected_order)


if __name__ == '__main__':
    unittest.main()
