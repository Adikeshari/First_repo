print('hey i am working with git')
print('its my first code')
#pattern code
'''
*
**
***
****
*****
'''
num=int(input())+1
for i in range(num):
    for j in range(i):
        print('*',end='')
    print()

#second pattern
num=int(input())
for i in range(num,1,-1):
    print('*'*i)
print("*")
    
    
    
