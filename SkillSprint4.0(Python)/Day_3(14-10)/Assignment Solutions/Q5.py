
def simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

p = int (input("Enter the Principal Amount"))
r = int (input("Enter the Rate"))
t = int (input("Enter the Time"))
s=simple_interest(p,r,t)
print(s)