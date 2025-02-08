import heapq
#lets first create a function
class Node:    
    def __init__(self,state):
        #this is the state of the node
        self.matrix = state
        #parent tracker
        self.parent = []
        #lets keep track of the cost 
        self.cost= 0
        #This is the herusitc cost for misplaced or manhatten
        self.heristic = 0
    #this is how we print a node
    def print(self):
        #in order to print out the nodes so we can match the ouput of the traceback so I am printing out the cost and for the herustic 
        #I am subtracting cost because my self.herustic accounts for the cost + heristic, so just herusitic would need to subtract cost
        print(f"The best state to expand with a g(n) = {self.cost} and h(n) = {self.heristic-self.cost} is.")
        #This is going through the current matrix and adding the brackets at the beg and end and printing out the matrix
        for row in range(3):
            print("[", end=" ")
            for column in range(3):
                #printing out the current matrix
                print(self.matrix[row][column], end=" " )
            print("]")
        print()
        
    def __str__(self):
        #This is representing the matrix of the object, it converts it to a string
        return str(self.matrix)
    def __repr__(self):
        # This method was used for debugging to see the herusitic value
        return str(self.heristic) +":" + str(self.matrix)
    def __lt__(self, other):
        # This method compares the herustic values of 2 objects
        return self.heristic < other.heristic
    def children(self):
        #now creating the children of the matrixes
        return_children = []
        #we want to make max 4 matrixes in the case that the space is in between, at max 4 children
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
            #creating a matrix
            for row in range(3):
                for column in range(3):
                    #lets fine the blank space
                    if(matrix[row][column]==0):
                        #lets set the tracker to true now after we find the blank space, takes care of all the cases if the 0 is on the edge, middle, top, bottom
                        done = True
                        #This is the first case
                        if i==0:
                            #if the column is less than the matrix, edge case
                            if(column < len(matrix)-1):
                                #then we swap the matrix, so swapping the 0's
                                matrix[row][column], matrix[row][ column + 1] =  matrix[row][column + 1], matrix[row][column]
                                #and we append it to the return_children 
                                return_children.append(matrix)
                        elif i==1:
                            #if the column is greater than 1
                            if(column >= 1):
                                #we swap the 0
                                matrix[row][column], matrix[row][column - 1] =  matrix[row][column - 1], matrix[row][column]
                                #append to the children
                                return_children.append(matrix)
                        elif i==2:
                            #if len(row) < 3
                            if(row + 1<3):
                                #swap the 0
                                matrix[row][column], matrix[row+1][column] =  matrix[row+1][column], matrix[row][column]
                                #append to the children
                                return_children.append(matrix)
                        elif i==3:
                            #if row -1 is still positive
                            if(row - 1>=0):
                                #swap the 0
                                matrix[row][column], matrix[row-1][column] =  matrix[row-1][column], matrix[row][column]
                                #append to the children
                                return_children.append(matrix)
                        #to avoid multiple manipulations, we want to break out after each iteration so we arent changing the same matrix
                        if done:
                            break
                    if done:
                        break
            #Now we want to create all the matrixes to node because we want to store the nodes
        for row in range(len(return_children)): # now we want to traverse through all the children we appended
            create_node = Node(return_children[row]) # we want to convert it to a Node becasue we are creating these matrix as a node
            create_node.cost = self.cost + 1  # we add the cost, or depth to these children
            create_node.parent = self #we assign the intial node as the parent to these children
            #print (create_node.print())
            #print (create_node.cost)
            return_children[row] = create_node #putting it back into return_children array as nodes

        return return_children #returning the children

    def calculate_misplaced_tiles(self, goal_state):
        # I want to calculate how many tiles are misplaced
        #lets create the matrix
        total_misplaced_tiles=0 
        #go through the matrix
        for row in range(3):
            for column in range(3):
                #we wanna make sure that we dont count the space, and if that tile it not in the same place as the goal state
                if self.matrix[row][column]!=0 and self.matrix[row][column] != goal_state[row][column]:
                    #we know its misplaced so lets add to the total tiles
                    total_misplaced_tiles=total_misplaced_tiles+1
        #We can now return the total misplaced tiles
        return total_misplaced_tiles

    def calculate_manhatten(self, goal_state):
        total_distance=0 # lets calculate the total_distance
        #go through the matrix
        for row in range(3):
            for column in range(3): 
                #if its not a blank space and the location is not matching from the goal state
                if self.matrix[row][column]!=0 and self.matrix[row][column]!= goal_state[row][column]:
                    #lets put a check
                    check=False
                    #get the row position of that misplaced tile
                    row_pos= row
                    #get the column position of that misplaced tile
                    column_pos = column
                    #we want to store that value of where it currently is in our matrix
                    num = self.matrix[row][column]
                    #intilizing values
                    row_pos_goal=0
                    column_pos_goal=0
                    #go through the goal state matrix
                    for row in range(3):
                        for column in range(3): 
                            #now we find where that tile is we stored in the goal state
                            if goal_state[row][column]==num:
                                #now we can set our check to true after we find the tile in goal state
                                check=True
                                # we get the new locations of the goal state of that tile for row and column
                                row_pos_goal= row
                                column_pos_goal = column
                                break
                        #lets break out of the loop so we dont account for mutliple checks after we find the tile
                        if check:
                            break
                    #Now simple we take the difference of the locations in the intial matrix and the goal matrix
                    total_distance+=abs(row_pos-row_pos_goal) + abs(column_pos-column_pos_goal)
        
        return total_distance
        #count the number of tiles that it is away from where it is supposed to be
        

