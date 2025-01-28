#lets first create a function
class Node:    
    def __init__(self,state):
        self.state = state
        self.children = []
        self.parent = []

def initial_input_puzzle():
    print("Lets start playing the 8 puzzle. Please enter valid 8-puzzle inputs in each row with a space when asked.")
    print("Please enter 9 numbers where one of them is a 0 to represent a blank space ")
    matrix=[]
    #cited from https://www.geeksforgeeks.org/python-matrix/ to build the matrix that is needed so I can display it
    #going through the row which has 3
    for row in range(3):
        first = [] #creating an array
        for column in range(3): #
            first.append(int(input()))
        matrix.append(first)
    print("Here is your 8 puzzle that you generated")
    for row in range(3):
        for column in range(3):
            print(matrix[row][column], end=" " )
        print()
    #Now we want the user to pick the heurisitc they are going to use to solve the algorithm
    Heuristic = input("Please pick the heuristic you want to use to solve the algorithm. 1. Uniform Cost Search, 2. The Manhattan distance, 3.The Misplaced Tile: ")
    if(Heuristic==1):
        general_search(matrix,0) #the problem here would be the matrix

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
    initial_input_puzzle()


main()