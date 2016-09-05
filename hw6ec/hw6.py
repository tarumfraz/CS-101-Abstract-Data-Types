# HW6ec.py
# Sources: TA's, Piazza, Google (for general python questions), Stack Overflow (python class information)
# python visualizer (to walk through BST implementation, and debug)


#****************************************************************************************************************
# Q1
#****************************************************************************************************************

# Variables to keep track of the color of the nodes in RBT
red = "red"
black = "black"

class leaf(object): # Constructor for our sentinen (dummy) leaves
    def __init__(self):
        self.color = black  # Always will be back

NIL = leaf() # Create an instance of the class leaf, call it NIL

# Constructor for our rbt nodes
class rbtNode(object):
    def __init__(self, key, value, color = red, leftchild = NIL, rightchild = NIL, parent = NIL):
        assert color in (red, black)
        self.color, self.key, self.value, self.leftchild, self.rightchild, self.parent = (color, key, value, leftchild, rightchild, parent)


# Contructor for our roor which is always initially initialized to NIL
class BSTree(object):
    def __init__(self, root = NIL):
        self.root = root

    # Rotation funtion that's goal is to preserve the ordering within the RBT
    # leftRotation will shift a node x to the left, and properly place all of its subtrees
    def leftRotation(self, node): 

        assert(node.rightchild != NIL) # Ensure right child of node to be rotated is not NUll 
        tempNode = node.rightchild # Rotate
        node.rightchild = tempNode.leftchild
        if tempNode.leftchild != NIL: # If the node has a left child
            tempNode.leftchild.parent = node # Then the left child of that parent will have to be moved
        tempNode.parent = node.parent 
        if node.parent == NIL: # If the node does not have a parent
            self.root = tempNode # Then the rorated node is now the new root
        elif node == node.parent.leftchild: # If it has a cousin
            node.parent.leftchild = tempNode # We will rotate appropriately
        else:
            node.parent.rightchild = tempNode # Miirror case for right children
        tempNode.leftchild = node
        node.parent = tempNode 

    # Rotation funtion that's goal is to preserve the ordering within the RBT
    # rightRotation will shift a node x to the right, and properly place all of ots subtrees
    def rightRotation(self, node):

        assert(node.leftchild != NIL) # Ensure left chilld of node is not NILL
        tempNode = node.leftchild # Rotate
        node.leftchild = tempNode.rightchild
        if tempNode.rightchild != NIL: # As long as the right child of shifted node is not NIL
            tempNode.rightchild.parent = node # Rotate
        tempNode.parent = node.parent
        if node.parent == NIL: # If the node's parent is NIL
            self.root = tempNode # Call the rotated node the root
        elif node == node.parent.rightchild: # If node has a cousin
            node.parent.rightchild = tempNode # Rotate appropiately
        else:
            node.parent.leftchild = tempNode # Mirror case for left cousins
        tempNode.rightchild = node
        node.parent = tempNode

    # A function to insert items into the BST
    def rbtInsertHelper(self, node):
        
        tempNode = NIL # Create a temp node and call it NILL
        currentNode = self.root # Start at the rood
        while currentNode != NIL: # As long as there is a node in the tree
            tempNode = currentNode # Temp node wil keep trach of where we are currently
            if node.key < currentNode.key: # Traverse through tree iteratively to find place for inserted node
                currentNode = currentNode.leftchild
            else:
                currentNode = currentNode.rightchild
        node.parent = tempNode # Assogn the parents of the children
        if tempNode == NIL: # If the tree is empty
            self.root = node # It is the first node in it, call it the root
        elif node.key < tempNode.key:
                tempNode.leftchild = node # If not root, put the node in the right place appropiately
        else:
                tempNode.rightchild = node
        

    # Insert function that maintains the RED BLACK TREE properties
    def insert(self, key, value = 1):
        node = rbtNode(key, value) # Create a RB node with given value and key
        self.rbtInsertHelper(node) # Call to the funciton to actually insert it into the BSTree (see above)
        node.color = red # Color newly inserted node RED

        while node != self.root and node.parent.color == red: # If the node is not the root and has a RED parent
            if node.parent == node.parent.parent.leftchild: # If the parent of node is the grandparent's left child
                tempNode = node.parent.parent.rightchild # Track the other child
                if tempNode.color == red: # If the node is RED
                    node.parent.color = black # Color the parent BLACK
                    tempNode.color = black # And the color of the node itself black as well
                    node.parent.parent.color = red # Color grandparent red
                    node = node.parent.parent # Node will equal it's grandparent
                else:
                    if node == node.parent.rightchild: # If the inserted node is the right child of parent
                        node = node.parent # The node now is equal to the parent
                        self.leftRotation(node) # Perform a left rotation on the node
                    node.parent.color = black # Color the parent of that node plack
                    node.parent.parent.color = red # Color the grandparent red
                    self.rightRotation(node.parent.parent) # Perform a right Rotation
            else:
                    tempNode = node.parent.parent.leftchild # Track the node's grandparent's left child
                    if tempNode.color == red: # If that node is red
                        node.parent.color = black # Color the parent of inserted node black
                        tempNode.color = black # Color the tracked node black
                        node.parent.parent.color = red # Grandparent of inserted node is red
                        node = node.parent.parent # Inserted node now equals the grandparent
                    else:
                        if node == node.parent.leftchild: # If the node we inserted is the left child of parent
                            node = node.parent # Set it equal to the parent
                            self.rightRotation(node) # Perform a right rotation on that node
                        node.parent.color = black # Color the parent of inserted node black
                        node.parent.parent.color = red # Color the grandparent of that node red
                        self.leftRotation(node.parent.parent) # Perform a right rotation on the node's grandparent
        self.root.color = black # Always set the root to the color black

    # A function to delete a node from RBT
    # Makes calls to helper functions
    def delete(self, key):

        node = self.find(key) # Find the node that needs to be deleted
        if node == None: # If thhe node is not in the tree
            return # Return the function
        tempNode = node # Track node
        tempNodeColor = tempNode.color # Track color of the node
        if node.leftchild == NIL: # If the node does not have a left child
            currentNode = node.rightchild # Track right child of the node
            self.rbtDeleteHelper1(node, node.rightchild) # Call to delete helper, rotates and deletes
        elif node.rightchild == NIL: # If the node does not have a right child
            currentNode = node.leftchild # Track the left child
            self.rbtDeleteHelper1(node, node.leftchild) # Fix RBT
        else:
            tempNode = self.minimum(node.rightchild) # Find the min in the tree, and track it
            tempNodeColor = tempNode.color # Track the color
            currentNode = tempNode.rightchild # Track the right child
            if tempNode.parent == node: # If the min in the tree is equal to the node being deleted
                currentNode.parent = tempNode # Update the parent to the tracked node
            else:
                self.rbtDeleteHelper1(tempNode, tempNode.rightchild) # Call to delete helper
                tempNode.rightchild = node.rightchild # Assign the values of right child of node
                tempNode.rightchild.parent = tempNode 
            self.rbtDeleteHelper1(node, tempNode) # Call to delete helper to fix RBT property
            tempNode.leftchild = node.leftchild # The tracked nodes left child is now equal to inserted nodes left child
            tempNode.leftchild.parent = tempNode # Tracked nodes's leftchild's parent is now equal to the tracked node
            tempNode.color = node.color # The color of the tracked node is equal to the node's color
        if tempNodeColor == black: # If the Tracked node is colored BLACK, we need to reconfisgure tree to maintain RBT 
            self.rbtDeleteHelper2(currentNode)

    # DELETE helper function
    # Input is 2 nodes, actually deletes the node, and replaces it appropiately
    def rbtDeleteHelper1(self, node1, node2):

        if node1.parent == NIL: # Handle the root case
            self.root = node2 # New root
        elif node1 == node1.parent.leftchild: # If node to be deleted is the left child
            node1.parent.leftchild = node2 # Replace second node with left child
        else:
            node1.parent.rightchild = node2 # If the nod eto be deleted is the right child
        node2.parent = node1.parent # Replace second node with the right child

    # DELETE helper funcion
    # Helps us maintain RBT properties throughout a deletion
    def rbtDeleteHelper2(self, node):

        while node != self.root and node.color == black: # If the node is not the root and is BLACK
            if node == node.parent.leftchild: # if the node is the left child
                tempNode = node.parent.rightchild # Track the right child
                if isinstance(tempNode, leaf): # if tempNode is a leaf
                    node.parent.rightchild = NIL # get rid of it
                    return
                if tempNode.color == red: # If the right child is red
                    tempNode.color = black # Color it black
                    node.parent.color = red # If the parent is red
                    self.leftRotation(node.parent) # Perform a left rotation of the parent
                    tempNode =  node.parent.rightchild # the tracked node is still right right child 
                if tempNode.leftchild.color == black and tempNode.rightchild.color == black: 
                    tempNode.color = red # Color cousoin of original node red
                    node = node.parent # Set it equal to the parent
                else:
                    if tempNode.rightchild.color == black: # If the right child of the node is black
                        tempNode.leftchild.color = black # Color left child black
                        tempNode.color = red # Color the right child red
                        self.rightRotation(tempNode) # Perform a right rotation of the original right child
                        tempNode = node.parent.rightchild # Node is still the right child 
                    tempNode.color = node.parent.color # The tracked node's color is same color as pareent
                    node.parent.color = black # Change parent to the black
                    tempNode.rightchild.color = black # Color the right child black
                    self.leftRotation(node.parent) # Perform a left Rotation on the node's parent
                    node = self.root # Assign the node to the root
            elif node == node.parent.rightchild: # If the node is the right child
                tempNode = node.parent.leftchild # Keep track of the left child
                if tempNode == NIL: # if tempnode is a leaf
                    node.parent.leftchild = NIL # get rid of it
                    return
                if tempNode.color == red: # If the right child is red
                    tempNode.color = black # Color the right child black
                    node.parent.color = red # Color the parent red
                    self.rightRotation(node.parent) # Perform a right rotation on the parent
                    tempNode = node.parent.leftchild # The right child is now the parent's left chilf
                if tempNode == NIL: # if tempnode is a leaf
                    node.parent.leftchild = NIL # get rid of it
                    return
                if tempNode.leftchild.color == black and tempNode.rightchild.color == black: # if either children are black
                    tempNode.color = red # Color parent red
                    node = node.parent 
                else:
                    if tempNode.leftchild.color == black: # If the left child is black
                        tempNode.rightchild.color = black # Color the right child black
                        tempNode.color = red # Color the parent red
                        self.leftRotation(tempNode) # Perform a left ratation on node
                        tempNode = node.parent.leftchild # Node now has a new parent
                    tempNode.color = node.parent.color # If parent and child are the same color
                    node.parent.color = black # Parent is black
                    tempNode.leftchild.color = black # Left child is black
                    self.rightRotation(node.parent) # Perform a right rotation on node's parent
        node.color = black # Color the node that was originally inserted black



    sParent = NIL #PARENT USED FOR A LEAF IN SUCCESSOR

    # A function to find values in the BST
    def find(self, key):

        node = self.root # Start at the root of the BST
        while node != NIL: # While the node exists
            if node.key == key: # If it matches the key 
                return node # Return the node
            if node.key > key: # If the key is less
                self.sParent = node # keep track of parent in case found key is a leaf
                node = node.leftchild # look in left subtree
            else:
                self.sParent = node # keep track of parent in case found key is a leaf
                node = node.rightchild # If it is equal too or greater, look in right subtree
        return NIL # Return NULL for any other cases

    # A function to find the minimum node in the RBT
    def minimum(self,node): 

        while node.leftchild != NIL: # While the left child is not a leaf
            node = node.leftchild # Iterate through left child
        if node.leftchild == NIL: # Once left child is a leaf
            return node # Return that node

    # A function to fdin the maximum node in the RBT
    def maximum(self,node):

        while node.rightchild != NIL: # While the node has a right child and is not NIL
            node = node.rightchild # Iterate through the tree, through the right child
        if node.rightchild == NIL: # Once the rigt child is a leaf
            return(node) # Return that node


    def successor(self, key):
        node = self.find(key)
        node.key = key
        if isinstance(node, leaf) != True: # if node is not a leaf
            if node.rightchild != NIL:
                return self.minimum(node.rightchild)
        if isinstance(node, leaf): # if node is a leaf
            tempNode = self.sParent # use parent that was kept track of in find
        else:
            tempNode = node.parent # else use node's parent attribute
        while tempNode != NIL and node == tempNode.rightchild:
            node = tempNode
            tempNode = tempNode.parent
        return(tempNode)


    def inOrderTraversal(self): # Function that prints BST in sorted order

        self.inOrderTraversalHelper(self.root) # Call to helper function w/ param root
         
    # distinctNodes = 0 # used to count num of distinct nodes for highRating in Q4

    def inOrderTraversalHelper(self, node): # Helper function that prints BST in sorted order
 
        if node != NIL: # If the node exists
            self.inOrderTraversalHelper(node.leftchild) # Recursively iterate through left subtree
            # commented code used in Q4
            '''self.distinctNodes += 1 Count node as distinct node
            if node.value > 70: #USED TO GET TOP 20 FREQUENT NODES
                print(node.key, " ", node.value) # Print key and value'''
            print(node.key, " " ,node.value) # Print key and value
            self.inOrderTraversalHelper(node.rightchild) # When done with left subtree, move to the right subtree




    

