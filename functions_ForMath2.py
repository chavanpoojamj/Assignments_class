def math(num1, num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    div = num1/num2
    return add, sub, mul, div


number1 = int(input("Enter 1st number:"))
number2 = int(input("Enter 2nd number:"))

# result1,result2,result3,result4=math(number1,number2)
# print(result1,result2,result3,result4)

result1 = math(number1, number2)
print(result1)

