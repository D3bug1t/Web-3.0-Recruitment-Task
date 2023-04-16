class Car:
    def _init_(self, make, model, year, speed_x, speed_y, x=0, y=0, size=10):
        self.make = make
        self.model = model
        self.year = year
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        self.size = size

    def accelerate_x(self, speed_inc):
        self.speed_x += speed_inc

    def accelerate_y(self, speed_inc):
        self.speed_y += speed_inc

    def brake_x(self, speed_dec):
        self.speed_x -= speed_dec

    def brake_y(self, speed_dec):
        self.speed_y -= speed_dec

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def detection(self, obj2):
        return ((abs(self.x-obj2.x)-(self.size + obj2.size)//2)<=0 and(abs(self.y-obj2.y)-(self.size + obj2.size)//2)<=0)

    def time_before_collision(self, obj2):
        x_collision_initial = (self.x-obj2.x - (self.size +obj2.size)/2)/(obj2.speed_x-self.speed_x)
        x_collision_final = (self.x-obj2.x + (self.size +obj2.size)/2)/(obj2.speed_x-self.speed_x)
        x_collision_initial = min(x_collision_initial, x_collision_final),
        x_collision_final= max(x_collision_initial, x_collision_final)
        y_collision_initial = (self.y-obj2.y - (self.size +obj2.size)/2)/(obj2.speed_y-self.speed_y)
        y_collision_final = (self.y-obj2.y + (self.size+obj2.size) / 2)/(obj2.speed_y-self.speed_y)
        if (x_collision_final) < 0: return -1
        if (x_collision_initial< 0):x_collision_initial = 0
        y_collision_initial = min(y_collision_initial, y_collision_final),
        x_collision_final= max(y_collision_initial, y_collision_final)
        if (x_collision_final < 0):return -1
        if( x_collision_initial< 0):x_collision_initial = 0
        y_collision_initial = min(y_collision_initial, y_collision_final),
        y_collision_final= max(y_collision_initial, y_collision_final)
        if y_collision_final < 0:return -1
        if y_collision_initial < 0:y_collision_initial = 0
        if (y_collision_final <= x_collision_initial and x_collision_initial<= y_collision_final): 
            return x_collision_initial
        if (x_collision_initial <= y_collision_initial and y_collision_initial<= x_collision_final):
            return y_collision_final
        return -1
