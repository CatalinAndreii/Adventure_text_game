player = input("Hello there! What is your name?: ")

print(f"Nice to meet you {player}. I'm a wizard from the Bapteni forest and i need your help")

answer = input("Do you help me?").lower().strip()

if answer == "yes":
    print(f"Thanks {player}, you are a brave man!")
    print("Ok now I want you to go in the Cave of Shadows. There is my brother and my magic stick.")
    print("But, be careful, because is guarded by royal guards.")
    answer = input(f"What weapon do you need {player}? I have a sword, a bow and an axe").lower().strip()
    if answer == "sword":
        print("Excellent choice, for that I will also give you a shield ")
        print("Now you are ready for this, lets go")
        ...
    elif answer == "bow":
        print("oh! You want to fight from distance, intelligent!")
        print("Now you are ready for this, lets go")
        ...
    elif answer == "axe":
        print("With this one, no one can beat you. But, be careful because is a little heavy compared to the sword and bow")
        print("Now you are ready for this, lets go")
        ...
    else:
        print("I dont have this weapon, sorry bye!")
else:
    print(f"Ok {player} bye!")

