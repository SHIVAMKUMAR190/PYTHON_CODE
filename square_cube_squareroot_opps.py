class calculator:
    
    def __init__(self,num):
        
        self.num = num
        
    def calculation(self):
        square = self.num * self.num  
        cube = self.num * self.num * self.num 
        root = self.num**0.5
        print(f"area of square is = {square}\ncube is = {cube} \nroot is = {root}")
            
num = int(input("enter your number = "))

obj = calculator(num)
obj.calculation()