class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        i = 0
        while current and i < index:
            current = current.next_node
            i += 1
        if current:
            return current.data
        else:
            return None

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next_node
            return
        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next_node
            i += 1
        if current and current.next_node:
            current.next_node = current.next_node.next_node

    def insert(self, n, val):
        if n <= 0:
            new_node = Node(val)
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            i = 0
            while current and i < n - 1:
                current = current.next_node
                i += 1
            if current:
                new_node = Node(val)
                new_node.next_node = current.next_node
                current.next_node = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node

# Пример использования:
my_list = LinkedList()
my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(4)

for item in my_list:
    print(item)

print(my_list.get(2))  # Выводит 3
my_list.remove(1)
for item in my_list:
    print(item)

my_list.insert(2, 5)
for item in my_list:
    print(item)