highRating = BSTree() # create tree for high ratings
lowRating = BSTree()  # create tree for low ratings
   

ignore = set() # words to ignore
stopwords = open("stopwords.txt", "r")
for line in stopwords:
    ignore.add(line.strip('\n'))
stopwords.close()

fineFoods = open("finefoods_cleaned.txt") #using tiny fraction of original
keysToDel = [] # will be populated by lowRating keys that will be deleted from highRating

for line in fineFoods:
    firstSplit = line.split(":", 1) #gets the number, limits splits to 1 just to make sure words are in one index
    secondSplit = firstSplit[1].split(" ") #words are in second index and are now seperated
    if int(firstSplit[0]) > 3: #go in tree with high rating
        for i in range(len(secondSplit)): #iterate through each word
            check = secondSplit[i] in ignore #check if word should be ignored, strings in ignore have new line character
            if check != True: #if word is not in set of words to ignore
                freqCheck = highRating.find(secondSplit[i].strip('\n')) #check if word is already in tree and remove new line
                if freqCheck != NIL: #increase frequency count but don't add node
                    freqCheck.value += 1 #Increase word frequency count
                else: #not already in tree
                    highRating.insert(secondSplit[i].strip('\n'), 1) #insert word, 1 is just temp value
    else:
        for i in range(len(secondSplit)): #iterate through each word
            check = secondSplit[i] in ignore #check if word should be ignored, strings in ignore have new line character
            if check != True: #as long as word is not in ignore
                freqCheck = lowRating.find(secondSplit[i].strip('\n')) #check if word is in tree already and remove new line
                if freqCheck != NIL: #increase frequency count but don't add node
                    freqCheck.value += 1 #increase word frequency count
                else: #not already in tree
                    lowRating.insert(secondSplit[i].strip('\n'), 1) #insert word, 1 is just temp value
                    keysToDel.append(secondSplit[i].strip('\n')) #add key to keys list for highRating deletion

