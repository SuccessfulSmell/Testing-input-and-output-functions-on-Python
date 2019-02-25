import unittest


def change_operation():
    user_answer = input()
    if user_answer == '1':
        return "Hello"
    elif user_answer == '2':
        return "Hello World"
    else:
        return 0


class TestAnswerReturn(unittest.TestCase):
    def test_change_operation_function_with_input_one(self):
        '''
        Test function change_operation() with input '1'
        '''
        original_raw_input = __builtins__.input
        __builtins__.input = lambda: '1'
        self.assertEqual(change_operation(), "Hello")
        __builtins__.input = original_raw_input

    def test_change_operation_function_with_input_two(self):
        '''
        Test function change_operation() with input '2'
        '''
        original_raw_input = __builtins__.input
        __builtins__.input = lambda: '2'
        self.assertEqual(change_operation(), "Hello World")
        __builtins__.input = original_raw_input

    def test_change_operation_function_with_other_input(self):
        '''
        Test function change_operation() with other input
        '''
        original_raw_input = __builtins__.input
        __builtins__.input = lambda: 'Something'
        self.assertEqual(change_operation(), 0)
        __builtins__.input = original_raw_input


if __name__ == '__main__':
    unittest.main()