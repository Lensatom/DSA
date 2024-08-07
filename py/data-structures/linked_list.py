"""/******************************************************

Implementation of a link-list in python
Author: Atayero Ayomide Samuel
Github: https://github.com/lensatom
LinkedIn: 
portfolio: 

******************************************************/"""

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
  
  """/**
  *
  * This function returns the size of the linked list
  *
  * It accesses the listSize attr and returns the size
  * of the linkedlist in constant time
  *
  * @return the size of the linked list
  *
  **/"""
  def size(self):
    return self.listSize
  
  """/**
  *
  * This function checks if the linked list is empty
  *
  * It checks if the head node is pointing to any address
  * and returns either true or false
  *
  * @return: True if the list is empty, otherwise, false
  *
  **/"""
  def empty(self):
    return self.head == None
  
  """/**
  *
  * This function gets the data stored at a particular
  * index in the linked list
  *
  * It loops over next addresses till the value of the
  * loop counter is equal to the value of the index given
  *
  * @param index: The index be be accessed in the linked list
  * @return: The data in the index given
  *
  **/"""
  def value_at(self, index):
    if (index >= self.listSize):
      raise Exception()
    curr_node_addr = self.data[self.head]
    i = 0
    while (i < index):
      curr_node_addr = self.data[curr_node_addr["next"]]
      i += 1
    return curr_node_addr["data"]
  
  """/**
  *
  * This function adds data to the first index
  * in the linked list.
  *
  * It creates a new node and arrors its next to
  * the current head node of the linked list the
  * makes the new node the new head and increases the
  * size of the list by 1
  *
  * @param data: The new data for the node to be
  * added to the front.
  * @return 1 to indicate success
  *
  **/"""
  def push_front(self, data):
    new_node = Node(data).get()
    new_node["next"] = self.head
    self.data[self.listSize] = new_node
    self.head = self.listSize
    self.listSize += 1
    return 1
  
  """/**
  *
  * This function removes a node from the front of
  * the linked list
  *
  * It reassigns the address of the linked list head
  * to the next address of the currnt linked list head
  * node and reduces the size of the list by 1
  *
  * @return 1 to indicate success
  *
  **/"""
  def pop_front(self):
    if (self.empty()):
      raise Exception()
    temp_head = self.head
    self.head = self.data[self.head]["next"]
    del self.data[temp_head]
    self.listSize -= 1
    return 1
  
  """/**
  *
  * This function adds data to the end of the linked list
  *
  * It creates a new node and assigns it to a new address.
  * It then goes to the node in the tail address and arrows
  * its next to the new node address.
  * Finally, it updates the tail address to the address of
  * the new node and increases the size of the list by 1
  *
  * @param data: The data to be used for the new node
  * @return: 1 to indicate success
  *
  **/"""
  def push_back(self, data):
    new_node = Node(data).get()
    self.data[self.tail]["next"] = self.listSize
    self.data[self.listSize] = new_node
    self.tail = self.listSize
    self.listSize += 1
    return 1
  
  """/**
  *
  * The fuction removes a node from the end of the
  * linked list
  *
  * It loops through the list till its at the index
  * of th second to the last node. It sets its next to
  * none and deletes the node in the next address.
  * Finally, it updates the tail address to the address
  * of the second to the last node and reduces the size of
  * the list by 1
  *
  * @return the data in the removed node
  *
  **/"""
  def pop_back(self):
    if (self.empty()):
      raise Exception()
    if (self.listSize == 1):
      self.data = {}
      return 1
    
    curr_node_addr = self.head
    i = 0
    while (i < self.listSize - 2):
      self.tail = self.data[curr_node_addr]["next"]
      curr_node_addr = self.data[curr_node_addr]["next"]
      i += 1

    popped = self.data[self.data[curr_node_addr]["next"]]
    del self.data[self.data[curr_node_addr]["next"]]
    self.data[curr_node_addr]["next"] = None
    self.listSize -= 1
    return popped["data"]
  
  """/**
  *
  * This function gets the data in the node at the front
  * of the linked list
  *
  * It goes to the node in the head address and returns the
  * the data in the node
  *
  * @return the data in the front of the linked list
  *
  **/"""
  def front(self):
    if (self.empty()):
      raise Exception()
    return self.data[self.head]["data"]
  
  """/**
  *
  * This function gets the data in the node at the end
  * of the linked list
  *
  * It goes to the node in the tail address and returns the
  * the data in the node
  *
  * @return the data at the end of the linked list
  *
  **/"""
  def back(self):
    if (self.empty()):
      raise Exception()
    return self.data[self.tail]["data"]
  
  """/**
  *
  * This function inserts data in a given index
  * in the linked list
  *
  * It creates a new node and assigns it an address
  * It loops through the linked list till its at the index
  * before the given index and stores its current next adress.
  * It then changes its next adress to the address of the new node and
  * gives the new node the adrress of the stored next address of the
  * previous node
  *
  * @param index: The index to add the new data node
  * @param value: The data for the new node
  * @return 1 to indicate success
  *
  **/"""
  def insert(self, index, value):
    new_node = Node(value).get()
    self.data[self.listSize] = new_node
    if (index >= self.listSize):
      return self.push_back(value)
    
    curr_node_addr = self.head
    i = 0
    while (i < index - 1):
      curr_node_addr = self.data[curr_node_addr]["next"]
      i += 1

    prev_node_addr = self.data[curr_node_addr]["next"]
    self.data[curr_node_addr]["next"] = self.listSize
    self.data[self.listSize]["next"] = prev_node_addr
    self.listSize += 1
    return 1
  
  """/**
  *
  * This function removes data from a given index in
  * the linked list
  *
  * loops through the list till its at the node before the
  * given index then changes its next to the next in the next node
  * then deletes the node in the given index and reduces thwe size
  * of the linked list by 1
  *
  * @param index: The index to be removed
  * @return the data at the given index
  *
  **/"""
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