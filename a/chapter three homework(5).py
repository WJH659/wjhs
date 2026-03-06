num= 23
while True:
    a=int(input("输入你猜的数字:"))
    if a==-1:
        break
    else:
        if a<num:
            print("小了")
        elif a>num:
            print("大了")
        else:
            print("恭喜猜中")
            break