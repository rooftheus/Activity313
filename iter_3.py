prices = {
    'chicken': 5.25,
    'beef': 6.25,
    'tofu': 5.75,
    'small': 1.00,
    'medium': 1.75,
    'large': 2.25,
    'small fries': 1.00,
    'medium fries': 1.50,
    'large fries': 2.00
}

final_price = 0

user_input = input(
    "Would you like a Chicken ($5.25), Beef ($6.25), or Tofu sandwich ($5.75)?\n"
).lower()

while True:
  if user_input != "chicken" and user_input != "beef" and user_input != "tofu":
    print("Please enter a valid sandwich type (chicken, beef, or tofu).\n")
    user_input = input(
        "Would you like a Chicken, Beef, or Tofu sandwich?\n").lower()
  else:
    break

print(f'This is the sandwich you ordered: {user_input.upper()} SANDWICH\n')

user_beverage = input(
    'Would you like a beverage? Answer with a yes or no\n').lower()
while True:
  if user_beverage != "yes" and user_beverage != "no":
    user_beverage = input('Answer with a yes or no\n').lower()
  else:
    break

if user_beverage == 'yes':
  bev_size = input(
      'What size beverage would you like? Small ($1.00), Medium ($1.75), or Large ($2.25)\n'
  )
  while True:
    if bev_size != "small" and bev_size != "medium" and bev_size != "large":
      bev_size = input('Choose between small, medium, and large\n')
    else:
      break
  print(f'This is the size of your beverage: {bev_size.upper()}\n')
else:
  bev_size = None
  print('You did not order a beverage')

user_fries = input(
    'Would you like fries? Answer with a yes or no. Any answer other than a no or yes will automatically add large fries to your order. \n'
).lower()

if user_fries == 'yes':
  fries_size = input(
      'What size fries would you like? Anser with small fries for small, medium fries for medium, and large fries for large. Any other answer assumes that you want large fries.\n'
  ).lower()
  if fries_size != "small fries" and fries_size != "medium fries":
    fries_size = "large fries"
    print('We added large fries to your order.\n')
elif user_fries == 'no':
  fries_size = None
  print('You did not order fries.\n')
else:
  fries_size = 'large fries'
  print('We added large fries to your order.\n')

if fries_size == 'small fries':
  mega_size = input(
      'Would you like to mega-size your fries? Answer with a yes or no.\n'
  ).lower()
  if mega_size == 'yes':
    fries_size = 'large fries'
    print('We added large fries to your order.\n')
  elif mega_size == 'no':
    print('You did not order to mega-size your fries.\n')
  else:
    print('We will keep your order the same\n')

if fries_size is not None:
  print(f'This is the size of your fries: {fries_size.upper()}\n')
print(f'This is the total price so far: {final_price}')
