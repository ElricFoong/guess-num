import random
start = input(" Start number ")
end = input(" End number ")
start = int(start)
end = int(end)

r = random.randint(start, end)
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
