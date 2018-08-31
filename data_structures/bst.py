# bin/pyhton

"""
implementation of BST Python

"""



class Node(object):


	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		

class BST(Node):
	
	def __init__(self, data):
		return super(BST, self).__init__(data)

		
	def insert(self, data):
		
		if self.data >= data:
			if self.left is None:
				self.left = BST(data)
			else:
				self.left.insert(data)

		elif self.data < data:
			if self.right is None:				
				self.right = BST(data)			
			else:
				self.right.insert(data)
		else:
			pass


root = BST(3)
root.insert(2)
root.insert(1)
root.insert(4)		

while ( root.left):
	print root.data
	root = root.left
print root.data

while root.left or root.right:
	print root.data
	root = root.right
		
		
		
