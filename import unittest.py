import unittest
from laba12_2_2 import Node, LinkedList

class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList()
        self.llist.insert_at_end_recursive(1)
        self.llist.insert_at_end_recursive(2)
        self.llist.insert_at_end_recursive(3)
        self.llist.insert_at_end_recursive(4)
        self.llist.insert_at_end_recursive(5)
        self.llist.insert_at_end_recursive(6)

    def test_insert_before_value_recursive(self):
        self.llist.insert_before_value_recursive(1, 8)
        self.llist.insert_before_value_recursive(3, 6)
        self.llist.insert_before_value_recursive(5, 9)
        
        self.assertEqual(self.llist.head.data, 8)
        self.assertEqual(self.llist.head.next.data, 1)
        self.assertEqual(self.llist.head.next.next.data, 2)
        self.assertEqual(self.llist.head.next.next.next.data, 6)
        self.assertEqual(self.llist.head.next.next.next.next.data, 3)
        self.assertEqual(self.llist.head.next.next.next.next.next.data, 4)
        self.assertEqual(self.llist.head.next.next.next.next.next.next.data, 9)
        self.assertEqual(self.llist.head.next.next.next.next.next.next.next.data, 5)
        self.assertEqual(self.llist.head.next.next.next.next.next.next.next.next.data, 6)

if __name__ == '__main__':
    unittest.main()

