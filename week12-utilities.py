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
