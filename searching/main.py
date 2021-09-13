from table import Table
from object.obstacle import Obstacle
from object.package import Package
from object.forklift import Forklift
from star import Star
if __name__ == "__main__":
  table = Table(4,4)
  
  package1 = Package()
  package2 = Package()
  package3 = Package()
  
  forklift = Forklift()

  table.addObject(0,0, package1)
  table.addObject(3,0, package2)
  table.addObject(1,0, Obstacle())
  table.addObject(1,1, Obstacle())
  table.addObject(0,2, package3)
  table.addObject(2,2, forklift)
  table.printTable()


  print("get first package")
  x_0, y_0 = forklift.getCurrentPoint()
  x_1, y_1 = package1.getCurrentPoint()
  star = Star(table)
  star.setPointToStart(x_0,y_0)
  star.setPointToFinish(x_1,y_1)
  x_0, y_0 = star.start()

  star.showCloseList()
  
  print("left fist package")
  x_1, y_1 = 3,3

  star2 = Star(table)
  star2.setPointToStart(x_0,y_0)
  star2.setPointToFinish(x_1,y_1)
  x_0, y_0 = star2.start()

  star.showCloseList()
  
  print("get second package")

  
  x_1, y_1 = package2.getCurrentPoint()

  star3 = Star(table)
  star3.setPointToStart(x_0,y_0)
  star3.setPointToFinish(x_1,y_1)
  x_0, y_0 = star3.start()

  star.showCloseList()
  print("left second package")
  
  x_1, y_1 = 3,2

  star4 = Star(table)
  star4.setPointToStart(x_0,y_0)
  star4.setPointToFinish(x_1,y_1)
  x_0, y_0 = star4.start()
  star.showCloseList()
  print("get third package")
  x_1, y_1 = package3.getCurrentPoint()

  star5 = Star(table)
  star5.setPointToStart(x_0,y_0)
  star5.setPointToFinish(x_1,y_1)
  x_0, y_0 = star5.start()
  star.showCloseList()
  print("left third package")
  
  x_1, y_1 = 1,3

  star6 = Star(table)
  star6.setPointToStart(x_0,y_0)
  star6.setPointToFinish(x_1,y_1)

  x_0, y_0 = star6.start()