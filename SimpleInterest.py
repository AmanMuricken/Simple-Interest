#(ptr)/100
def simpleInterest(p,t,r):
    si=(p*t*r)/100
    print("The simpleInterest is:",si)
    return si
    


p=float(input("Enter the value for principle:"))
t=float(input("Enter the value for time:"))
r=float(input("Enter the value for rate:"))

simpleInterest(p,t,r)