def pattern1(rows):
  for r in range(rows):
    for c in range(rows):
      print("*", end=" ")
    print("\r")
   
def pattern2(rows):
 for r in range(rows):
   for c in range(r+1):    
    print("*" , end=" ")
   print("\r")  

def pattern3(rows):
 for r in range(rows):
   for c in range(rows - r):    
    print("*" , end=" ")
   print("\r")

def pattern4(rows):
  for r in range(1,rows+1):
    for c in range(1,r+1):
      print(c, end=" ")
    print("\r")

def pattern5(rows):
  for r in range(rows*2):
    # (if_test_false,if_test_true)[test]
    colRange = (r, (rows*2 - r)) [ r > rows ]
    for c in range(colRange):
      print("*", end=" ")
    print("\r")

def pattern6(rows):
  for r in range(rows):
   print("*", end=" ")

pattern1(5)


