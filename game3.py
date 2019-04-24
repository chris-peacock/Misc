from game1 import *
from time import sleep

def engagement(shealth,swep,sarm,bwep,barm,sactor,bactor):
    stevestat = stat(shealth, 10, sactor, False)
    bobstat = stat(10, 10, bactor, False)
    steveequip = equipstat(swep, sarm)
    bobequip = equipstat(bwep, barm)
    while (stevestat[0]>0 and bobstat[0]>0):
        stat(stevestat[0], 10, sactor, True)
        stat(bobstat[0], 10, bactor, True)
        steveroll = roll(*steveequip, sactor, False)
        bobroll = roll(*bobequip, bactor, False)

        if steveroll[0] > bobroll[0]:
            print(stevestat[2] + ' beat ' + bobstat[2] + ' with ' + item(swep))
            if (steveroll[0]-bobroll[0] - bobequip[3]) > 0:
                bobstat[0] -= (steveroll[0]-bobroll[0] - bobequip[3])
            else:
                print(bobstat[2] + 's ' + item(barm) + ' defends!')
            sleep(2)
        elif steveroll[0] < bobroll[0]:
            print(bobstat[2] + ' beat ' + stevestat[2] + ' with ' + item(bwep))
            if (bobroll[0]-steveroll[0] - steveequip[3]) > 0:
                stevestat[0] -= (bobroll[0]-steveroll[0] - steveequip[3])
            else:
                print(stevestat[2] + 's ' + item(sarm) + ' defends!')
            sleep(2)
        else:
            print('tie!')
            sleep(2)

    if stevestat[0]<= 0:
        print(bobstat[2] + ' wins!')
    elif bobstat[0]<= 0:
        print(stevestat[2] + ' wins!')

#print('Chris')
#sequip = equip(5, 15)
#print('Prison Guard')
#bequip = equip(2, 17)
#engagement(10, *sequip, *bequip, 'You', 'Prison Guard')