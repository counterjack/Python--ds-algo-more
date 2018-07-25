"""
Refer : contact : ankurnitp@gmail.com

"""
#/bin/python
prefix_postfix_choice = input('1: Prefix Expression, 2: Postfix Expression')
user_input  = input() #  prefix expression
from Queue import Queue
char_to_ignore = ['(', ')','[', ']']
operators = ['+', '-', '/', '*']


class Stack(object):
	"""
		implementing stack "LIFO" concept using List
	"""
	def __init__(self, **kwargs):
		self.__stack = []
			
	def push(self, element):
		return self.__stack.append(element)	
			
	def pop(self):
		try:		
			return self.__stack.pop(len(self.__stack)-1)	
		except:
			return Exception ('Blank Stack. No element found')

	def size(self):
		return len(self.__stack)

	def seek(self, index):
		try:
			return self.__stack[index]
		except Exception as e:
			return e.message

	def isEmpty(self):
		return not self.__stack
	
	def isFull(self):
		raise Exception ('To be implemented')
	

def process_postfix_notation():
	result = Stack() 
	for item in user_input:
		if item in operators:
			# pop last 2 elements
			l1,l2 = map(int,[result.pop(), result.pop()])
				
			if item == '+':
				res = l1+l2
			elif item == '-':
				res = l1-l2
			elif item == '*':
				res = l1*l2
			elif item == '/':
				res = l1/l2
			result.push(res)
		else:
			result.push(item)
	
	print result.seek(0)
			
			
def process_prefix_notation():
	operand_count = 0
	result  = Stack() # using stack to process
	for item in user_input:
		if item not in operators:
			operand_count += 1
		result.push(item)	

		if operand_count == 2:			
			# pop last 2 operands 
			l1,l2 = map(int,[result.pop(), result.pop()])
			# pop operator also
			operator = result.pop()				
			if operator  == '+':
				res = l1+l2
			elif operator  == '-':
				res = l1-l2
			elif operator == '*':
				res = l1*l2
			elif operator == '/':
				res = l1/l2
			result.push(res)
			operand_count = 0
	
	print result.seek(0)

'''
methods_call = {
	1: process_prefix_notation(), 
	2: process_postfix_notation()
	}
'''
#methods_call[prefix_postfix_choice]

if prefix_postfix_choice == 1:
	process_prefix_notation()
else:
	process_postfix_notation()


"""

More Stack applications :
1. Memory Management 
	call stack --> Activation Records --> { Return Address, Previous Pointer, Return Value, Local Variables, Parameters }

2. BackTracking
3. Expressions Evaluation
4. Undo the actions. ( Editor Undo Functionality )
5. Syntax Checking
6. Balance Paranthesis
7. Browser Back/Forth
8. 

"""
