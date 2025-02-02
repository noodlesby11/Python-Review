"""
****
****
****
"""
for i in range(1,4):
    for j in range(1,5):
        print("*",end="")
    print()
"""
*
**
***
****
*****
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""
*****
****
***
**
*
"""
for i in range(1,6):
    for j in range(1,7-i):
        print("*",end="")
    print()
"""
   *
  ***
 *****
*******
"""
for i in range(1,5):
    for j in range(1,5-i):
        print(" ", end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""
for i in range(1,5):
    for j in range(1,5-i):
        print(" ", end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
for i in range(1,4):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,8-2*i):
        print("*",end="")
    print()