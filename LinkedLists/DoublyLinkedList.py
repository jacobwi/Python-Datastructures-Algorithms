class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev = new_node.next = None
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def add_first(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev = new_node.next = None
        else:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return "Found " + value
            current = current.next
        return

    def remove(self, value="first"):
        current = self.head
        while current is not None:
            if current.data == value:
                if current.prev is None:
                    self.head = current.next
                    current.next.prev = None
                else:
                    previous_node = current.prev
                    next_node = current.next
                    previous_node.next = next_node
                    next_node.prev = previous_node
            current = current.next
        return

    def print_list(self):
        current = self.head
        while current is not None:
            print(" <-- " + current.data + " --> ", end=" ")
            current = current.next
        return

    def print_list_reverse(self):
        current = self.tail
        while current is not None:
            print(" <-- " + current.data + " --> ", end=" ")
            current = current.prev
        return


ls = DoublyLinkedList()

ls.add_last("first")
ls.add_last("second")
ls.add_last("third")
ls.add_last("fourth")
ls.add_first("added first")
ls.remove()
ls.print_list()
