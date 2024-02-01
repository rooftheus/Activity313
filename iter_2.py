prices = {'chicken': 5.25, 'beef': 6.25, 'tofu': 5.75, 'small': 1.00, 'medium': 1.75, 'large': 2.25}

user_input = input("Would you like a Chicken ($5.25), Beef ($6.25), or Tofu sandwich ($5.75)?\n").lower()

while True:
  if user_input != "chicken" and user_input != "beef" and user_input != "tofu":
    print("Please enter a valid sandwich type (chicken, beef, or tofu).\n")
    user_input = input("Would you like a Chicken, Beef, or Tofu sandwich?\n").lower()
  else:
    break
    
print(f'This is the sandwich you ordered: {user_input.upper()} SANDWICH\n')

user_beverage = input('Would you like a beverage? Answer with a yes or no\n').lower()
while True:
  if user_beverage != "yes" and user_beverage != "no":
    user_beverage = input('Answer with a yes or no\n').lower()
  else:
    break

if user_beverage == 'yes': 
  bev_size = input('What size beverage would you like? Small ($1.00), Medium ($1.75), or Large ($2.25)\n') 
  while True:
    if bev_size != "small" and bev_size != "medium" and bev_size != "large":
      bev_size = input('Choose between small, medium, and large\n')
    else:
      break
  print(f'This is the size of your beverage: {bev_size.upper()}\n')
else: 
  print('You did not order a beverage')

middle_price = 0
for key, value in prices.items():
  if key == user_input or key == user_beverage:
    middle_price += value
  else:
    continue
print(f'This is the total price so far: {middle_price}')






    
