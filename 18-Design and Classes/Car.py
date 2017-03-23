#constansts
START_NORTH = 0
START_SOUTH = 0
START_EAST = 0
START_WEST = 0
# Define the class
class Car(object):
    
    """
    Base class for a car
    """
    def __init__(self, color,location = [0,0],direction = 'N'):
        if len(location) < 2 or len(location) > 2:
            print('location is the x,y coordinates of the car')
        else:    
            self.color = color
            self.location = location
            self.x = location[0] 
            self.y = location[1]
            self.direction = direction
    
    def go(self,units,movement):
        """
        function to move the car the given distance in the given direction
        """
        if movement == 'forward':
        
            if self.direction == 'N':
                self.y = self.y + units
            elif self.direction == 'S':
                self.y = self.y - units
            elif self.direction == 'E':
                self.x = self.x + units
            elif self.direction == 'W':
                self.x = self.x - units
            else:
                print('Direction options are N, S, E, and W')
            self.location = [self.x,self.y]   
        elif movement == 'backward':
            if self.direction == 'N':
                self.y = self.y - units
            elif self.direction == 'S':
                self.y = self.y + units
            elif self.direction == 'E':
                self.x = self.x - units
            elif self.direction == 'W':
                self.x = self.x + units
            else:
                print('Direction options are N, S, E, and W')
            self.location = [self.x,self.y]   
  
        else:
            print('Possible movements are forward and backward')
        
    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'
        else:
            print('direction is wrong')
            
    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'
        else:
            print('direction is wrong')
            
    def printcar(self):
        print('Car Color is ' + self.color)
        print('Car Location is ')
        print(self.location)
        print('Car Direction is ' + self.direction)
            