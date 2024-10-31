
import unittest


from DataStructure.linkedList import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linkedList = LinkedList(2)

    def test_insert_at_beginning(self):
        self.linkedList.insert_at_beginning(10)
        self.linkedList .insert_at_beginning(20)
        self.assertEqual(self.linkedList , 20)
        # self.assertEqual(self.linkedList , 10)

    def test_insert_at_end(self):
        self.linkedList .insert_at_end(10)
        self.linkedList .insert_at_end(20)


        self.assertEqual(self.linkedList , 10)
        self.assertEqual(self.linkedList , 20)

    def test_delete_node(self):
        self.linkedList .insert_at_end(10)
        self.linkedList .insert_at_end(20)
        self.linkedList .insert_at_end(30)


        self.linkedList .delete_node(20)

        self.assertEqual(self.linkedList, 10)
        self.assertEqual(self.linkedList , 30)


        self.linkedList .delete_node(10)

        self.assertEqual(self.linkedList, 30)


        self.linkedList .delete_node(30)

        self.assertIsNone(self.linkedList .head)

    def test_display(self):
        self.linkedList .insert_at_end(10)
        self.linkedList .insert_at_end(20)


        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        self.linkedList .display()
        sys.stdout = sys.__stdout__


        self.assertEqual(captured_output.getvalue(), "10 -> 20 -> None\n")



