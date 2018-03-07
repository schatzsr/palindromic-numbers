import unittest
from mock import patch, mock_open, call
from utils import _is_palindrome, _find_palindrome_base, generate_smallest_palindrome_bases


class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome_returns_false_when_number_is_not_palindrome_in_given_base(self):
        # decimal 12 is not a palindrome in base 4
        self.assertFalse(_is_palindrome(12, 4))

    def test_is_palindrome_returns_true_when_number_is_palindrome_in_given_base(self):
        # decimal 12 is a palindrome in base 5
        self.assertTrue(_is_palindrome(12, 5))


class TestFindPalindromeBase(unittest.TestCase):

    @patch('utils._is_palindrome')
    def test_find_palindrome_base_returns_number_and_lowest_palindrome_base(self, is_palindrome_mock):
        # Make it so the loop in _find_palindrome_base is iterated over twice
        is_palindrome_mock.side_effect = [False, True]

        number, base = _find_palindrome_base(2)

        self.assertEqual(number, 2)
        self.assertEqual(base, 3)


class TestGenerateSmallestPalindromeBases(unittest.TestCase):

    def test_value_error_raised_when_start_num_less_than_one(self):
        with self.assertRaises(ValueError) as e:
            generate_smallest_palindrome_bases(0, 3)
        self.assertEqual(e.exception.message, 'Must provide a "start_num" value greater than or equal to 1')

    def test_value_error_raised_when_end_num_less_than_start_num(self):
        with self.assertRaises(ValueError) as e:
            generate_smallest_palindrome_bases(3, 2)
        self.assertEqual(e.exception.message, '"end_num must" be greater than start_num')

    @patch('utils.writer')
    @patch('utils._find_palindrome_base')
    def test_generate_smallest_palindrome_bases_creates_csv(self, find_palindrome_base_mock, writer_mock):
        find_palindrome_base_mock.side_effect = [(1, 2), (2, 3), (3, 2)]

        m = mock_open(read_data='read data')
        with patch('__builtin__.open', m) as mock_file:
            generate_smallest_palindrome_bases(1, 3)
            self.assertIn(call('palindrome_bases_1_to_3.csv', 'w'), mock_file.call_args_list)

        self.assertEqual(find_palindrome_base_mock.call_args_list, [call(1), call(2), call(3)])

        self.assertEqual(writer_mock.return_value.writerow.call_args_list,
                         [call(['decimal', 'smallest base in which the number is a palindrome']),
                          call([1, 2]),
                          call([2, 3]),
                          call([3, 2])])


if __name__ == '__main__':
    unittest.main()
