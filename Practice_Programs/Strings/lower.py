s1 = input("Enter a string: ").lower()
s1 += " "
s2 = input("Enter another string: ").lower()
current = ""
longest = ""
for count in range(len(s1)):
    if s1[count] in s2:
        current += s1[count]
    else:
        if len(current)>len(longest):
            longest = current
            current = ""
        elif len(current)==len(longest):
            longest += ", "
            longest += current
print(longest)