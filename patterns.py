def pattern1(rows):
    for r in range(rows):
        for c in range(rows):
            print("*", end=" ")
        print("\r")


def pattern2(rows):
    for r in range(rows):
        for c in range(r+1):
            print("*", end=" ")
        print("\r")


def pattern3(rows):
    for r in range(rows):
        for c in range(rows - r):
            print("*", end=" ")
        print("\r")


def pattern4(rows):
    for r in range(1, rows+1):
        for c in range(1, r+1):
            print(c, end=" ")
        print("\r")


def pattern5(rows):
    for r in range(rows*2):
        # (if_test_false,if_test_true)[test]
        colRange = (r, (rows*2 - r))[r > rows]
        for c in range(colRange):
            print("*", end=" ")
        print("\r")

def pattern6(rows):
    for r in range(rows):        
        for c in range(rows):
            printItem = ("*"," ") [(rows-1 - r) > c]
            print(printItem, end=" ")
        print("\r")

def pattern7(rows):
    for r in range(rows):        
        for c in range(rows):
            printItem = ("*"," ") [c < r]
            print(printItem, end=" ")
        print("\r")

def pattern8(rows):
    for r in range(rows):
        for c in range(rows * 2 -1):
            printItem = ("*"," ") [(rows-1 - r) > c or ]
            print(printItem, end=" ")
        print("\r")
         
pattern8(5)
