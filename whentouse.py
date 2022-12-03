# when to use classmethod and staticmethod ?
class item:
    @staticmethod
    def is_integer(num):
        '''
        this should do something that has a relationship with the class
    t not something that must be unique per instance!
        '''
    @classmethod
    def instantiate_from_csv(cls):
        '''
        this should do something that has a relationship with the class, but usually
        those are used to manipulate different structures of to instantiate 
        objects ,like we have done with CSV(comma seperated values)
        
        '''
# however , those could be also called from instances.
iten1 = item()
iten1.is_integer() #static method
iten1.instantiate_from_csv() #class method

#refer main.py for more info

