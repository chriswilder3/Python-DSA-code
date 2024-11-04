class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
class Dll:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self, data):
        if self.head == None:
            newnode = Node( data, self.head, self.head)
            self.head = newnode
            return
        newnode = Node(data)
        self.head.prev = newnode
        newnode.next = self.head
        self.head = newnode
    
    def print_forward(self):
        if self.head == None:
            print(' No node to print')
            return
        curr = self.head
        list_str = " "
        while curr!= None:
            list_str += str(curr.data) + "-->"
            curr = curr.next
        print(list_str)

    def print_backward(self):
        if self.head == None:
            print('No node to print')
            return
        curr = self.head
        list_str = " "
        while curr.next != None:
            curr = curr.next
        # print(curr.data, curr== None)
        while curr != self.head:
            # print(curr.data, curr== None)
            list_str += str(curr.data) + "-->"
            curr = curr.prev
        # print(curr.data)
        list_str += str(curr.data) + "-->"
        print(list_str)

if __name__ == "__main__":
    dll = Dll()
    dll.insert_at_start(12)
    dll.insert_at_start(39)
    dll.insert_at_start(23)
    dll.print_forward()
    dll.print_backward()