#Calculates Ontario Tax On Purchases
while True:
    try:
        Before_Tax = float(input("Please Enter Cost: "))
    except ValueError:
        Before_Tax = float(input("Please Enter an integer only! "))
    else:
        Tax_Before_Addition = round(Before_Tax * 0.13,2)
        Total_After_Tax = round(Tax_Before_Addition + Before_Tax,2)
        print("Your Total after tax is", Total_After_Tax, "Tax added was", Tax_Before_Addition,)