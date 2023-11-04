# Anas Jamil (668659)
# 2020-10-06
# A shopping program for computer parts.Given the quantity the prorgram provides subtotal, tax charged, and total after tax. Given 10 items to choose from.
print("Welcome to AJ's Computer Shop, what would you like to purchase?")
print(" ")
print("Please enter the quantity of each item between the range of 1 and 5.")
print(" ")
CPU1 = float(input("AMD Ryzen 5 3600XT, $340.00: "))
CPU2 = float(input("Intel Core I7 9700K, $430.00: "))
GPU1 = float(input("MSI Radeon RX 5600 XT 6GB GDDR6, $400.00: "))
GPU2 = float(input("GIGABYTE GeForce RTX 2060 WINDFORCE OC, $439.99: "))
PCB1 = float(input("ASUS ROG STRIX B450-F GAMING Socket AM4, $179.99: "))
PCB2 = float(input("ASUS Prime Z390-P LGA1151, $189.99: "))
RAM1 = float(input("Corsair Vengeance RAM LPX 16GB !SALE! ,NOW $94.99 was $104.99: "))
RAM2 = float(input("G.SKILL Ripjaws V Series 32GB 2x16GB DDR4 3000MHz C15, $179.99: "))
SSD1 = float(input("WD Blue™ 3D NAND SATA SSD, 500GB, $79.99: "))
HDD1 = float(input("Seagate BarraCuda 2TB SATA 3.5 HDD, $74.99: "))
Quantity1 = 340.00 * CPU1
Quantity2 = 430.00 * CPU2
Quantity3 = 400.00 * GPU1
Quantity4 = 439.99 * GPU2
Quantity5 = 179.99 * PCB1
Quantity6 = 189.99 * PCB2
Quantity7 = 94.99 * RAM1
Quantity8 = 179.99 * RAM2
Quantity9 = 79.99 * SSD1
Quantity10 = 74.99 * HDD1
Subtotal = round(Quantity1 + Quantity2 + Quantity3 + Quantity4 + Quantity5 + Quantity6 + Quantity7 + Quantity8 + Quantity9 + Quantity10, 2)
print(" ")
print("This is your subtotal: $",Subtotal)
Tax = round(Subtotal * 0.17,2)
print(" ")
print ("This is how much tax you are being charged: $",Tax)
Total = round(Tax + Subtotal,2)
print(" ")
print("Your total is $",Total)
print(" ")
Payment = str(input("How would you like to pay, Cash, visa or Debit? "))           
print(" ")
print("This is your recipt")
print(" ")
print("Thanks For Shopping With Us!")
print("2020-10-06")
print("Payment VIA",Payment)
print("Subtotal: $",Subtotal)
print("Tax Charged: $",Tax)
print("Total: $",Total)
print("Farewell!, Come Again Soon!")