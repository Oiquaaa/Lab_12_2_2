class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end_recursive(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            self._insert_at_end_recursive(data, self.head)

    def _insert_at_end_recursive(self, data, current):
        if not current.next:
            current.next = Node(data)
        else:
            self._insert_at_end_recursive(data, current.next)

    def insert_before_value_recursive(self, value, new_value):
        if not self.head:
            return
        if self.head.data == value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
        else:
            self._insert_before_value_recursive(value, new_value, self.head)

    def _insert_before_value_recursive(self, value, new_value, current):
        if not current.next:
            return
        if current.next.data == value:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node
        else:
            self._insert_before_value_recursive(value, new_value, current.next)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

llist = LinkedList()
llist.insert_at_end_recursive(1)
llist.insert_at_end_recursive(2)
llist.insert_at_end_recursive(3)
llist.insert_at_end_recursive(4)
llist.insert_at_end_recursive(5)
llist.insert_at_end_recursive(6) 

llist.print_list()

llist.insert_before_value_recursive(1, 8) 
llist.insert_before_value_recursive(3, 6) 
llist.insert_before_value_recursive(5, 9) 

llist.print_list()
