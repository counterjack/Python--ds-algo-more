# /bin.python


"""

Refer :  https://www.geeksforgeeks.org/trie-insert-and-search/

Strings used essentially as in 
1. Search Engines
2. Genome Analytics
3. Data Analytics
4. Mobile Name Searching 
5. 

"""


class TrieNode(object):
	# node that can have maximum 26 childrens { alphabets a-z }
	def __init__(self):
		self.children = [None]*26
		self.is_end_of_word = False
		


class Trie(object):

	def __init__(self):
		"""	
			Init method creating root node
		"""
		self.root = self.get_node()

	def get_node(self):
		"""
			will return new node
		"""
		return TrieNode()
	
	def get_index(self, char):
		"""
			will return index of the given char in alphabet series. 
			{ a:1, b:2, ... z=26}
		"""
		return ord(char)-ord('a')

	def insert(self, key):
		parent_node  = self.root
		length = len(key)
		for item in key:
			index = self.get_index(item)	
			if parent_node.children[index] is None:
				# insert a new node at that index
				parent_node.children[index] = self.get_node()
			parent_node =  parent_node.children[index]
		# mark leaf node as last node
		parent_node.is_end_of_word = True
		

	def search(self, key):
		"""
			search the given key in tree. 		
		"""
		parent_node = self.root
		length = len(key)
		for item in key:
			index = self.get_index(item)
			if parent_node.children[index] is None:
				return False
			parent_node = parent_node.children[index]
		return parent_node is not None and parent_node.is_end_of_word


def main():
	trie  = Trie()
	keys = ["the","a","there","anaswe","any",
            "by","their"]
	output = ["Not present in trie",
              "Present in tire"]
	insert=	[trie.insert(key) for key in keys ]
	print("{} ---- {}".format("the",output[trie.search("the")]))
	print("{} ---- {}".format("these",output[trie.search("these")]))
	print("{} ---- {}".format("their",output[trie.search("their")]))
	print("{} ---- {}".format("thaw",output[trie.search("thaw")]))

main()
