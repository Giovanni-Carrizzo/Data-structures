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
        newNode = Node(data)
        curNode = self.head
        #iterate over existing list until the tail node
        while curNode.next != None:
            #traverse through list
            curNode = curNode.next
        curNode.next = newNode

    def display(self):
        '''Displays contents of linked list'''
        listofElements = []
        curNode = self.head
        while curNode.next != None:
            #traverse through list
            curNode = curNode.next
            listofElements.append(curNode.data)
        print(listofElements)

    def getListLength(self):
        curNode = self.head
        totalNodes = 0
        while curNode.next != None:
            totalNodes += 1
            curNode = curNode.next
        return totalNodes
    
    def extractor(self):
        index = int(input('Input what index the number is: '))
        curNode = self.head
        totalNodes = self.getListLength()
        curIndex = 0
        try:
            if index >= totalNodes or index < 0:
                return None
            #if the item removed is the head node
            elif index == 0:
                self.head = self.head.next
            else:
                #starting from index 0 interate to the given index
                curIndex = 0
                while curIndex < index:
                    previous = curNode
                    curNode = curNode.next
                    curIndex += 1
                #update the pointers to remove the mode at the index
                previous.next = curNode.next
                curNode.next = None
        except ValueError:
            print('Index must be a number')
            return None
    def searchMethod(self,index):
        if index >= self.getListLength():
            print('Error! given index is out of range')
            return None
        curIndex = 0
        curNode = self.head
        while True:
            curNode = curNode.next
            if curIndex == index:
                return curNode.data
            curIndex += 1
        
                

myList = LinkedList()

def addToList():
    for i in range(5):
        num = int(input('Enter a number to add to the list: '))
        myList.appendmeth(num)
    myList.display()
addToList()
print(myList.searchMethod(2))