def initial_input_puzzle():
    #This is our initial setup to get the user input
    print("Lets start playing the 8 puzzle. Please enter valid 8-puzzle inputs in each row with a space when asked.")
    print("Please enter 9 numbers where one of them is a 0 to represent a blank space ")
    #create a matrix
    matrix=[]
    #going through the row which has 3
    for row in range(3):
        first = [] #creating an array
        for column in range(3): #
            #appending the input that the user is entering
            first.append(int(input()))
        matrix.append(first)
    #we are now simply generating the 8-puzzle that they entered and printing it out for them
    print("Here is your 8 puzzle that you generated")
    for row in range(3):
        for column in range(3):
            print(matrix[row][column], end=" " )
        print()
    #lets return that matrix that the user generated
    return matrix

def queue_make_node(initial_state):
    #create a new quene and node
    queue = []
    #creating a node
    new_node = Node(initial_state)
    #using a heapq so we can order it based on the priority values or in other words the herustic
    heapq.heappush(queue, new_node) 
    #queue.append(new_node)
    return queue


def general_search(problem, target, heruistic ):
    # lets make a dictionary to keep track of the repeating states
    repeat = dict()
    # we are making the quene and adding the intial matrix to the quene
    nodes = queue_make_node(problem)
    #keeping track of the total_nodes, max_size, and count
    total_nodes=0
    max_size=0
    #this count is so I dont print the first intial matrix that the user enters
    count =0
    #check if the whole quene is empty, if its not empty than only going through the while loop
    while (len(nodes)!=0):
        #lets add the total_nodes that we are expanding and lets get the max size of the quene
        total_nodes=total_nodes+1
        max_size= max(len(nodes),max_size)
        
        #number of pops is time
        #max size of the quene is memory
        curNode = nodes.pop(0) #remove the first element
        count = count+1 # increase count
        #ass the matrix into the repeat dictionary
        repeat[hash(tuple(map(tuple, curNode.matrix)))] = 1
        #print all the matrix's except for the intiial one
        if(count>1):     
            curNode.print()

        
        if(curNode.matrix == target): #this is how we are checking if its a goal state
            #Lets print out all the of the following when we find the goal state
            print("Solution Depth",curNode.cost) 
            print("Number of nodes expanded", total_nodes)
            print("Max quene size", max_size)
            return curNode
        #now we want to go through the children
        for child in curNode.children(): #simmilar to expanding
            #lets set that inital matrix we expanding to the parent
            child.parent = curNode
            #make sure that the children are not a repeat, we dont wanna push repeates
            if(not (hash(tuple(map(tuple, child.matrix))) in repeat)):
                #if its uniform cost
                if heruistic=="1" :
                    #the heristic is the same as the cost
                    child.heristic = child.cost 
                    #if its misplaed
                elif heruistic=="3" :
                    # add the cost with the misplaced tiles
                    child.heristic = child.cost + child.calculate_misplaced_tiles(target)
                    #If its manhatten tiles
                elif heruistic=="2":
                    #add the manhatten herusitic with the cost
                    child.heristic = child.cost + child.calculate_manhatten(target)
                heapq.heappush(nodes, child) #appending children based on the herusitc values, priority quene
                # print('nodes', nodes)
                #adding these to repeate so we dont repeate in any of the children
                repeat[hash(tuple(map(tuple, child.matrix)))] = 1
    #we are going to return failure if the quene was empty
    return "Failure"

def main():
    #creating our first matrix, start state
    matrix = initial_input_puzzle()
    #Now we want the user to pick the heurisitc they are going to use to solve the algorithm
    Heuristic = input("Please pick the heuristic you want to use to solve the algorithm. 1. Uniform Cost Search, 2. The Manhattan distance, 3.The Misplaced Tile:\n ")
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] # target or goal state
    # now we do the general search algorithm
    result = (general_search(matrix, target, Heuristic)) 
#return the main function
main()