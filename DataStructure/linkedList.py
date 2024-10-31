class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.head = None

    def insert_at_beginning(self):
        self.head = None
    def insert_at_end(self):
        if not self.head:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = None


    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return


        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next


        if not temp:
            return


        prev.next = temp.next
        temp = None


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next



