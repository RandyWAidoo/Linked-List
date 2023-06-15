class LinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
        
        def get(self): return self.data

        def delete(self): self.data = None
    
    def __init__(self, iterable=[]):
        self.head = None
        self.tail = None
        self.len = 0
        if len(iterable) > 0: 
            dummy = self.Node()
            self.tail = dummy
            for data in iterable:
                self.tail.next = self.Node(data, None, self.tail)
                self.tail = self.tail.next
                self.len += 1
            self.head = dummy.next
            self.head.prev = None

    def __len__(self): return self.len

    def get(self, index):
        if index < 0:
            curr = self.tail
            for _ in range(abs(index)): 
                curr = curr.prev
            return curr
        curr = self.head
        for _ in range(index): 
            curr = curr.next
        return curr

    def append(self, data):
        if not self.len:
            self.head = self.Node(data, None, None)
            self.tail = self.head
            self.len = 1
            return
        self.tail.next = self.Node(data, None, self.tail)
        self.tail = self.tail.next
        self.len += 1

    def insert(self, index, data):
        if not self.len:
            if index == 0 or index == -1:
                self.head = self.Node(data, None, None)
                self.tail = self.head
                self.len = 1
            else: 
                raise ValueError("Insertion index out of range")
            return
        index = index if isinstance(index, self.Node) else self.get(index)
        node = self.Node(data, index, index.prev)
        index.prev.next = node
        index.prev = node
        self.len += 1

    def pop(self, index):
        index = index if isinstance(index, self.Node) else self.get(index)
        if index is self.head:
            self.head = self.head.next
        elif index is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            index.prev.next = index.next
            index.next.prev = index.prev
        self.len -= 1

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0

    
    def copy(self):
        copy = LinkedList()
        curr = self.head
        for _ in range(self.len): 
            copy.append(curr.data)
            curr = curr.next
        return copy
    
    def __iter__(self):
        self.curr = self.Node(None, self.head)
        return self

    def __next__(self):
        self.curr = self.curr.next
        if self.curr == None: 
            raise StopIteration
        return self.curr
