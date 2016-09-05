# HW6.py
# Sources: TA's, Piazza, Google (for general python questions), Stack Overflow (python class information)
# python visualizer (to walk through BST implementation, and debug)


#****************************************************************************************************************
# Q1
#****************************************************************************************************************


class BSTreeNode: # Create a class that constructs the node that is in a BST
	
	# This is the initialization method, that creates a new instance  of the node everytime it is called
	# Also known as a constructor
	def __init__(self, key, value, parent = None, left = None, right = None):

		self.key = key # The key of the node, which is just a word
		self.value = value # The value of the node, which is a pos # representing the freq
		self.parent = parent # A node that is a parent
		self.left = left # A node that is a left child
		self.right = right # A node rhat is a right child


class BSTree(object): # Create a class for the actual BST implementation

	# This is the initialization method, that creats a new instance everytime it is called
	# Also known as a constructor
	def __init__(self):
		
		self.root = None # The root of tree, initialized to empty



	# A function to insert items into the BST
	def insert(self, key, value = 1):
		
		if None == self.root:
			self.root = BSTreeNode(key, value)
			return 
		currentNode = self.root
		while currentNode: # While the node that we at exisits
			if key < currentNode.key: # If the input is less than noe
				if currentNode.left: # And a left node exists
					currentNode = currentNode.left # Assign the new current node we are at, to left most val
				else: # If we cannot go anymore left
					currentNode.left = BSTreeNode(key, value, currentNode) # Create a left node that is left child
					return 
			else: # If the val is greater than or equal to the current node we are at
				if currentNode.right: # And the current node exisits
					currentNode = currentNode.right # Iterate to the next  right most child
				else: # If it does not exist anymore
					currentNode.right = BSTreeNode(key, value, currentNode) # Create a right node that is right child
					return 


	# A function to delete items from the BST
	def delete(self, key):

		node = self.find(key) # Look for the key we need to delete, and track it
		if node != None: # While that node exists
			self.deleteHelper(node) # Pass into helper function
			return None # Return true if node is deleted successfully


	def deleteHelper(self, node): # Helper function 1, basically to assign deletion cases

		if node.left != None and node.right != None: # If the node has 2 children
			successor = node.right # Find the successor
			while successor.left != None: # Iterate to find min val on right subtree
				successor = successor.left
			node.key = successor.key # Copy successor key
			node.value = successor.value # Copy successor value
			self.deleteHelper(successor) # Recursively delete the successor
		elif node.left != None: # If the node only has a left child
			self.deleteHelper2(node, node.left) # pass into helper function to remove
		elif node.right != None: # If the node only has a right child 
			self.deleteHelper2(node, node.right) # Pass into helper function to remove
		else: # If the node has no children
			self.deleteHelper2(node, None)  # Pass into helper function to remove
		return None # Return a NULL values

	
	def deleteHelper2(self, node, newNode):  # Helper function, to actually delete the node

		if node == self.root: # When the node is the root
			self.root = newNode # Point to new node as root
			return None # Return NULL
		parent = node.parent # Keep track of parent nodes
		if parent.left != None and parent.left == node: # If parent of left node exists, and we have the correct node
			parent.left = newNode # Point to the new node 
		elif parent.right != None and parent.right == node: # If the right parent exists and is correct node
			parent.right = newNode # Point to right node
		else:
			return None # Return NULL for any other error cases


	# A function to find values in the BST
	def find(self, key):

		node = self.root # Start at the root of the BST
		while node != None: # While the node exists
			if node.key == key: # If it matches the key 
				return node # Return the node
			if node.key > key: # If the key is less
				node = node.left # look in left subtree
			else:
				node = node.right # If it is equal too or greater, look in right subtree
		return None # Return NULL for any other cases


	# A function to find the successor of a node in the BST
	def successor(self, key):

		node = self.find(key)
		if node ==  None: # If input it is empty or not in BST
			return None # Return Null
		if node.right is not None: # If the value has a right child
			successor = node.right # The sucessor is the right child
			while successor.left: # If the right child has a left child
				successor = successor.left # The succesor is then the min value in the right subtree
			return successor # Return that value
		if node.right is None: # If the val has no right child
			successor = node.parent.right # Return the right most ancestor of the value
			return successor


	def inOrderTraversal(self): # Function that prints BST in sorted order

		self.inOrderTraversalHelper(self.root) # Call to helper function w/ param root
		 

	def inOrderTraversalHelper(self, node): # Helper function that prints BST in sorted order
 
		if node != None: # If the node exists
			self.inOrderTraversalHelper(node.left) # Recursively iterate through left subtree
			print(node.key, " " ,node.value) # Print key and value
			self.inOrderTraversalHelper(node.right) # When done with left subtree, move to the right subtree



#****************************************************************************************************************
# Q2
#****************************************************************************************************************

highRating = BSTree()
lowRating = BSTree()   
   

ignore = set()
stopwords = open("stopwords.txt", "r")
for line in stopwords:
    ignore.add(line.strip('\n'))
stopwords.close()

fineFoods = open("finefoods_cleaned.txt") #using tiny fraction of original

for line in fineFoods:
    firstSplit = line.split(":", 1) #gets the number, limits splits to 1 just to make sure words are in one index
    secondSplit = firstSplit[1].split(" ") #words are in second index and are now seperated
    if int(firstSplit[0]) > 3: #go in tree with high rating
        for i in range(len(secondSplit)): #iterate through each word
            check = secondSplit[i] in ignore #check if word should be ignored, strings in ignore have new line character
            if check != True: #if word is not in set of words to ignore
                freqCheck = highRating.find(secondSplit[i].strip('\n')) #check if word is already in tree and remove new line
                if freqCheck: #increase frequency count but don't add node
                	freqCheck.value += 1 #Increase word frequency count
                else: #not already in tree
                	highRating.insert(secondSplit[i].strip('\n'), 1) #insert word, 1 is just temp value
    else:
	    for i in range(len(secondSplit)): #iterate through each word
		    check = secondSplit[i] in ignore #check if word should be ignored, strings in ignore have new line character
		    if check != True: #as long as word is not in ignore
			    freqCheck = lowRating.find(secondSplit[i].strip('\n')) #check if word is in tree already and remove new line
			    if freqCheck: #increase frequency count but don't add node
				    freqCheck.value += 1 #increase word frequency count
			    else: #not already in tree
				    lowRating.insert(secondSplit[i].strip('\n'), 1) #insert word, 1 is just temp value


fineFoods.close()




#****************************************************************************************************************
# Q3 HELPER CODE
#****************************************************************************************************************

'''
#searches 
def treeSearch(BST, str):
    node = BST.find(str)
    if node:
        print(str + " found %d times" % node.value)
    else:
        print(BST.successor(str))


def searchDelete(BST, str):
    global numHigh
    node = BST.find(str)
    if node:
        BST.delete(str)
        numHigh -= 1
    else:
        return "Not found"
        
#top 20 frequent words in lowRating
frequentWordsLR = {"coffee", "taste", "love", "flavor", "tea", "proudct",
                        "food", "little", "time", "amazon", "tried", "price",
                        "buy", "try", "eat", "dog", "found", "chocolate", "bag",
                        "drink"}

#delete nodes from highRating that have top 20 keys from lowRating
for i in frequentWordsLR:
    searchDelete(highRating, i)

print(numHigh)
        
#ASYMPTOTIC
treeSearch(lowRating, "asymptotic")
treeSearch(highRating, "asymptotic")


print("finished") #finished running



'''





