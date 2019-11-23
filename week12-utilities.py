# Audrey Bradford
# ​CSCI 102 – Section F
# Week 12 - Part A

################################################
########   Function 1 : PrintOutput    #########
################################################

def PrintOutput(x):
    print("OUTPUT", x)

################################################
########   Function 2 : LoadFile       #########
################################################

def LoadFile(x):
    lines = open(x, "r")
    listedboi = lines.splitlines()
    return (listedboi)

################################################
########   Function 3 : UpdateString   #########
################################################

def UpdateString(x,y,z):
    updated = ''
    original = list(x)
    original.pop(z)
    original.insert(3, y)
    for i in original:
        updated += i
    return (updated)

################################################
########   Function 4 : FindWordCount  #########
################################################

def FindWordCount(x,y):
    times = 0
    for i in x:
        if i == y:
            times += 1
    return times

################################################
########   Function 5 : ScoreFinder    #########
################################################

def ScoreFinder(x,y,z):
    scorespot = -1
    playerscore = ''
    for i in x:
        if i.lower() == z.lower():
            scorespot = x.index(i)
    if scorespot == -1:
        return ('player not found')
    else:
        playerscore = str(x[scorespot]) + ' got a score of ' + str(y[scorespot])
        return (playerscore)

################################################
########   Function 6 : Union          #########
################################################
    
def Union(x,y):
    list1 = list(x) + list(y)
    for i in list1:
        if list1.count(i) > 1:
            list1.pop(list1.index(i))
    return list1
