vida = 100
for i in range(100,-1,-10):
    
    if (i < 100 and i > 0):
        #print("|."+"█."*(i//10)+"_."*((100-i)//10)+"|"+" - ",i,"%")
        print("|{}{}| - {}%".format("█"*(i//10), "_"*((100-i)//10), i))

    if(i == 100):
        #print("|."+"█."*10+"|"+" - ",i,"%")
        print("|{}| - {}%".format("█"*10, i))

    if(i == 0):
        #print("|."+"_."*10+"|"+" - ",i,"%")
        print("|{}| - {}%".format("_"*10, i))
        break