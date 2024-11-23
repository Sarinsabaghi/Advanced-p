#jojo dar khatar

def main():
    num=vorodi_input()
    x,y=loc_x_y(num)
    print(x,y)

def loc_x_y(num):
    x,y=0,0
    if num % 4 ==0:
        x,y=-num//4, num//4
    if num % 4 ==1:
        x,y=-(num-1)//4,-(num-1)//4
    if num % 4 ==2:
        x,y=(num+2)//4,(num-2)//4
    if num % 4 ==3:
        x,y=(num+1)//4,(num+1)//4
    return x,y

def vorodi_input():
    num=input()
    num=int(num)
    return num