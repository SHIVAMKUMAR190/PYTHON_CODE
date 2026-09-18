import random

user_input = input("enter your choice (snake, water, gun) : ").lower()


choice = {
    "snake": "snake",
    "water": "water",
    "gun": "gun"
}

computer_input = random.choice(["snake", "water", "gun"])

snake = "snake"
water = "water"
gun = "gun"

print(f"your choice : {user_input}")
print(f"computer choice : {computer_input}")

if (computer_input == snake and user_input == water):
    print("computer win")

elif (computer_input == water and user_input == gun):
    print("computer win")

elif (computer_input == gun and user_input == snake):
    print("computer win")

elif (computer_input == snake and user_input == gun):
    print("you win")

elif (computer_input == water and user_input == snake):
    print("you win")

elif (computer_input == gun and user_input == water): 
    print("you win")

elif (computer_input == snake and user_input == snake):
    print("draw")

elif (computer_input == water and user_input == water):
    print("draw")

elif (computer_input == gun and user_input == gun): 
    print("draw")

else: 
    print("Invalid input")