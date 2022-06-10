#0,1,1,2,3,5,8,13,21.....

def fibonacci():
    x,y=0,1
    while True:
        yield x      #0,1,1,2,3,5,8
        x,y=y,x+y

for x in fibonacci():
    if x>10000:
        break
    print(x,end=' ')