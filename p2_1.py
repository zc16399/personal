# p2_1.py
"""---第一个小游戏"""
import random

secret  =   random.randint(1,10)
temp    =   input("不妨猜一下Archer现在心里想的是哪个数字：")
guess   =   int(temp)

while  guess   !=   secret:
    temp    =   input("哎呀，猜错了，请重新输入另一个数字吧：")
    guess   =   int(temp)
    if guess    >    secret:
        print("哥，大了大了~~~")
    elif guess    <    secret:
        print("嘿，小了小了~~~")
    elif  guess   ==   secret:
        print("你是Atcher心里的蛔虫么？！")
        print("猜中了!")
print("哼,没有奖励！")
print("游戏结束，不玩啦^_^")
