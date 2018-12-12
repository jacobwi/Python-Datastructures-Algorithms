class Node:
    def __init__(self, data, top, bottom):
        self.data = data
        self.top = top
        self.bottom = bottom


class Stack:
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None

    # Insertion method to add nodes out
    def push_top(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.bottom = new_node.top = None
        else:
            new_node.bottom = self.tail
            new_node.top = None
            self.tail.top = new_node
            self.tail = new_node

    # Insertion method to push the stack in
    def push(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.bottom = new_node.top = None
        else:
            new_node.bottom = None
            new_node.top = self.head
            self.head.bottom = new_node
            self.head = new_node

    # Search method to look for specific node with a value that matches the user-entered value
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return "Found " + value
            current = current.top
        return

    # Pop method for removing nodes from the stack
    def pop(self, value="first"):
        current = self.head
        while current is not None:
            if current.data == value:
                if current.bottom is None:
                    self.head = current.next
                    current.top.bottom = None
                else:
                    previous_node = current.bottom
                    next_node = current.top
                    previous_node.top = next_node
                    next_node.bottom = previous_node
            current = current.top
        return

    # Prints the list transversely
    def print_list(self):
        current = self.head
        while current is not None:
            print("|" + current.data + "|")
            print("-----------------")
            current = current.top
        return

    # Prints the list in reverse
    def print_list_reverse(self):
        current = self.tail
        while current is not None:
            print(" <-- " + current.data + " --> ", end=" ")
            current = current.bottom
        return


# Test
ls = Stack()

ls.push("bottom")
ls.push("top")
ls.pop()
ls.print_list()
