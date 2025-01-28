#lets first create a function
class Node:    
    def __init__(self,state):
        self.state = state
        self.parent = []
    def children(self):
        #now creating the children of the matrixes
        return_children = []
        for i in range(4):
            matrix=[]
            for row in range(3):
                first = [] #creating an array
                for column in range(3): #
                    first.append(self.state[row][column])
                matrix.append(first)
            for row in range(3):
                for column in range(3):
                    if(matrix[row][column]==0):
                        if i==0:
                            if(column < len(matrix)-1):
                                matrix[row][column], matrix[row][ column + 1] =  matrix[row][column + 1], matrix[row][column]
                                return_children.append(matrix)
                        if i==1:
                            if(column < len(matrix)-1):
                                matrix[row][column], matrix[row][column - 1] =  matrix[row][column - 1], matrix[row][column]
                                return_children.append(matrix)
                        if i==2:
                            if(column < len(matrix)-1):
                                matrix[row][column], matrix[row+1][column] =  matrix[row+1][column], matrix[row][column]
                                return_children.append(matrix)
                        if i==3:
                            if(column < len(matrix)-1):
                                matrix[row][column], matrix[row-1][column] =  matrix[row-1][column], matrix[row][column]
                                return_children.append(matrix)
        
        return return_children


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
    return matrix

def queue_make_node(initial_state):
    #create a new quene and node
    queue = []
    new_node = Node(initial_state)
    queue.append(new_node)
    return queue

def general_search(problem, target):
    #make
    repeat = set()
    nodes = queue_make_node(problem)
    #check if the whole quene is empty
    while (len(nodes)!=0):
        curNode = nodes.pop(0) #remove the first element
        #check if the state is repeated, pop it
        if(curNode.state == target): #this is how we are checking if its a goal state
            return curNode
        for child in curNode.children(): #simmilar to expanding
            child.parent = curNode
            nodes.append(child)
    return "Failure"

def main():
    #assuming we
    matrix = initial_input_puzzle()
    #Now we want the user to pick the heurisitc they are going to use to solve the algorithm
    Heuristic = input("Please pick the heuristic you want to use to solve the algorithm. 1. Uniform Cost Search, 2. The Manhattan distance, 3.The Misplaced Tile: ")
    target = [[1, 2, 3], [4, 0, 5], [6, 7, 8]] #sample target
    if(Heuristic==1):
        general_search(matrix, target) #the problem here would be the matrix
    print(matrix)


main()