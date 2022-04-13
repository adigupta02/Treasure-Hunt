def snake_room():
    print("\nThere is a snake here.")
    print("Behind the Snake is another door.")
    print("The snake is having egg!")
    print("What would you do? (1 or 2)")
    print("1). Take the eggs.")
    print("2). Taunt the snake.")
    

def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another room. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")
    

def treasure_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")
    

def game_over(reason):
    print("\n"+reason)
    print("Game Over!")

def lets_play_again():
    print("\nDo you want to play again? (y or n)")
    answer=input(">").lower()
    if(answer=="y"):
        print()
        start()
    else:
        exit()


def start():
    print("You are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r)")
    inp_start=input(">").lower()
    if(inp_start=="l"):
        snake_room()
        inp_snake=input(">")
        if(inp_snake=="2"):
            treasure_room()
            inp_treasure=input(">")
            if(inp_treasure=="1"):
                print("Yay!! You won!")
            else:
                game_over("You didnt chose diamonds")
                lets_play_again()
        else:
            game_over("You want eggs not the treasure !! Thats why the snake killed you")
            lets_play_again()

    else:
        monster_room()
        inp_monster=input(">")
        if(inp_monster=="1"):
            treasure_room()
            inp_treasure=input(">")
            if(inp_treasure=="1"):
                print("Yay!! You won!")
            else:
                game_over()
                lets_play_again()
        else:
            game_over("The monster was hungry, he/it ate you")
            lets_play_again()


start()
