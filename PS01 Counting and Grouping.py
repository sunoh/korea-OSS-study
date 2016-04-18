

def item_order(order):
    numSalad = 0
    numHamburger = 0
    numWater = 0
    list_order = order.split()
    for item in list_order:
        if item == 'salad':
            numSalad += 1
        elif item == 'hamburger':
            numHamburger += 1
        elif item == 'water':
            numWater += 1 
    print "salad:" + str(numSalad) + " hamburger:" + str(numHamburger) + \
    " water:" + str(numWater)
       
            
    