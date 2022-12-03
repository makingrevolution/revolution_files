'''
instructions
------------
>input your current age
>input the current year
>input the year u want to check your current age
>get back your age in that year

FOR THAT :-
> make a funtion that process the your difference
between current year and the year we need
add the number with current age 
return the number 
'''
def difference(curage,curyear,exyear):
    diff = exyear - curyear
    if curage + diff < 0:
        return 0
    return curage+diff
curage = int(input("current age: "))
curyear = int(input("current year:  "))
exyear = int(input("expected year: "))
goblin = difference(curage,curyear,exyear)
print("your age will be: ", goblin)
