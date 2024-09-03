from math import *

print("HELLO!!!!! WELCOME TO PYCAL-PYTHON BASED CALCULATOR", sep="\n")
print(" developed by TEJAS SINGH ARORA , XII B",  sep="\n")
print("KV Sector 8 , RK Puram , New Delhi", sep="\n")
print("This is a calculator having  all basic functions", " Please select an option from the given below list to continue", sep="\n")


print("1. Addition","2. Subtraction","3. Multiplication","4. Division","5. e to the power *num*","6. *num1* to the power *num2*","7. square of *num*","8. cube of *num*","9. 10 to the power *num*","10. inverse of *num*","11. square root of *num*","12. cube root of *num*","13. natural logarithm of *num*","14. logarithm *num1* with base *num2*","15. factorial of *num*", sep="\n")
print("16. sine value of *num* i.e sin(*num*)","17. cosine value of *num* i.e cos(*num*)","18. tangent value of *num* i.e tan(*num*)","19. cosecant value of *num* i.e cosec(*num*)","20. secant value of *num* i.e sec(*num*)","21. cotangent value of *num* i.e cot(*num*)","22. smallest integer greater than or equal to *num*","23. Absolute value of *num*","24. greatest integer less than or equal to *num*","25. Euclidean norm i.e √((num1)*2+(num2)*2))", sep="\n")

ans='y'


while ans == 'y':
    number = int(input("Which function do you wish to perform ? (Enter it's number.) :  "))


    if number == 1:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        print("Your answer is : ", num1 + num2)
        ans = input("Want to continue ? : ")


    elif number == 2:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        print("Your answer is : ", num1 - num2)
        ans = input("Want to continue ? : ")


    elif number == 3:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        print("Your answer is : ", num1 * num2)
        ans = input("Want to continue ? : ")


    elif number == 4:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        print("Your answer is : ", num1 / num2)
        ans = input("Want to continue ? : ")


    elif number == 5:
        num = float(input("Enter number : "))
        print("Your answer is : ", e ** num)
        ans = input("Want to continue ? : ")


    elif number == 6:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        print("Your answer is : ", num1 ** num2)
        ans = input("Want to continue ? : ")


    elif number == 7:
        num = float(input("Enter number : "))
        print("Your answer is : ", num1 ** 2)
        ans = input("Want to continue ? : ")


    elif number == 8:
        num = float(input("Enter number : "))
        print("Your answer is : ", num1 ** 3)
        ans = input("Want to continue ? : ")


    elif number == 9:
        num = float(input("Enter number : "))
        print("Your answer is : ", 10 ** num)
        ans = input("Want to continue ? : ")


    elif number == 10:
        num = float(input("Enter number : "))
        print("Your answer is : ", 1 / num)
        ans = input("Want to continue ? : ")


    elif number == 11:
        num = float(input("Enter number : "))
        print("Your answer is : ", num ** 1/2)
        ans = input("Want to continue ? : ")


    elif number == 12:
        num = float(input("Enter number : "))
        print("Your answer is : ", num ** 1/3)
        ans = input("Want to continue ? : ")


    elif number == 13:
        num = float(input("Enter number : "))
        print("Your answer is : ", log(num))
        ans = input("Want to continue ? : ")


    elif number == 14:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        print("Your answer is : ", log(num1,num2))
        ans = input("Want to continue ? : ")


    elif number == 15:
        num = int(input("Enter number : "))
        print("Your answer is : ", factorial(num))
        ans = input("Want to continue ? : ")


    elif number == 16:
        num = float(input("Enter the angle(in degrees) : "))
        print("Your answer is : ", sin(radians(num)))
        ans = input("Want to continue ? : ")


    elif number == 17:
        num = float(input("Enter the angle(in degrees) : "))
        print("Your answer is : ",cos(radians(num)))
        ans = input("Want to continue ? : ")


    elif number == 18:
        num = float(input("Enter the angle(in degrees) : "))
        print("Your answer is : ", tan(radians(num)))
        ans = input("Want to continue ? : ")


    elif number == 19:
        num = float(input("Enter the angle(in degrees) : "))
        print("Your answer is : ", 1/sin(radians(num)))
        ans = input("Want to continue ? : ")


    elif number == 20:
        num = float(input("Enter the angle(in degrees) : "))
        print("Your answer is : ", 1/cos(radians(num)))
        ans = input("Want to continue ? : ")


    elif number == 21:
        num = float(input("Enter the angle(in degrees) : "))
        print("Your answer is : ", 1/tan(radians(num)))
        ans = input("Want to continue ? : ")


    elif number == 22:
        num = float(input("Enter number :  "))
        print("Your answer is : ", ceil(num))
        ans = input("Want to continue ? : ")


    elif number == 23:
        num = float(input("Enter number :  "))
        print("Your answer is : ", fabs(num))
        ans = input("Want to continue ? : ")


    elif number == 24:
        num = float(input("Enter number :  "))
        print("Your answer is : ", floor(num))
        ans = input("Want to continue ? : ")


    elif number == 25:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        print("Your answer is : ", hypot(num1,num2))
        ans = input("Want to continue ? : ")


    else:
        print("Invalid choice !!!. (Choose from the given options only.)")
        continue

    if ans.lower() == 'y' or ans.lower() == 'yes':
        ans = 'y'













print("THANK YOU !!! ", sep="\n")
print("BYE - BYE", sep="\n")
print("SEE YOU SOON :)")


