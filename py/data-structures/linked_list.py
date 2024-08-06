"""
/******************************************************

Implementation of a link-list in python
Author: Atayero Ayomide Samuel
Github: https://github.com/lensatom
LinkedIn: 
portfolio: 

******************************************************/
"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def get(self):
    return self.__dict__

class CreateLinkedList:
  def __init__(self, data):
    self.data = {0: Node(data).get()}
    self.head = 0
    self.tail = 0
    self.listSize = 1
  
  """
  /******************************

  - returns size of linkedlist

  ******************************/
  """
  def size(self):
    return self.listSize
  
  """
  /******************************

  - returns true if linkedlist is empty, otherwise, false

  ******************************/
  """
  def empty(self):
    # Check if there is an head address
    return self.head == None
  
  """
  /******************************

  - 

  ******************************/
  """
  def value_at(self, index):
    if (index >= self.listSize):
      raise Exception()
    currNode = self.data[self.head]
    i = 0
    while (i < index):
      currNode = self.data[currNode["next"]]
      i += 1
    return currNode["data"]
  
  """
  /******************************

  - 

  ******************************/
  """
  def push_front(self, data):
    # create new node
    new_node = Node(data).get()
    # arrow new node to head address
    new_node["next"] = self.head
    # insert new node in new address
    self.data[self.listSize] = new_node
    # update head address to new node address
    self.head = self.listSize
    # increase list size
    self.listSize += 1
    # return success
    return 1
  
  """
  /******************************

  - 

  ******************************/
  """
  def pop_front(self):
    # check if linkedlist is empty
    if (self.empty()):
      # return failure
      return 0
    # store current head address temporarily
    temp_head = self.head
    # assign new head address
    self.head = self.data[self.head]["next"]
    # delete data in previous head address
    del self.data[temp_head]
    # reduce linkedlist size by 1
    self.listSize -= 1
    # return success
    return 1
  
  """
  /******************************

  - 

  ******************************/
  """
  def push_back(self, data):
    # create new node with data
    new_node = Node(data).get()
    # arrow current linkedlist tail node "next" to new address
    self.data[self.tail]["next"] = self.listSize
    # store new node in the new address
    self.data[self.listSize] = new_node
    # assign new tail address
    self.tail = self.listSize
    # increase linkedlist size by 1
    self.listSize += 1
    # return success
    return 1
  
  """
  /******************************

  - 

  ******************************/
  """
  def pop_back(self):
    if (self.empty()):
      return 0
    if (self.listSize == 1):
      self.data = {}
      return 1
    currNode = self.head
    i = 0
    while (i < self.listSize - 2):
      self.tail = self.data[currNode]["next"]
      currNode = self.data[currNode]["next"]
      i += 1
    popped = self.data[self.data[currNode]["next"]]
    del self.data[self.data[currNode]["next"]]
    self.data[currNode]["next"] = None
    self.listSize -= 1
    return popped["data"]
  
  """
  /******************************

  - 

  ******************************/
  """
  def front(self):
    # check if linkedlist is empty
    if (self.empty()):
      # return failure
      return 0
    # return data in head address
    return self.data[self.head]["data"]
  
  """
  /******************************

  - 

  ******************************/
  """
  def back(self):
    # check if linkedlist is empty
    if (self.empty()):
      # return failure
      return 0
    # return data in tail address
    return self.data[self.tail]["data"]
  
  """
  /******************************

  - 

  ******************************/
  """
  def insert(self, index, value):
    new_node = Node(value).get()
    if (index >= self.listSize):
      self.data[self.listSize] = new_node
      self.data[self.tail]["next"] = self.listSize
      self.listSize += 1
      return 1
    
    curr_node_addr = self.head
    i = 0
    while (i < index - 1):
      curr_node_addr = self.data[curr_node_addr]["next"]
      i += 1

    prev_node_addr = self.data[curr_node_addr]["next"]
    self.data[curr_node_addr]["next"] = self.listSize
    self.data[self.listSize] = new_node
    self.data[self.listSize]["next"] = prev_node_addr
    self.listSize += 1
    return 1
  
  """
  /******************************

  - 

  ******************************/
  """
  def erase(self, index):
    if (index >= self.listSize):
      raise Exception()
    
    curr_node_addr = self.head
    i = 0
    while (i < index - 1):
      curr_node_addr = self.data[curr_node_addr]["next"]
      i += 1
    
    leaving_node_addr = self.data[curr_node_addr]["next"]
    self.data[curr_node_addr]["next"] = self.data[leaving_node_addr]["next"]
    del self.data[leaving_node_addr]

  """
  /******************************

  - 

  ******************************/
  """
  # def reverse(self):
  #   reversed_list = CreateLinkedList(self.data[self.head]["data"])
  #   reversed_list.pop_back()
  #   curr_node_addr = self.head
  #   self.head = 0
  #   i = 0
  #   while (i < self.listSize):
  #     reversed_list.push_front(self.data[curr_node_addr]["data"])
  #     if (self.data[curr_node_addr]["next"] == None):
  #       break
  #     curr_node_addr = self.data[curr_node_addr]["next"]
  #     i += 1
  #   self.tail = curr_node_addr
    
  #   self.data = reversed_list.data