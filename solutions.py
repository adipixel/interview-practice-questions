def question1(s, t):
	# removing blank spaces from the string
	s = s.strip().lower()
	t = t.strip().lower()
	sLen = len(s)
	tLen = len(t)

	# iterating over the string s
	for i in range(0,sLen-tLen+1):
		if isAnagram(s[i:i+tLen], t):
			return True

	return False


# checks for anagram
def isAnagram(s1,s2):
	s1Dic = {}
	# creating a Map (dictionary) to store alphabet count from s1
	for x in s1:
		if x in s1Dic:
			s1Dic[x] += 1
		else:
			s1Dic[x] = 1

	# checking for availability of all the alphabets from string s2
	for x in s2:
		if x in s1Dic and s1Dic[x]>0:
			s1Dic[x] -= 1
		else:
			return False

	return True


def question2(a):
	if a == "":
		return None
	a = a.lower()
	palindrome = {}

	# initializing default values
	palindrome["text"] = a[0]
	palindrome["length"] = 1

	for i in range(0, len(a)):
		for j in range(0, i):
			subStr = a[j:i+1]
			# check if palindromes
			if subStr == subStr[::-1]:
				subLen = len(subStr)
				if subLen > palindrome["length"]:
					palindrome["text"] =  subStr
					palindrome["length"] = subLen

	return palindrome["text"]

# supporting function for question3
def union(V1, V2, rank ,parent):
	root1 = search(V1, parent)
	root2 = search(V2, parent)
	if (root1 != root2):
		if (rank[root1] <= rank[root2]):
			parent[root1] = root2
			if rank[root1] == rank[root2]:
				rank[root2] += 1
		else:
			parent[root2] = root1

# supporting function for question3
# search for the set of V
def search(V, parent):
	if parent[V] != V:
		parent[V] = search(parent[V], parent)
	return parent[V]

# Minimum spanning tree using Kruskal's Algorithm
def question3(G):
	parent = {}
	rank = {}
	graph = G
	vertices = []
	edges = []
	result = {}
	MST = set()

	# generating vetices and edges from the given graph
	for V in graph.keys():
		vertices.append(V)
		verticeEdges = graph[V]
		for verticeEdge in verticeEdges:
			source = V
			destination, weight = verticeEdge
			edges.append((source, destination, weight))

	# initializing
	for V in vertices:
		parent[V] = V
		rank[V] = 0

	# sorting edges in non decresing values of weights
	edges = sorted(edges, key=lambda item : item[2])

	for E in edges:
		# selection of node
		if (search(E[0], parent) != search(E[1], parent)):
			# adding in MST
			MST.add(E)
			union(E[0], E[1], rank, parent)

	# generating results
	for node in MST:
		source = node[0]
		destination = node[1]
		weight = node[2]

		if (destination < source):
			source = node[1]
			destination = node[0]

		if (source not in result):
			result[source] = [(destination, weight)]
		else:
			result[source].append((destination, weight))

	return result


def question4(T, r, n1, n2):
	# boundary conditions check
	n = len(T[0])
	if r < 0 or r >= n:
		return "Invalid Input"
	R = [[ 0 for x in range(0, len(T[0]))] for y in range(0, len(T[0]))]
	fillAllChildrenMatrix(T, R, r, [r])
	return findNode(R, n1, n2)

def fillAllChildrenMatrix(T, R, r, ancestorList):
	for x in range(0, len(T[0])):
		if T[r][x] == 1:
			R[r][x] = 1
			# filling 1 in all ancestors
			for a in ancestorList:
				R[a][x] = 1
			# adding current child and recursive call
			fillAllChildrenMatrix(T, R, x, ancestorList + [x])


# This function finds node with childrens n1 and n2
# and with the farthest node from the root that is an ancestor
# of both nodes
def findNode(R, n1, n2):
	minOnesRow = 0
	minCount = len(R[0])+1
	for x in range(0, len(R[0])):
		if R[x][n1] == 1 and R[x][n2] == 1:
			count = 0
			for y in range(0,len(R[0])):
				if R[x][y] == 1:
					count += 1
			if minCount > count:
				minCount = count
				minOnesRow = x
	return minOnesRow




# supporting class for question 5
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


# supporting class for question 5
class LinkedList(object):
	def __init__(self, head):
		# initializing head of the linked list
		if head:
			self.head = head
		else:
			self.head = None

	# adding node to linked list
	def addNode(self, node):
		curNode = self.head
		if self.head == None:
			self.head = node
		else:
			# finding the tail and adding node
			while curNode.next != None:
				curNode = curNode.next
			curNode.next = node

	def getNodeFromTail(self, m):
		# initializing pointers
		listPtr = self.head
		dataPtr = self.head

		# placing the list pointer ahead by m nodes
		if self.head == None:
			return None
		else:
			for x in range(0,m):
				if listPtr == None:
					return "Invalid value of m"
				else:
					listPtr = listPtr.next

		# shifting both pointers
		while listPtr != None:
			listPtr = listPtr.next
			dataPtr = dataPtr.next

		return dataPtr.data

