costprice = int(input("enter the cp: "))
sellingprice = int(input("enter the sp: "))

if (sellingprice > costprice):
    print("There is a profit")
    profit = sellingprice - costprice
    print(profit)
else:
    print("No profit")