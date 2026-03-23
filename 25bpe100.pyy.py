import random
def set3 ():
    lst = [random.randrange (-5, 5)for x in range (15)]
    print (lst)
    uniqlst = list (set(lst))
    print (uniqlst)
set3 ()
    
