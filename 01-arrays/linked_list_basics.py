class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create 3 nodes manually
first = Node(10)
second = Node(20)
third = Node(30)

# Link them together
first.next = second
second.next = third

# Traverse and print
current = first
while current is not None:
    print(current.value)
    current = current.next