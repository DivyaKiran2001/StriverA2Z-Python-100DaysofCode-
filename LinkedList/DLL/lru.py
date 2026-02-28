
from sys import stdin

class Node():
	def __init__(self,key,value):
		self.key=key
		self.value=value
		self.next=None
		self.prev=None

class LRUCache:
	# Initialize the LRU Cache
	def __init__(self, capacity):
		# Your code goes here
		self.head = Node(-1, -1)
		self.tail = Node(-1, -1)
		self.head.next=self.tail
		self.tail.prev=self.head
		self.capacity=capacity
		self.nodemap={}
	
	# def insertAfterHead(self,nd):
	# 	curafterhead=self.head.next
	# 	# self.head.next=nd
	# 	nd.next=curafterhead
	# 	# nd.prev = self.head
	# 	curafterhead.prev = nd
	# 	curafterhead=nd

	def insertAfterHead(self, node):
		node.next = self.head.next
		node.prev = self.head
		self.head.next.prev = node
		self.head.next = node
	
	def deleteNode(self,nd):
		prevNode=nd.prev
		afterNode=nd.next
		prevNode.next=afterNode
		afterNode.prev=prevNode
	
	def get(self, key):
		# Your code goes here
		if key not in self.nodemap:
			return -1
		node = self.nodemap[key]
		self.deleteNode(self.nodemap[key])
		self.insertAfterHead(self.nodemap[key])
		return node.value

	def put(self, key, value):
		if self.capacity == 0:
			return
		# Your code goes here
		if key in self.nodemap:
			node=self.nodemap[key]
			node.value=value
			self.deleteNode(node)
			self.insertAfterHead(node)
		else:
			if len(self.nodemap)==self.capacity:
				node=self.tail.prev
				del self.nodemap[node.key]
				self.deleteNode(node)
			nd=Node(key,value)
			self.nodemap[key]=nd
			self.insertAfterHead(nd)
# main
capacity, q = map(int, stdin.readline().rstrip().split(" "))

cache = LRUCache(capacity)

while q != 0:
	query = list(map(int, stdin.readline().rstrip().split()))

	if query[0] == 0:
		key = query[1]
		print(cache.get(key))
	elif query[0] == 1:
		key = query[1]
		value = query[2]
		cache.put(key, value)
	
	q -= 1
