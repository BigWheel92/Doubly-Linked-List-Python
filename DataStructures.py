#node class implementation for doubly linked list
class DNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

    def setNext(self, next):
        self.next=next

    def setPrev(self, prev):
        self.prev=prev

    def setData(self, data):
        self.data=data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getData(self):
        return self.data


#doubly linked list implementation
class DLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def insertAtHead(self, data):
        newNode=DNode(data=data, next=self.head, prev=None)

        #if the list is empty
        if self.head==None:
            self.head=self.tail=newNode
            return

        self.head.setPrev(newNode)
        self.head=newNode

    def insertAtTail(self, data):
        newNode= DNode(data=data, next=None, prev=self.tail)

        #if the list is empty
        if self.head==None:
           self.head=self.tail=newNode
           return

        self.tail.setNext(newNode)
        self.tail=newNode

    def deleteFromHead(self):

        if self.head==None:
            return

        if self.head==self.tail:
            self.head=self.tail=None

        else:
            self.head=self.head.getNext()
            self.head.setPrev(None)

    def deleteFromTail(self):

        if self.tail==None:
            return

        if self.head==self.tail:
            self.head=self.tail=None

        else:
            self.tail=self.tail.getPrev()
            self.tail.setNext(None)


    def reverse(self):
        if self.head==None:
            return

        if self.head==self.tail:
            return

        temp=self.head
        self.head=self.tail
        self.tail=temp

        curr=self.head

        while curr!= None:
            temp=curr.getNext()
            curr.setNext(curr.getPrev())
            curr.setPrev(temp)
            curr=curr.getNext()

    def removeDuplicates(self):
        outer=self.head

        while outer!=None:

            inner=outer.getNext()

            while inner!=None:

                if inner.getData()== outer.getData():
                    inner.getPrev().setNext(inner.getNext())
                    if inner.getNext()!=None:
                        inner.getNext().setPrev(inner.getPrev())
                    if inner==self.tail:
                        self.tail=inner.getPrev()

                inner=inner.getNext()


            outer=outer.getNext()




    def print(self):
        curr=self.head
        while curr!=None:
            print(curr.getData())
            curr=curr.getNext()
