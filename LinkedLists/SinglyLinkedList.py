'''
Node class represents a single node in the linked list Each node has value (data) and a pointer to the next node
'''


class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        return


'''
Singly-Linked list class represents a list of connected, single-direction nodes
'''


class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        return

    def add_last(self, data):
        new_node = Node(data)

        # If list is empty by checking head is none
        if self.head is None:
            self.head = new_node        # Set head to the new node
            new_node.next = self.tail   # Point the new node to tail

        # If list is NOT empty
        else:
            self.tail.next = new_node   # Point next to the tail to new node

        # Set the new node as tail in both cases because we're adding last
        self.tail = new_node

        # Node has been added, therefore increment list's size
        self.size += 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data + " -->"),
            current = current.next

    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return value
            current = current.next
        return

    def remove(self, value):
        current = self.head
        if current.data == value:
            print("removing head")
            self.head = current.next
            current = None
            self.size -= 1
        else:
            while current.next is not None:
                if current.next.data == value:
                    to_delete_node = current.next
                    current.next = to_delete_node.next
                    to_delete_node = None
                current = current.next
                self.size -= 1
        return


# Below is a simple test of the data structure
ls = LinkedList()
ls.add_last("first")
ls.add_last("second")
ls.add_last("third")

ls.print_list()

item = raw_input('\nEnter search keyword: ')
print(ls.search(item))

item_remove = raw_input('\nEnter remove: ')
ls.remove(item_remove)
ls.print_list()

