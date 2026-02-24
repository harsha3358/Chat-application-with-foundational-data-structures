class Node:
    def __init__(self, message):
        self.message = message
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, message):
        new_node = Node(message)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.message)
            temp = temp.next

    def search(self, keyword):
        temp = self.head
        while temp:
            if keyword in temp.message.content:
                print(temp.message)
            temp = temp.next