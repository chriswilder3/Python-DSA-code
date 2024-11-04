class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self,data):
        newnode = Node(data, self.head ) # to insert at start : newnode.next->head,
                                   # head = newnode
        self.head = newnode
    def print_list(self):
        if self.head == None:
            print(" List is empty")
            return
        curr = self.head
        data_in_list = " "
        while curr != None:
            data_in_list += str(curr.data) + "-->"
            curr = curr.next
        print(data_in_list)
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        newnode = Node(data)
        curr.next = newnode
    def delete_at_start(self):
        if self.head == None:
            print(" No node to delete")
        start = self.head 
        self.head = start.next
        print(f"deleted {start.data}")
        del start
    def length(self):
        length = 0
        curr = self.head
        while curr != None:
            curr = curr.next
            length +=1
        return length
    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            print(' No node to search')
            return
            
        curr = self.head
        inserted = False
        while curr.next!= None:
            if curr.data == data_after:
                newnode = Node(data_to_insert, curr.next)
                curr.next = newnode
                inserted = True
                break
            curr = curr.next
        if curr.next == None and inserted == False and curr.data == data_after:
            newnode = Node(data_to_insert)
            curr.next = newnode

    def remove_by_value(self, data):
        if self.head == None:
            print('Nothing to Delete')
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        prev = self.head
        while curr!= None:
            if curr.data == data:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_start(21)
    # ll.insert_at_start(34)
    ll.insert_at_end(17)
    ll.insert_at_end(22)
    # print(ll.length())
    ll.print_list()
    ll.delete_at_start()
    ll.print_list()
    ll.insert_at_start(12)
    ll.print_list()
    ll.insert_after_value(12,38)
    ll.print_list()
    ll.remove_by_value(22)
    ll.print_list()
    # print(ll.length())

    
