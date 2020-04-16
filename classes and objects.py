import os.path
import sys
import copy



def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
        print(msg)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)

class SMS_store:
    def __init__(self, cellphone_number):
        self.cell = str(cellphone_number)
        if not os.path.isfile("SMS_store{0}.txt".format( self.cell )):
            SMS = open("SMS_store{0}.txt".format( self.cell ),"w")
            SMS.close()

    def add_new_arrival(self, from_number , time_arrived , text_of_SMS ):
        read = open ("SMS_store{0}.txt".format( self.cell ))
        stored = read.readlines()
        has_been_viewed = False
        new_SMS = (str(has_been_viewed) +"|"+ str(from_number) +"|"+ str(time_arrived) +"|"+ text_of_SMS + "\n")
        stored.append(new_SMS)
        write = open("SMS_store{0}.txt".format( self.cell ), "w")
        for i in stored:
            if i == "\n":
                continue
            else:
                write.write(i)
        write.close()

        
    def message_count(self):
        read = open("SMS_store{0}.txt".format( self.cell ))
        all_SMS = read.readlines()
        read.close()
        count = 0
        for i in all_SMS:
            count += 1
        return count

    def get_unread_indexes(self):
        reading = open("SMS_store{0}.txt".format( self.cell ))
        all_SMS = reading.readlines()
        reading.close()
        unread_indexes = []
        for i in range(len(all_SMS)):
            text = all_SMS[i].split("|")
            if text[0] == "False":
                unread_indexes.append(i)
        return unread_indexes


    def get_message(self, index):
        reading = open("SMS_store{0}.txt".format( self.cell ))
        all_SMS = reading.readlines()
        reading.close()
        if index > len(all_SMS):
            return None
        message = all_SMS[index]
        messagelist = message.split("|")
        if messagelist[0] == "False":
            messagelist[0] = "True"
            message_att = "|".join(messagelist)
            all_SMS[index] = message_att
            writing = open ("SMS_store{0}.txt".format( self.cell ), "w" )
            for i in all_SMS:
                writing.write(i)
            writing.close()
        return messagelist[1:]


    def delete(self,index):
        reading = open("SMS_store{0}.txt".format( self.cell ))
        all_SMS = reading.readlines()
        reading.close()
        if index > len(all_SMS):
            return None
        del all_SMS[index]
        writing = open("SMS_store{0}.txt".format( self.cell ), "w")
        print(all_SMS)
        for SMS in all_SMS:
            writing.write(SMS)
        writing.close()
            

    def clear(self):
        SMS = open("SMS_store{0}.txt".format( self.cell ),"w")
        SMS.write("")
        SMS.close()
        
        
        
class Point:
    """Point Class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        
    def distance_origin(self):
        return ((self.x ** 2) + (self.y **2)) ** 0.5

    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def halfway(self, target):
        "return teh halfway point between myself and the target"
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)


    def reflect_x(self):
        return Point(self.x * -1, self.y)

    def slope_origin(self):
        if self.x == 0:
            return "undefined"
        return self.y/self.x
    
    def get_line_to(self , point):
        if self.x - point.x == 0:
            return self.x
        m = ( self.y - point.y ) / ( self.x - point.x )
        c = self.y - self.x * m
        return Point( m , c )
    
    def tuple(self):
        return (self.x,self.y)

    def list(self):
        return [self.x , self.y]
        
    
class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner,self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2* self.width + 2* self.height

    def flip(self):
        return Rectangle(self.corner,self.height,self.width)

    def contains(self,point):
        print(point)
        centralize = 0
        pointlist = point.list() 
        if self.corner.x < 0:
            centralize = int(self.corner.x)
            self.corner.x = self.corner.x - centralize
            pointlist[0] += abs(centralize)
        if self.corner.y < 0:
            centralize = int(self.corner.y)
            self.corner.y = self.corner.y - centralize
            pointlist[1] += abs(centralize)
        print(self.corner.y, pointlist[0], pointlist[1])
        if pointlist[0] < 0 or pointlist[1] < 0:
            return False
        if pointlist[0] >= self.corner.x + self.width or pointlist[1] >= self.corner.y + self.height:
            return False
        else:
            return True

    def collision(self,other):
        
        selfv1 = Point(self.corner.x, self.corner.y)
        selfv2 = Point(self.corner.x + self.width , self.corner.y)
        selfv3 = Point(self.corner.x , self.corner.y + self.height)
        selfv4 = Point(self.corner.x + self.width , self.corner.y + self.height)
        
        listaselfv = []
        
        listaselfv.append(selfv1.list())
        listaselfv.append(selfv2.list())
        listaselfv.append(selfv3.list())
        listaselfv.append(selfv4.list())

        
        otherv1 = Point(other.corner.x, other.corner.y)
        otherv2 = Point(other.corner.x + other.width , other.corner.y)
        otherv3 = Point(other.corner.x , other.corner.y + other.height)
        otherv4 = Point(other.corner.x + other.width , other.corner.y + other.height) 

        listaotherv = []

        listaotherv.append(otherv1.list())
        listaotherv.append(otherv2.list())
        listaotherv.append(otherv3.list())
        listaotherv.append(otherv4.list())

        for i in listaselfv:
            if other.contains(Point(i[0], i[1])):
                return True
        for j in listaotherv:
            if self.contains(Point(j[0],j[1])):
                return True
        else:
            return False



r = Rectangle(Point(0, 0), 10, 5)
s = Rectangle(Point(-15, -20), 10, 5)

print(r.collision(s))


def distante(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

def circle_center(point1, point2, point3):
    center = Point()
    d = 2 * (point1.x * (point2.x - point3.y) + point2.x * (point3.y - point1.y) + point3.x * (point1.y - point2.y))
    center.x = ((point1.x ** 2 + point1.y ** 2) * (point2.y - point3.y) + (point2.x ** 2 + point2.y ** 2) * (point3.y - point1.y) + (point3.x ** 2 + point3.y ** 2) * (point1.y - point2.y)) / d
    center.y = ((point1.x ** 2 + point1.y ** 2) * (point3.x - point2.x) + (point2.x ** 2 + point2.y ** 2) * (point1.x - point3.x) + (point3.x ** 2 + point3.y ** 2) * (point2.x - point1.x)) / d
    return center

