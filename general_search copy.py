#lets first create a function
class Node:    
    def __init__(self,state):
        #this is the state of the node
        self.matrix = state
        #parent tracker
        self.parent = []
        #lets keep track of the cost for uniform cost search
        self.cost= 0
    #this is how we print a node
    def print(self):
        #in order to print out the nodes
        print(self.matrix)

    def children(self):
        #now creating the children of the matrixes
        return_children = []
        #we want to make max 4 matrixes for a certain case
        for i in range(4):
            #lets create the matrix
            matrix=[]
            for row in range(3):
                first = [] #creating an array
                for column in range(3): #
                    #this is the initial values that the user enters into the matrix
                    first.append(self.matrix[row][column])
                matrix.append(first)
            # a tracker to break out the loop each time we make a move so there arent double of them
            done  = False
            for row in range(3):
                for column in range(3):
                    #lets fine the blank space
                    if(matrix[row][column]==0):
                        done = True
                        if i==0:
                            if(column < len(matrix)-1):
                                matrix[row][column], matrix[row][ column + 1] =  matrix[row][column + 1], matrix[row][column]
                                return_children.append(matrix)
                        elif i==1:
                            if(column >= 1):
                                matrix[row][column], matrix[row][column - 1] =  matrix[row][column - 1], matrix[row][column]
                                return_children.append(matrix)
                        elif i==2:
                            if(row + 1<3):
                                matrix[row][column], matrix[row+1][column] =  matrix[row+1][column], matrix[row][column]
                                return_children.append(matrix)
                        elif i==3:
                            if(row - 1>=0):
                                matrix[row][column], matrix[row-1][column] =  matrix[row-1][column], matrix[row][column]
                                return_children.append(matrix)
                        #to avoid multiple manipulations
                        if done:
                            break
                    if done:
                        break
            #Now we want to create all the matrixes to node because we want to store the nodes
        for row in range(len(return_children)):
            create_node = Node(return_children[row])
            create_node.cost = self.cost + 1 
            create_node.parent = self
            #print (create_node.print())
            #print (create_node.cost)
            return_children[row] = create_node #putting it back into return_children array

        return return_children

    def calculate_misplaced_tiles(self, goal_state):
        # I want to calculate how many tiles are misplaced
        #lets create the matrix
        total_misplaced_tiles=0
        for row in range(3):
            for column in range(3): #
                if self.matrix[row][column]!=0 and self.matrix[row][column] != goal_state[row][column]:
                    total_misplaced_tiles=total_misplaced_tiles+1
        #I did minus one here to subtract the blank space
        return total_misplaced_tiles

def calculate_manhatten():
    #count the number of tiles that it is away from where it is supposed to be
    return "Calculate Manhatten"

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

def general_search(problem, target ):
    #make
    repeat = dict()
    nodes = queue_make_node(problem)
    total_nodes=0
    max_size=0
    #check if the whole quene is empty
    while (len(nodes)!=0):
        total_nodes=total_nodes+1
        max_size= max(len(nodes),max_size)
        
        #number of pops is time
        #max size of the quene is memory
        curNode = nodes.pop(0) #remove the first element
        repeat[hash(tuple(map(tuple, curNode.matrix)))] = 1
        print(curNode.print())
        # repeat.add(tuple(tuple(curNode.matrix)))
        #check if the state is repeated, pop it
        if(curNode.matrix == target): #this is how we are checking if its a goal state
            #print("Misplaced Tiles f(n)",calculate_misplaced_tiles(problem)+curNode.cost)
            print("Solution Depth",curNode.cost) #g(n) cost, h(n) the guess to how many to solve the problem, f(n) for any state we have to know the number of misplaced tiles
            print("Number of nodes expanded", total_nodes)
            print("Max quene size", max_size)
            #print("Max quene size", max)
            return curNode
        for child in curNode.children(): #simmilar to expanding
            child.parent = curNode
            if(not (hash(tuple(map(tuple, child.matrix))) in repeat)):
                nodes.append(child) #appending children
                repeat[hash(tuple(map(tuple, child.matrix)))] = 1
    return "Failure"

def main():
    #assuming we
    matrix = initial_input_puzzle()
    #Now we want the user to pick the heurisitc they are going to use to solve the algorithm
    Heuristic = input("Please pick the heuristic you want to use to solve the algorithm. 1. Uniform Cost Search, 2. The Manhattan distance, 3.The Misplaced Tile:\n ")
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #sample target
    if(Heuristic=="1"):
        #this is a node
        result = (general_search(matrix, target)) #the problem here would be the matrix
        result.print() # we want to print from the class
main()