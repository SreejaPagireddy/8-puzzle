#lets first create a function
import numpy as np
class Node:    
    def __init__(self,state):
        self.state = state
        self.children = []
        self.parent = []
def initial_input():
    print("Lets start playing the 8 puzzle. Please enter valid 8-puzzle inputs in each row with a space when asked.")
    entry_message = input("Please Enter the first Row, make sure to include space between.")

def queue_make_node(initial_state):
    #create a new quene and node
    queue = []
    new_node = Node(initial_state)
    queue.append(new_node)
    return queue

def general_search(problem,QUEUEING_FUNCTION, target):
    nodes = queue_make_node(problem.initial_state())
    #check if the whole quene is empty
    while (not nodes.empty()):
        if(curNode==target): #this is how we are checking if its a goal state
            return curNode
        curNode = nodes.pop(0) #remove the first element
        for child in curNode.children: #simmilar to expanding
            child.parent = curNode
            nodes.append(child)
    return "Failure"

def main():
    #assuming we
    initial_input()

main()