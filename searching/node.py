from object.object import Object

#clase que identifica a un nodo del árbol de busqueda 
class Node:
  object = {"manhata":int,"object":Object,"name":str}
  children = []
  distance = int
  id = int
  isUse = bool
  g = 1

  def __init__(self,object,id):
    self.object = object
    self.id = id
    self.children = []
    self.isUse = False