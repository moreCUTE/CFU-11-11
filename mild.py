import random
candy = [0, 0, 0, 0, 0, 0]

def TrickOrTreat():
    nomnom = random.randrange(0, 100)
    candynum = random.randrange(0, 5)
    
    if nomnom < 15:
        print("u gots", candynum, "Butterfingers")
    elif nomnom < 35:
        print("u gotd", candynum, "Hershey")
    elif nomnom < 70:
        print("you got", candynum, "Peanutbutter cups")
    elif nomnom < 80:
        print("youi have gotten", candynum, "M&M's")
    elif nomnom < 98:
        print("you have recieved", candynum, "Sour pathch kifsd")
    return candynum
    
    
    
for i in range(5):
    candy[i] = TrickOrTreat()
    
print("final candy count for each kid:", candy)
