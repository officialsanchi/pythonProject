


import unittest

from DataStructure.task.stack import Stack


class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(5)

    def test_that_stack_have_a_size(self):
        self.assertEqual(5, self.stack.get_size())

    def test_that_stack_have_a_empty_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_that_stack_can_accept_element(self):
        self.stack.push(16)
        self.assertFalse(self.stack.is_empty())

    def test_that_stack_can_accept_two_or_more_elements(self):
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())

    def test_that_stack_can_not_contain_element_more_than_the_size(self):
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(87)
        self.stack.push(31)
        self.stack.push(60)
        self.assertRaises(IndexError, self.stack.push, 42)

    def test_that_stack_can_pop_element_store_inside(self):
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(2)
        self.stack.push(87)
        self.stack.push(31)
        self.stack.pop()
        self.assertEqual(self.stack.get_element_number(), 4)


    def test_that_stack_can_pop_the_last_element_store_inside(self):
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(2)
        self.stack.push(87)
        self.stack.push(31)
        self.assertEqual(self.stack.pop(), 31)


    def test_that_pop_should_raise_exception_if_element_not_found(self):
        self.assertRaises(IndexError, self.stack.pop)


    def test_that_I_Can_Push_123_And_Pop_321(self):
        self.stack.push(13)
        self.stack.push(11)
        self.stack.push(48)
        self.stack.push(90)
        self.stack.push(67)
        self.assertEqual(self.stack.pop(), 67)
        self.assertEqual(self.stack.pop(), 90)
        self.assertEqual(self.stack.pop(), 48)
        self.assertEqual(self.stack.pop(), 11)
        self.assertEqual(self.stack.pop(), 13)
        self.assertRaises(IndexError, self.stack.pop)

    def test_that_peek_returns_the_last_element_store_inside(self):
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(2)
        self.stack.push(87)
        self.assertEqual(self.stack.peek(), 87)


    def test_that_you_can_search_for_an_element_and_the_index_will_be_returned(self):
        self.stack = Stack(8)
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(2)
        self.stack.push(87)
        self.stack.push(31)
        self.stack.push(60)
        self.assertEqual(self.stack.search(16), 6)
        self.assertEqual(self.stack.search(35), 5)
        self.assertEqual(self.stack.search(87), 3)

    def test_that_when_element_not_found_return_minus_one(self):
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(2)
        self.stack.push(87)
        self.stack.push(31)
        self.assertEqual(self.stack.search(18), -1)


    def test_that_when_pop_the_element_will_not_be_in_stack(self):
        self.stack.push(16)
        self.stack.push(35)
        self.stack.push(2)
        self.stack.push(87)
        self.stack.push(31)
        self.assertEqual(self.stack.pop(),31)
        self.assertEqual(self.stack.search(31),-1)
        self.assertEqual(self.stack.pop(), 87)
        self.assertEqual(self.stack.search(87),-1)