fineFoods.close()
'''
# does what Q3 asks for
def treeSearch(BST, str):
    node = BST.find(str) # looks for string
    if node != NIL: # as long as node is not NIL (basically not a leaf, this poses a problem but works for what Q3 wants)
        print(str + " found %d times" % node.value)
    else: # not found (is a leaf/NIL)
        succ = BST.successor(str) # insert is not required :D
        print("Not found in tree: frequency = 0; successor is " + succ.key)

#Q3 HELPER CODE
print("LOW RATING")

treeSearch(lowRating, "asymptotic")
treeSearch(lowRating, "binary")
treeSearch(lowRating, "complexity")
treeSearch(lowRating, "depth")
treeSearch(lowRating, "mergesort")
treeSearch(lowRating, "quicksort")
treeSearch(lowRating, "structure")
treeSearch(lowRating, "theta")


print("HIGH RATING")

treeSearch(highRating, "asymptotic")
treeSearch(highRating, "binary")
treeSearch(highRating, "complexity")
treeSearch(highRating, "depth")
treeSearch(highRating, "mergesort")
treeSearch(highRating, "quicksort")
treeSearch(highRating, "structure")
treeSearch(highRating, "theta")

'''

# Q4 TOP 20
'''
highRating.distinctNodes = 0
for key in keysToDel:
    if highRating.find(key) != NIL:
        highRating.delete(key)
highRating.inOrderTraversal
print("Number of distinct nodes: " + str(highRating.distinctNodes))

'''