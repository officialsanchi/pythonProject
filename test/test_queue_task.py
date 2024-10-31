import unittest
from DataStructure.task.queue import Queue

class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(0)

    def test_that_queue_have_size(self):
        self.assertEqual(self.queue.get_size(), 5)

    def test_that_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_that_queue_is_not_empty(self):
        self.queue.add(56)
        self.assertFalse(self.queue.is_empty())

    def test_that_queue_can_add_one_or_more_elements(self):
        self.queue.add(76)
        self.queue.add(3)
        self.queue.add(51)
        self.queue.add(33)
        self.assertFalse(self.queue.is_empty())

    def test_that_queue_is_full(self):
        self.queue.add(56)
        self.queue.add(3)
        self.queue.add(51)
        self.queue.add(33)
        self.queue.add(56)
        self.assertFalse(self.queue.is_empty())
        self.assertRaises(IndexError, self.queue.add, 78)

    def test_that_queue_can_remove_elements(self):
        self.queue.add(56)
        self.queue.add(3)
        self.queue.add(51)
        self.queue.add(33)
        self.assertEqual(self.queue.count_elements(), 4)
        self.queue.remove()
        self.assertEqual(self.queue.count_elements(), 3)

    def test_that_queue_can_remove_all_elements(self):
        self.queue.add(56)
        self.queue.add(3)
        self.queue.add(51)
        self.queue.add(33)
        self.queue.add(56)
        self.assertEqual(self.queue.count_elements(), 5)
        self.queue.remove()
        self.assertEqual(self.queue.count_elements(), 4)
        self.queue.remove()
        self.assertEqual(self.queue.count_elements(), 3)
        self.queue.remove()
        self.assertEqual(self.queue.count_elements(), 2)
        self.queue.remove()
        self.assertEqual(self.queue.count_elements(), 1)
        self.queue.remove()
        self.assertEqual(self.queue.count_elements(), 0)


    def test_that_queue_can_return_the_element_removed(self):
        self.queue.add(56)
        self.queue.add(3)
        self.queue.add(51)
        self.queue.add(33)
        self.assertEqual(self.queue.remove(), 56)
        self.assertEqual(self.queue.remove(), 3)
        self.assertEqual(self.queue.remove(), 51)
        self.assertEqual(self.queue.remove(), 33)

    def test_that_queue_cannot_remove_when_queue_is_empty(self):
        self.queue.add(56)
        self.queue.add(3)
        self.queue.add(51)
        self.queue.add(33)
        self.assertEqual(self.queue.remove(), 56)
        self.assertEqual(self.queue.remove(), 3)
        self.assertEqual(self.queue.remove(), 51)
        self.assertEqual(self.queue.remove(), 33)
        self.assertRaises(IndexError, self.queue.remove)

    def test_that_I_can_view_the_last_elements(self):
        self.queue.add(56)
        self.queue.add(3)
        self.queue.add(51)
        self.queue.add(33)
        self.assertEqual(self.queue.element(), 56)