class DoubleElement:
    def __init__(self, *lst):
        self.elements = list(lst)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.elements):
            pair = (self.elements[self.index], self.elements[self.index + 1] if self.index + 1 < len(self.elements) else None)
            self.index += 2
            return pair
        else:
            raise StopIteration


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)