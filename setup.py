def hello():
    print("Hello")

def pack(a, b, c):
    newList = [a, b, c]
    print(newList)

def eat_lunch(lunchList):
    if lunchList:
        print("First I eat", lunchList[0])
        if len(lunchList) > 1:
            i = 1
            while i < len(lunchList):
                print("Next I eat", lunchList[i])
                i += 1
    return None

hello()
pack(1, 2, 3)
eat_lunch(["a hamburger", "fries", "cheese cake"])