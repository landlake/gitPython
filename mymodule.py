import random

def divider(n):
    return [a for a in range(1, n+1) if not n%a]
def issosu(n):
    for i in range(2, n//2):
        if not n%i:
            return False
    return True
    
def sosuList(n):
    return [a for a in range(2, n+1) if issosu(a)]

def auler_pi(n):
    li=[]
    for i in range(1,n+1):
        li.append(1/i**2)
    return li

class myPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def dist(self, oP):
        return (((oP.x-self.x)**2)+((oP.y-self.y)**2))**0.5
    def setRandom(self):
        self.x = random.randrange(100)
        self.y = random.randrange(100)
    def __str__(self):
        return '['+str(self.x)+', '+str(self.y)+']'
    def printThis(self):
        self.name = 'myPoint'
        print(self.name, 'is member of myPoint class')

if __name__=='__main__':
    # print(__name__)
    # print(divider(10))
    # print(issosu(11))
    # print(sosuList(100))
    # for i in range(100):
    #     print('sosu :', (sum(auler_pi(i))*6)**0.5)
    # p = myPoint()
    # print(type(p))
    # print(dir(p))
    # p = myPoint()
    # myPoint.printThis(p)
    # p.printThis()
    # p.name = 'pppppp'
    # p.printThis()
    p = myPoint(3,4)
    origin = myPoint()
    print(p)
    print(origin)
    print(p.dist(origin))
    p.setRandom()
    print(p.dist(origin))