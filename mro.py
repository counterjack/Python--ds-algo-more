# usr/bin/python
"""

Refer : https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc
MRO : Method Resolution Order
Method Resolution Order is the hierarchy in which base classes are searched when looking for a method in the parent class

Algo Used : 

Old Class Ways : DLR ( Depth First, then go Left to right )
New Class Ways : c3 Linearization

<> Old classes : <>

class A():
	pass

<> New classes : <>

class A(object):
	pass


c3 linearization constraints :  ( c2 linearization algorithm preserves monotonicity )
1.) Children precede their parents
2.) If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.


"""

# new class mro 

class A(object):
	pass


class B(object):
	pass


class C(A, B):
	pass


class D(B, A):
	pass

class E(C):
	pass

print "MRO OF E "
print E.__mro__


# old class mro

class A():
	pass


class B():
	pass


class C(A, B):
	pass


class D(B, A):
	pass

class E(C):
	pass

print "MRO OF E "
print "E-> C-> A-> B"
