main_coins = 0
coins = 0
main_coins = int(input())

coins = main_coins

##print("Player One")
##first = int(input("1: Pick Coins: "))
##coins = coins - first
###print(coins)
##
##first = int(input("2: Pick Coins: "))
##coins = coins - first
###print(coins)
names = ["Alice","Bob"]
values = []
for one in range(2):
##    print(names[one])
    first = int(input())
    coins = coins - first
    values.append(first)
print(values)
    
while True:
    coins = coins - first**2
##    print(coins)

    if(coins <= 0):
##        print(coins)
        print("Alice")
        break
##    print(coins)
    print("Bob")





