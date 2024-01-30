#---------------------Exercise Automatic tiller-------------------------------
#Input of console is the money that I want get


Money= int(input("Enter the money you want to withdraw, please: "))
Coins_10= Money // 10
Money= Money % 10


Coins_5= Money // 5
Money= Money % 5


Coins_1= Money // 1
Money= Money % 1


print("Amount of 10 coins: " , Coins_10)
print("Amount of 5 coins: ", Coins_5)
print("Amount of 1 Coin: ", Coins_1)

   
