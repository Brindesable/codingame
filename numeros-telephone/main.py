import sys
import math

class Element:
    def __init__(self):
        self.value = None
        self.next = []

    def getNext(self, value):
        '''
        If one of next element has the same value, we return it. Otherwise None.
        '''
        nextElement = None
        for element in self.next:
            if(element.value == value):
                nextElement = element
                break

        return nextElement

class Tree:
    def __init__(self):
        element = Element()
        self.first = element

    def append(self, telNumber):
        currElement = self.first
        # We fork when we create a new element in the tree
        fork = False
        # Total number of added elements
        nbAddedElem = 0
        for digit in telNumber:
            nextElement = currElement.getNext(digit)
            # If the digit is among the next elements
            if(nextElement != None and not(fork)):
                currElement = nextElement
            else:
                nbAddedElem += 1
                fork = True
                element = Element()
                element.value = digit
                element.next = []
                currElement.next.append(element)
                currElement = element

        return nbAddedElem

totalElemAdded = 0
list = Tree()
n = int(raw_input())
for i in xrange(n):
    telephone = raw_input()
    totalElemAdded += list.append(telephone)

print totalElemAdded
