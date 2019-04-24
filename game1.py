from random import randint
from time import sleep


def item(a):
    I = ['Empty',
         '1d04+0 Sharpened Keys ',
         '1d04+2 Stun Baton',
         '1d06+2 Kitchen Knife',
         '1d04+4 Metal Pipe',
         '1d08+2 Stun Pistol'
         '1d08+4 Stun Rifle',
         '2d08+2 Coil pistol',
         '2d08+4 Coil Rifle',
         '1d08+8 Vacuum Rifle',
         '2d06+8 Gladius',
         'bandage',
         'medpack',
         'snack',
         'meal',
         '+1 Prison Tats',
         '+0 Prison Uniform',
         '+2 Guard Uniform',
         '+0 Civilian Clothing',
         '+2 Armored Padding',
         '+3 Body Armor',
         '+4 Power Armor',
         '+1 Vacuum Suit']
    return I[a]



def stat(h,s,actor,P):
    H = '++++++++++'
    S = '!!!!!!!!!!'
    if P == True:
        print(actor)
        print('H: ' + H[:h])
        print('S: ' + S[:s])
    else:
        return [h, s, actor]

def roll(mult,die,add,defence,actor,P):
    r = ((mult*randint(1, die)) + add)
    if P == True:
        print(actor + ' rolls ' +str(r))
        return [r, defence]
    else:
        return [r, defence]

def locmess(loc):
    if loc == 1:
        print("""The cell is not much bigger than the hold of the ship that 
took you here; just large enough for your to stretch your legs 
and clear your head from the ceiling.  It encloses your with metal 
walls that have been scuffed so much you cannot make out your 
reflection in them.  In place of bars, 3 inches of solid metal.""")
    elif loc == 2:
        print("""The guards are presumably on their food break, the post is deserted.
The post itself is much like a longer version of the cell you just left, with
a few pieces of battered furnature and some protein synthesizers for the staff.
Somehow, you feel like you would rather spend your time in a cell than work out 
your life at this post.""")
    elif loc == 3:
        print("""The cafeteria is, surprisingly, empty for the first time since you've arrived.
It is not much different that the guard post, with it's uncomfortable- looking furnature 
and dull lighting.  Just like you remember, large gobs of grey protein cling to the
sides of tables and smear the ground.  Chairs are overturned and the place smells of 
nothing but recycled air.""")
# Takes in string of numbers, separates each number and feeds into item. Returns list of strings from item, based on input numbers
def inventory(a,b,c,d,e,f):
    print('1. ' + item(a))
    print('2. ' + item(b))
    print('3. ' + item(c))
    print('4. ' + item(d))
    print('5. ' + item(e))
    print('6. ' + item(f))

class Illegal(Exception):
    pass
class Disengage(Exception):
    pass

def additem(a,b,c,d,e,f,g):
    List = [a,b,c,d,e,f]
    inventory(a, b, c, d, e, f)
    p = input('Position to swap?')
    if int(p) < 7:
        pass
    else:
        raise Illegal
    choice = input('Swap ' + item(List[int(p) - 1]) + ' for ' + item(int(g)) + '? (Y/N)')
    if choice == 'Y':
        List[int(p) - 1] = int(g)
        inventory(*List)
        return List
    elif choice == 'N':
        inventory(*List)
    else:
        raise Illegal
# Checks whether input is ok from additem, then returns list of inventory items
def additemcheck(a,b,c,d,e,f,g):
    List = [a,b,c,d,e,f]
    while True:
        try:
            List = additem(*List, g)
            return List
        except Illegal:
            print('Invalid entry.  Enter again')
            continue
        except ValueError:
            print('Invalid entry.  Enter again')
            continue
        else:
            break

def dropitem(a, b, c, d, e, f):
    List = [a, b, c, d, e, f]
    inventory(a,b,c,d,e,f)
    drop = input('which item to drop (index)?')
    if int(drop) < 7:
        List[int(drop) - 1] = 0
        inventory(*List)
        return List
    else:
        raise Illegal
# Checks whether input is ok from dropitem, then returns list of inventory items    CALL THIS IN MAIN
def dropitemcheck(a,b,c,d,e,f):
    List = [a,b,c,d,e,f]
    while True:
        try:
            List = dropitem(*List)
            return List
        except Illegal:
            print('Invalid entry.  Enter again')
            continue
        except ValueError:
            print('Invalid entry.  Enter again')
            continue

def useitem(a, b, c, d, e, f, h, s):
    h = int(h)
    s = int(s)
    stat(h, s, 'Current stats: ', True)
    List = [a, b, c, d, e, f]
    inventory(a, b, c, d, e, f)
    use = int(input('which item to use (index)?'))
    if (0< int(use) < 7 and (int(List[use -1]) == 11 or int(List[use -1]) == 12 or int(List[use -1]) == 13 or int(List[use -1]) == 14)):
        if int(List[use -1]) == 11:
            if h <= 7:
                h += 3
            else:
                h = 10
        elif int(List[use -1]) == 12:
            if h <= 4:
                h += 6
            else:
                h = 10
        elif int(List[use -1]) == 13:
            if s <= 7:
                s += 3
            else:
                s = 10
        elif int(List[use -1]) == 14:
            if s <= 4:
                s += 6
            else:
                s = 10
        List[int(use) - 1] = 0
        inventory(*List)
        stat(h, s, 'New stats: ', True)
        return [*List, h, s]
    else:
        raise Illegal
