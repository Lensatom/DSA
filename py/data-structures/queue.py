"""
/******************************************************

Implementation of a queue using a linked-list in python
Author: Atayero Ayomide Samuel
Github: https://github.com/lensatom
LinkedIn: 
portfolio: 

******************************************************/
"""

from linked_list import CreateLinkedList

class Queue:
  def __init__(self, data):
    self.data = CreateLinkedList(data)

  """/**
  * This function chacks if the linked-list is empty
  *
  * It uses the linked-list "empty" function
  *
  * @return: True if queue is empty, otherwiae, False
  **/"""
  def empty(self):
    return self.data.empty()
  
  """/**
  * This adds a new item to the queue
  *
  * It uses the linked-list "push_back" method to add
  * the item to the end of the linked-list
  *
  * @param item: The item to be added to the queue
  * @return 1 to indicate success
  **/"""
  def enqueue(self, item):
    self.data.push_back(item)
    return 1
  
  """/**
  * This removed the oldest item in the queue and
  * returns the removed item
  *
  * It uses the linked-list "front" emthod to get the
  * oldest item and the "pop_front" method to remove
  * the oldest item
  *
  * @return oldest item in the queue
  **/"""
  def dequeue(self):
    if (self.empty()):
      raise Exception()
    dequeued = self.data.front()
    self.data.pop_front()
    return dequeued
