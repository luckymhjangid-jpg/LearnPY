# try:
#     print(x)
#     print(str)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("something went wrong")

# try:
#     a=10
#     b=0
#     c= a/b
# except:
#     print("Cannot be zero")


# #mulitple exception
# try:
#     num = int(input("Enter a number:"))
#     print(100/num)
# except ZeroDivisionError:
#     print("Division by zero")
# except ValueError:
#     print("Invalid Input")


# # use of finally 
balance = 10000
try:
    print("Processing Transaction")
    amount = int(input("Enter amount5"))

    if amount > 1000:
         print("Transaction Approved")     if amount > balance:
         raise Exception("Amount must be positive")
    balance -= amount
    print("Remaining balance",balance)

except Exception as e:
     print(e)
finally:
     print("Thakyou")

 #one block for mulitple exceptions
try:
      num = int(input("Enter the number:"))
      result = 100/num
     
except (ValueError , ZeroDivisionError):
    print("Invalid Operation")

else:
      print(result)
#exception object
try:
     a = 10
     b=0
     c=a/b

except ZeroDivisionError as e:
     print("Zero division error")