def question5(ll, m):
	return ll.getNodeFromTail(m)


def main():
	print("\n*****Question1*****")
	# test case 1
	print("Input Strings: 'udacity', 'ad'")
	print("Result: Is it an Anagram?")
	print(question1("udacity", "ad"))
	# expected output: True

	# test case 2
	print("Input Strings: 'udacity', ''")
	print("Result: Is it an Anagram?")
	print(question1("udacity", ""))
	# expected output: True

	# test case 3
	print("Input Strings: '', 'ad'")
	print("Result: Is it an Anagram?")
	print(question1("", "ad"))
	# expected output: False

	# test case 4
	print("Input Strings: 'udacity', 'dy'")
	print("Result: Is it an Anagram?")
	print(question1("udacity", "dy"))
	# expected output: False


	print("\n\n*****Question2*****")
	# test case 1
	print("Input String: 'adityaaytodssdot'")
	print("Result: Longest palindrome")
	print(question2("adityaaytodssdot"))
	# expected output: todssdot

	# test case 2
	print("Input String: ''")
	print("Result: Longest palindrome")
	print(question2(""))
	# expected output: None

	# test case 3
	print("Input String: 'abc'")
	print("Result: Longest palindrome")
	print(question2("abc"))
	# expected output: a

	print("\n\n*****Question3*****")
	# test case 1
	G = {'A': [('B', 2)],
		 'B': [('A', 2), ('C', 5)],
		 'C': [('B', 5)],
		}
	print ("Input Graph:")
	print(G)
	answer = question3(G)
	print("Result: Minimum Spanning Tree")
	print(answer)
	# expected output: {'A': [('B', 2)], 'B': [('C', 5)]}

	# test case 2
	G = {'A': [('B', 10), ('C', 1)],
		 'B': [('A', 10), ('C', 3), ('D', 32), ('E', 5)],
		 'C': [('A', 1), ('B', 3), ('D', 1)],
		 'D': [('B', 32), ('C', 1), ('E', 3)],
		 'E': [('B', 5), ('D', 3)],
		}
	print ("Input Graph:")
	print(G)
	answer = question3(G)
	print("Result: Minimum Spanning Tree")
	print(answer)
	# expected output: {'A': [('C', 1)], 'B': [('C', 3)], 'C': [('D', 1)], 'D': [('E', 3)]}

	# test case 3
	G = {}
	print ("Input Graph:")
	print(G)
	answer = question3(G)
	print("Result: Minimum Spanning Tree")
	print(answer)
	# expected output: {}


	print("\n\n*****Question4*****")
	# test case 1
	T =[[0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[1, 0, 0, 0, 1],
	[0, 0, 0, 0, 0]]
	print ("Input Tree:")
	print(T)
	print("Result: Least common ancestor of 1 and 4 with root as 3")
	print(question4(T, 3, 1, 4))
	# expected output: 3

	# test case 2
	T =[[0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0]]

	print ("Input Tree:")
	print(T)
	print("Result: Least common ancestor of 1 and 4 with root as 5")
	print(question4(T, 5, 1, 4))
	# expected output: 3

	# test case 3
	T =[[0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]]
	print ("Input Tree:")
	print(T)
	print("Result: Least common ancestor of 1 and 4 with root as 6")
	print(question4(T, 6, 1, 4)) # invalid root
	# expected output: Invalid Input


	print("\n\n*****Question5*****")
	head = Node(0)
	ll = LinkedList(head)

	# test case 1
	print ("Input: LinkedList = 0(only head), m = 1")
	print("Result: Value of 1st node from tail of the Linked list is: ")
	print(question5(ll, 1))
	# expected output: 0

	# adding total 10 nodes (node0 to node9) including head
	for x in range(1,10):
		ll.addNode(Node(x))

	# test case 2
	print ("Input: LinkedList = 0>1>2>3>4>5>6>7>8>9, m = 3")
	print("Result: Value of 3rd node from tail of the Linked list is: ")
	print(question5(ll, 3))
	# expected output: 7

	# test case 3
	print ("Input: LinkedList = 0>1>2>3>4>5>6>7>8>9, m = 20")
	print("Result: Value of 20th node from tail of the Linked list is: ")
	print(question5(ll, 20))
	# expected output: Invalid value of m

	print()

main()