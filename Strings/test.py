def substring_in_order(s1, s2):
    for char in s2:
        if char in s1:
            idx = s1.find(char)
            s1 = s1[idx:]
        else: 
            return False
        return True
substring_in_order("CALCULATOR", "CART")
    print ("Bye")
else:
    print("Hi")