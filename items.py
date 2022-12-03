import csv
class  item:
    pay_rate = 0.6 #the pay rate after 20% discount

    all = []
    def __init__(self,name:str,price:float,quantity=0):
    # Run validations to received arguments 
        assert price >= 0, f"price{price} is noy greater than or equal to zero!"
        assert quantity >= 0, f"quantity{quantity} is not greater than or equal to zero!"
    #Assign to self object
        self._name = name
        self.price = price
        self.quantity = quantity
#action to execute
        item.all.append(self)

        @property 
        # read only attribute
        def name(self):
            return self._name
        @name.setter
        def name(self , value):
            self._name =   value

    def apply_discount(self):
        self.price = self.price * item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for itemi in items:
            item(
                name = itemi.get('name'),
                price = float(itemi.get('price')),
                quantity = int(itemi.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zer
        if isinstance(num,float):
            #if its a decimel
            return num.is_integer()
        elif isinstance(num , int):
            return True
        else:
            return False
    # another magic method to access all instances
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"



""" 
print(item.is_integer(7.88))
item.instantiate_from_csv()
print(item.all)
print(item.all)
    def calculate_price(self):
        return self.price * self.quantity
item1 = item('daniel', 500,7)
item2 = item("jackson",1000,9)
print(item2.calculate_price()) """
"""
print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
also
you can make new attritbutes always
like 

item2.lame = False

also
print("class or objectname".__dict__) works in a way that returns ll the methods in the class or method asked for
"""
""" 

item1.apply_discount()
print(item1.price)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
to access every name or price or quantity
for instance in item.all:
    print(instance.name) """

