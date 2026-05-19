while True:
    try:
         x = int(input("what is x? "))
         print(100 / x)
         break
    except ValueError:
         print("Error: That's not a number")
    except ZeroDivisionError:
         print("Error: Cannot divide by zero")