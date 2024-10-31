import unittest
from math_quiz import generate_random_number, choose_operator, generate_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        # TODO
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of choices
            opr = choose_operator()
            self.assertIn(opr, operators)

    def test_generate_problem(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 3, '*', '4 * 3', 12),
            (10, 5, '+', '10 + 5', 15),
            (7, 4, '-', '7 - 4', 3),
            (6, 6, '*', '6 * 6', 36)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # TODO
            problem, answer = generate_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()

