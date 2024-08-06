class Vector:
  def __init__(self, capacity):
    self.capacity = capacity
    self.size = 0
    self.data = [None] * capacity
  
  def size(self):
    return self.size
  
  def capacity(self):
    return self.capacity

  def is_empty(self):
    return self.size == 0
  
  def at(self, index):
    if (index >= self.size):
      raise Exception("index out of capacity bounds")
  
  def push(self, item):
    self.data[self.size] = item
    self.size += 1
  
  def insert(self, index, item):
    if (index >= self.capacity):
      raise Exception("index out of capacity bounds")

    i = index
    while (i < self.capacity - 1):
      temp = self.data[index]
      self.data[i + 1] = temp
      i += 1
    self.data[index] = item

  def prepend(self, item, insert=insert):
    insert(self, 0, item)

  def pop(self, is_empty=is_empty):
    if (is_empty(self)):
      return 0