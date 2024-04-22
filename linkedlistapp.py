class Node:
    def __init__(self, data=None):
        '''Node class constructor'''
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        '''LinkedList class constructor'''
        self.head = Node()

    def appendmeth(self,data):
        newNode = Node()
        current = self.head
        #iterate over existing list until the tail node
        while current.next != None:
            #traverse through list
            current = current.next
        current.next = newNode

    def display(self):
        '''Displays contents of linked list'''
        mylist = []
        current = self.head
        while current.next != None:
            #traverse through list
            current = current.next
            mylist.appendmeth(current)
        print(mylist)

