def choice(a,b,c,d,e,f,loc,enemy,enemtype):
    print('1. Look around')
    print('2. Look for loot')
    print('3. Inventory')
    if enemy ==True:
        print('4. Attack')
    else:
        print('4. Use item')
    while True
        i = input('What would you like to do?')
        if i == 1:
            locmess(loc)
        elif i == 2:
            locloot(loc)
        elif i == 3:
            inventory(a,b,c,d,e,f)
        elif i == 4:
            if enemy == True:
                engagement(enemtype)
            else:
