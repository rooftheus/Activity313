user_input = input("Would you like a Chicken, Beef, or Tofu sandwich?\n").lower()

while True:
  if user_input != "chicken" and user_input != "beef" and user_input != "tofu":
    print("Please enter a valid sandwich type (chicken, beef, or tofu).\n")
    user_input = input("Would you like a Chicken, Beef, or Tofu sandwich?\n").lower()
  else:
    break
    
print(f'This is the sandwich you ordered: {user_input.upper()} SANDWICH')




    
