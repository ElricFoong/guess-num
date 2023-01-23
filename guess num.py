import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input("guess number ")
    num = int(num)
    if num == r:
        print(" Thats right ")
        print("this is your count ", count, "times")
        break
    elif num < r:
        
        print(" larger number ")
    elif num > r:
        
        print(" smaller number ")
    print("this is your count ", count, "times")
