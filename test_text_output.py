import unittest
from unittest import mock
import io


def say_hello():
    print("Hello!")


class TestAnswerReturn(unittest.TestCase):
    # UnitTest to check the output of function.
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_for_say_hello_function(self, arg, expected_output, mock_stdout):
        say_hello()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_salesman_menu_input(self):
        '''
        This method checks text output of the say_hello function.
        Small note: in expected_output need to make a transition to a new line.
        '''
        expected_output = ("Hello!\n")
        self.assert_stdout_for_say_hello_function(say_hello(), expected_output)


if __name__ == '__main__':
    unittest.main()
