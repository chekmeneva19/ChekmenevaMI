class Node:

    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None
class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):

        if self.start is None:
            return None  # Очередь пуста
        val = self.start.data
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None
        return val

    def push(self, val):

        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):

        new_node = Node(val)
        if n == 0:
            if self.start is not None:
                new_node.nref = self.start
                self.start.pref = new_node
                self.start = new_node
            else:
                self.start = new_node
                self.end = new_node
        else:
            current = self.start
            index = 0
            while current is not None and index < n:
                current = current.nref
                index += 1
            if current is None:
                self.end.nref = new_node
                new_node.pref = self.end
                self.end = new_node
            else:
                new_node.pref = current.pref
                new_node.nref = current
                current.pref.nref = new_node
                current.pref = new_node

    def print(self):

        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
        print()

