a = int(input("enter number : "))



tens_place = (a // 10) % 10
ones_place = a%10
hundred_place = a//100



print("tens_place of a number : ",tens_place)
print("ones_place of a number : ",ones_place)
print("hundred_place of a number : ",hundred_place)