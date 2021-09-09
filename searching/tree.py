from table import Table
from object.object import Object

class Tree:
  table = Table
  x_0 = int
  x_1 = int
  y_0 = int
  y_1 = int
  
  def __init__(self,table):
    self.table = table

  def start():
    pass

  def setPointToStart(self,x,y):
    self.x_0 = x
    self.y_0 = y

  def setPointToFinish(self,x,y):
    self.x_1 = x
    self.y_1 = y