# Checks whether input is ok from dropitem, then returns list of inventory items    CALL THIS IN MAIN
def useitemcheck(a,b,c,d,e,f,h,s):
    List = [a,b,c,d,e,f]
    while True:
        try:
            List = useitem(*List, h, s)
            return [*List]
        except Illegal:
            print(' Cannot be used, or Invalid entry.  Enter again')
            continue
        except ValueError:
            print('Invalid entry.  Enter again')
            continue

# Returns and prints the weapon/apparel and related stats, to call in the 'roll' function
def equip(wep,arm):
    print('Weapon: ' + item(wep))
    print('Apparel: ' + item(arm))
    return [wep, arm]
# Returns mult, dieroll, addition, defence
def equipstat(wep,arm):
    return [int(item(wep)[0]), int(item(wep)[3]), int(item(wep)[5]), int(item(arm)[1])]

def engagement(shealth,bhealth,sstam,bstam,swep,sarm,bwep,barm,sactor,bactor):
    stevestat = stat(shealth, sstam, sactor, False)
    bobstat = stat(bhealth, bstam, bactor, False)
    steveequip = equipstat(swep, sarm)
    bobequip = equipstat(bwep, barm)
    if (stevestat[0]>0 and bobstat[0]>0):
        stat(stevestat[0], stevestat[1], sactor, True)
        stat(bobstat[0], bobstat[1], bactor, True)
        steveroll = roll(*steveequip, sactor, False)
        bobroll = roll(*bobequip, bactor, False)
        ask = input('Continue ? (Enter)   Exertion? (e)')
        if ask == '':
            pass
        elif ask == 'e':
            addroll = input('Enter number of stamina points to spend: ')
            if int(addroll) <= int(stevestat[1]):
                steveroll[0] += int(addroll)
                stevestat[1] -= int(addroll)
            else:
                print('Overexterted!')
                stevestat[0] -= 1
                stevestat[1] = 0
                steveroll[0] += 1
        else:
            raise Illegal
        if steveroll[0] > bobroll[0]:
            print(stevestat[2] + ' beat ' + bobstat[2] + ' with ' + item(swep))
            if (steveroll[0]-bobroll[0] - bobequip[3]) > 0:
                bobstat[0] -= (steveroll[0]-bobroll[0] - bobequip[3])
            else:
                print(bobstat[2] + 's ' + item(barm) + ' defends!')
                bobstat[0] -= 1
            sleep(2)
        elif steveroll[0] < bobroll[0]:
            print(bobstat[2] + ' beat ' + stevestat[2] + ' with ' + item(bwep))
            if (bobroll[0]-steveroll[0] - steveequip[3]) > 0:
                stevestat[0] -= (bobroll[0]-steveroll[0] - steveequip[3])
            else:
                print(stevestat[2] + 's ' + item(sarm) + ' defends!')
                stevestat[0] -= 1
            sleep(2)
        else:
            print('tie!')
            sleep(2)

    elif stevestat[0]<= 0:
        print(bobstat[2] + ' wins!')
        raise Disengage
    elif bobstat[0]<= 0:
        print(stevestat[2] + ' wins!')
        raise Disengage
    return [stevestat[0], bobstat[0], stevestat[1], bobstat[1], swep,sarm,bwep,barm,stevestat[2], bobstat[2]]

def engagementcheck(shealth, sstam,swep,sarm,sactor, bhealth, bstam,bwep,barm,bactor):
    fightstat = [shealth, bhealth, sstam, bstam, swep, sarm, bwep, barm, sactor, bactor]
    print('*********COMBATANTS********')
    print(sactor)
    equip(swep,sarm)
    print(bactor)
    equip(bwep, barm)
    print('')
    print('***********FIGHT***********')
    print('Prepare yourself!')
    while True:
        try:
            newstat = engagement(*fightstat)
            fightstat = newstat
        except Illegal:
            print('Invalid entry.  Enter again')
            continue
        except ValueError:
            print('Invalid entry.  Enter again')
            continue
        except Disengage:
            print('The fight is over!')
            break
#Returns list of enemy health, stamina, weapon and aparrel
def enemytype(a):
    if a == 1:
        return [4,4,3,16, 'Prisoner']
    if a == 2:
        return [6,6,5,17, 'Prison Guard']
    if a == 3:
        return [8,8,2,20, 'City Guard']
    if a == 4:
        return [10,10,8,21, 'Power Soldier']

def choice(a,b,c,d,e,f,h,s,wep,arm, name,loc,enemycheck,etype):
    enemystat = enemytype(etype)
    while True:
        try:
            print('1. Look around')
            print('2. Look for loot')
            print('3. Inventory')
            print('4. Use Item')
            if enemycheck == True:
                print('5. Attack')
            else:
                pass
            i = int(input('What would you like to do?'))
            if i == 1:
                locmess(loc)
            elif i == 2:
                locloot(loc)
            elif i == 3:
                inventory(a,b,c,d,e,f)
            elif i == 4:
                [a, b, c, d, e, f, h, s] = useitemcheck(a,b,c,d,e,f,h,s)
            elif i == 5:
                if enemycheck == True:
                    engagementcheck(h,s, wep, arm, name, *enemystat)
                else:
                    print('No Enemy to attack')
            else:
                raise Illegal
        except Illegal:
            print('Invalid entry.  Enter again')
            continue
        except ValueError:
            print('Invalid entry.  Enter again')
            continue

