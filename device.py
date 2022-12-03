from items import item
class device(item):
    def __init__(self, name: str, price: float, quantity=0,broken = 0):
        #call the super  function to have access to all attribute / methods
        super().__init__(name, price, quantity)
        assert broken >= 0 , f"broken{broken} is not greater than 0"
        #assign to self object
        self.broken = broken
device1 = device("dell inspiron", 40000, 6)
"""

 print(device1.apply_discount())
print(device1.price)
print(item.all)
print(device.all)
"""