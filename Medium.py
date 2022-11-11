class FRIDGE:
    def __init__(self, items, door, running):
        self.items = 0
        self.door = False
        self.running = True
        
    def prnt(self, x):
        if x == 'a':
            print("fridge door is", self.dooropen)
            print("you have", self.items, " items in fridege")
            print("ur fridge is", self.running)
            if self.running == True:
                print("ur fridge rinnung lmaoooooo, better go cath ittttttt")
        if x == 'q':
            print("There are,", self.items, " items in the fridge")
        if x == 'r':
            print("Fridge Open is:", self.dooropen)
        if x == 'x':
            print("The Fridge running is:", self.running)
            if self.isRunning == True:
                print("Haha your fridge is running, better go catch it!")
          
                
    def dooropen(self):
        self.door = True
        
    def doorcose(self):
        self.door = False
    
    def fridgeitems(self, x):
        if self.dooropen == True:
            self.items += x
        else:
            print("what?")
            
    def dinner(self):
        self.items -= 10
        
print()
fridge = FRIDGE(0, False, True)

fridge.prnt('a')
print()
fridge.dooropen()
fridge.prnt('r')

f = int(input("how many intems u want in FRIDGE????"))
fridge.fill(f)
fridge.prnt('i')
choice = input("u trynna make dinner??")
if choice == "yes":
    fridge.dinner()
else:
    print("ight then")
    
print("Now", end = ' ')
fridge.prnt('i')

p = input("close the fridge door?")
if p == "yes":
    fridge.doorcose()
else:
    fridge.doorcose()

fridge.prnt('d')
