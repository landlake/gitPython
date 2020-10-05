def divider(n):
    return [a for a in range(1, n+1) if not n%a]
def issosu(n):
    for i in range(2, n//2):
        if not n%i:
            return False
    return True
    
def sosuList(n):
    return [a for a in range(2, n+1) if issosu(a)]

if __name__=='__main__':
    print(__name__)
    print(divider(10))
    print(issosu(11))
    print(sosuList(100))