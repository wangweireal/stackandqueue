
class Stack(object):
	def __init__(self):
		self.stack = []
	
	def pop(self):
		if self.is_empty():
			return None
		else:
			return self.stack.pop()

	def push(self,val):
		return self.stack.append(val)

	def peak(self):
		if self.is_empty():
			return None
		else:
			return self.stack[-1]

	def size(self):
		return len(self.stack)

	def is_empty(self):
		return self.size() == 0		


class Queue(object):
	def __init__(self):
		self.queue = []

	def enqueue(self,val):
		self.queue.insert(0,val)

	def dequeue(self);
		if self.is_empty():
			return None
		else:
			return self.queue.pop()

	def size(self);
		return len(self.queue)

	def is_empty(self):
		return self.size() == 0	


#use queue imitate	 stack
class StackByQueue(object):	
	def __init__(self):
		self.stack = Queue()

	def push(self,val):
		self.stack.enqueue(val)

	def pop(self):
		for i in range(self.stack.size()-1):
			value = self.stack.dequeue()
			self.stack.enqueue(value)
		return self.stack.dequeue()
		

#use stack imitate queue
class QueueByStack(object):
	def __init__(self):
		self.queue1 = Stack()
		self.queue2 = Stack()

	def enqueue(self,val):
		self.queue1.push(val)

	def dequeue(self):
		for i in range(self.queue1.size()-1)		
			value = self.queue1.pop()
			self.queue2.push(value)
		res = self.queue1.pop()
		for i in range(self.queue2.size()):
			value = self.queue2.pop()
			self.queue1.push(value)
		return res
		
				


			
						

