

#bring in necessary imports
import sys 
sys.path.append('C:\Workspace\CE 599\ce599-s17\18-Design and Classes')
from Car import Car


if __name__ == "__main__":
    print('First Car')
    Car = Car(color = 'yellow',location = [0,0],direction = 'N')
    Car.printcar()
    Car.go(2,'forward')
    Car.turn_left()
    Car.go(1,'forward')
    print( '\n' + 'After Movements')
    Car.printcar()
    
#reset the Car object
    from Car import Car 
    print('\n' + '\n' + 'Second Car')    
    Car2 = Car(color = 'green',location = [0,0], direction = 'N')
    
    Car2.printcar()
    Car2.turn_left()
    Car2.go(1,'forward')
    Car2.turn_right()
    Car2.go(2,'forward')
    print( '\n'  + 'After Movements')
    Car2.printcar()
    