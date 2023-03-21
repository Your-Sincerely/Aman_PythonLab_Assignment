def add(add1, add2):
    return add1 + add2
def largest_num(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    elif y > x:
        if y > z:
            return y
        else:
            return z
def pos_neg(num):
    if num > 0:
        return "positive"
    else:
        return "negative"
def day(num):
    if 0 < num < 8:
        Dict = {1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
                }
        return Dict[num]
    else:
        return "Enter Value again"
num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))
num3 = int(input("Enter 3rd number :"))
one_to_seven = int(input("Enter number between 1 to 7 :"))

print("Addition of 2 number :", add(num1, num2))
print("Largest number is:", largest_num(num1, num2, num3))
print("positive negative number :", pos_neg(num1))
print("day today is :", day(one_to_seven))
