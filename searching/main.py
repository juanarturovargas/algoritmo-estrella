from table import Table
from object.obstacle import Obstacle
from object.package import Package
from object.forklift import Forklift
from star import Star
if __name__ == "__main__":
  table = Table(4,4)
  
  package = Package()
  forklift = Forklift()

  table.addObject(2,0, Obstacle())
  table.addObject(1,0, Obstacle())
  table.addObject(3,3, package)
  table.addObject(0,0, forklift)
  table.printTable()
  x_0, y_0 = forklift.getCurrentPoint()
  x_1, y_1 = package.getCurrentPoint()


  star = Star(table)

  star.setPointToStart(x_0,y_0)
  star.setPointToFinish(x_1,y_1)

  star.start()
  

  


  