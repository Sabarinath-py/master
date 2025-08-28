vehical_number = int(input("enter number"))

last_digit = vehical_number % 10

print(last_digit > 5 and last_digit%2==0
      )