red = "red"
black = "black"

class leaf(object):
	def __init__(self):
		self.color = black

NIL = leaf()

class rbtNode(object):
	def __init__(self, key, value, color = red, leftchild = NIL, rightchild = NIL, parent = NIL):
		assert color in (red, black)
		self.color, self.key, self.value, self.leftchild, self.rightchild, self.parent = (color, key, value, leftchild, rightchild, parent)



class BSTree(object):
	def __init__(self, root = NIL):
		self.root = root

	def leftRotation(self, node):

		assert(node.rightchild != NIL)
		tempNode = node.rightchild
		node.rightchild = tempNode.leftchild
		if tempNode.leftchild != NIL:
			tempNode.leftchild.parent = node
		tempNode.parent = node.parent
		if node.parent == NIL:
			self.root = tempNode
		elif node == node.parent.leftchild:
			node.parent.leftchild = tempNode
		else:
			node.parent.rightchild = tempNode
		tempNode.leftchild = node
		node.parent = tempNode

	def rightRotation(self, node):

		assert(node.leftchild != NIL)
		tempNode = node.leftchild
		node.leftchild = tempNode.rightchild
		if tempNode.rightchild != NIL:
			tempNode.rightchild.parent = node
		tempNode.parent = node.parent
		if node.parent == NIL:
			self.root = tempNode
		elif node == node.parent.rightchild:
			node.parent.rightchild = tempNode
		else:
			node.parent.leftchild = tempNode
		tempNode.rightchild = node
		node.parent = tempNode

	# A function to insert items into the BST
	def rbtInsertHelper(self, node):
		
		tempNode = NIL
		currentNode = self.root
		while currentNode != NIL:
			tempNode = currentNode
			if node.key < currentNode.key:
				currentNode = currentNode.leftchild
			else:
				currentNode = currentNode.rightchild
			node.parent = tempNode
			if tempNode == NIL:
				self.root = node
			elif node.key < tempNode.key:
				tempNode.leftchild = node
			else:
				tempNode.rightchild = node
		return


	def insert(self, key, value = 1):
		node = NIL
		node.key = key
		node.value = value
		self.rbtInsertHelper(node)
		node.color = red
		while node != self.root and node.parent.color == red:
			if node.parent == node.parent.parent.leftchild:
				tempNode = node.parent.parent.rightchild
				if tempNode.color == red:
					node.parent.color = black
					tempNode.color = black
					node.parent.parent.color = red
					node = node.parent.parent
				else:
					if node == node.parent.rightchild:
						node = node.parent
						leftRotation(self, node)
					node.parent.color = black
					node.parent.parent.color = red
					rightRotation(self, node.parent.parent)
			else:
					tempNode = node.parent.parent.leftchild
					if tempNode.color == red:
						node.parent.color = black
						tempNode.color = black
						node.parent.parent.color = red
						node = node.parent.parent
					else:
						if node == node.parent.leftchild:
							node = node.parent
							rightRotation(self, node)
						node.parent.color = black
						node.parent.parent.color = red
						left(self, node.parent.parent)
		self.root.color = black


	def delete(self, key):
		return

	# A function to find values in the BST
	def find(self, key):

		node = self.root # Start at the root of the BST
		while node != None: # While the node exists
			if node.key == key: # If it matches the key 
				return node # Return the node
			if node.key > key: # If the key is less
				node = node.leftchild # look in left subtree
			else:
				node = node.rightchild # If it is equal too or greater, look in right subtree
		return None # Return NULL for any other cases

	def minimum(self, node):
		while node.leftchild != NIL:
			node = node.leftchild
			return node

	def successor(self, key):
		node = NIL
		node.key = key
		if node.rightchild != NIL:
			return self.minimum(node.rightchild)
		tempNode = node.parent
		while tempNode != NIL and node == tempNode.rightchild:
			node = tempNode
			tempNode = tempNode.parent
		return(tempNode)

	def inOrderTraversal(self): # Function that prints BST in sorted order

		self.inOrderTraversalHelper(self.root) # Call to helper function w/ param root
		 

	def inOrderTraversalHelper(self, node): # Helper function that prints BST in sorted order
 
		if node != None: # If the node exists
			self.inOrderTraversalHelper(node.leftchild) # Recursively iterate through left subtree
			print(node.key, " " ,node.value) # Print key and value
			self.inOrderTraversalHelper(node.rightchild) # When done with left subtree, move to the right subtree


	
rbt = BSTree()
rbt.insert("c", 1)
rbt.insert("a", 2)
rbt.insert("b", 3)
rbt.insert("d", 4)
rbt.insert("e", 5)
rbt.inOrderTraversal()












