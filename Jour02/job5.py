
for value in range(1, 101):
    if value < 3 : 
      print(value)
    elif value == 3 :
         print("Fizz")
    elif value == 5 :
           print(f"Buzz")
    elif value % 3 == 0 and value % 5 == 0 :
           print("BuzzFizz") 
    elif value % 3 == 0 :
           print("Fizz")
    elif value % 5 == 0 :
            print("Buzz")
    else : 
        print(value)
        