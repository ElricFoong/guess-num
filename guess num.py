import random
r = random.randint(1, 100)
while True:
    num = input("guess number ")
    num = int(num)
    if num == r:
        print(" Thats right ")
        break
    elif num < r:
        
        print(" larger number ")
    elif num > r:
        
        print(" smaller number ")
