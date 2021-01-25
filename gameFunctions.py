import ast
import random



def addPlayer(name):
    with open('players.txt', 'r') as f:
        data = f.read()
        upd = ast.literal_eval(data)
        upd[name] = 50
        with open('players.txt', 'w') as f:
            f.write(str(upd)+'\n')

def addPoints(name, amount):
    with open('players.txt', 'r') as f:
        data = f.read()
        upd = ast.literal_eval(data)
        upd[name] += amount
        with open('players.txt', 'w') as f:
            f.write(str(upd))

def removePoints(name, amount):
    with open('players.txt', 'r') as f:
        data = f.read()
        upd = ast.literal_eval(data)
        upd[name] -= amount
        with open('players.txt', 'w') as f:
            f.write(str(upd))

def checkBalance(name):
    with open('players.txt', 'r') as f:
        data = f.read()
        upd = ast.literal_eval(data)
        return 'Your balance is: '+ str(upd[name])
        
def isEqual(playerPick):
    side = ['h','t']
    coinFlip = random.choice(side)
    return playerPick == coinFlip

def isNewPlayer(name):
    with open('players.txt', 'r') as f: #opens players file to check if player already exists
        data = f.read()
        upd = ast.literal_eval(data)
        return name not in upd

def enoughBalance(name, amount):
    with open('players.txt', 'r') as f: 
        data = f.read()
        upd = ast.literal_eval(data)
        if int(upd[name]) >= amount:
            return True
        else:
            return False
