from table import Table
from object.obstacle import Obstacle
from object.package import Package
from object.forklift import Forklift
from tree import Tree
if __name__ == "__main__":
  table = Table(4,4)
  
  package = Package()
  forklift = Forklift()

  table.addObject(2,2, Obstacle())
  table.addObject(2,1, Obstacle())
  table.addObject(0,0, package)
  table.addObject(2,3, forklift)

  x_0, y_0 = forklift.getCurrentPoint()
  x_1, y_1 = package.getCurrentPoint()

  tree = Tree(table)

  tree.setPointToStart(x_0,y_0)
  tree.setPointToFinish(x_1,y_1)

  
  

  


  