class car:
    def __init__(self,color,price,km):
        self.color=color
        self.price=price
        self.km=km
    def __gt__(self,other):
        if(self.price>other.price):
            return True
        else:
            return False
    def __add__(self,other):
        return self.km+other.km
car1=car("blue",1200000,400)
car2=car("red",1500000,600)
print("first car\ncolor:",car1.color,"\nprice:",car2.price,"\nkilometers:",car1.km)
print("second car\ncolor:",car2.color,"\nprice:",car2.price,"\nkilometers:",car2.km)
sum=car1.km+car2.km
print("sum of kilometers:",sum)
if(car1.price>car2.price):
    print("car1 is more expensive")
else:
    print("car2 is more expensive")
        
        
