
from object.object import Object
class Node:
  object = {"manhata":int,"object":Object,"name":str}
  children = []
  distance = int
  id = int

  def __init__(self,object,id):
    self.object = object
    self.id = id
    self.children = []

