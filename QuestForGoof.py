#set up
import time
import random

locationa = ["forest","town","shop","hall of goof","factory","gooflandea square"]
abilities = ["sneaky hat", "magic glasses","detectives drum","nothing"]
guessing_game_num = 0
log_corect = 0
has_been_in_goofs_house = False

def find_goof_piece():
    if found_goof_piece:
        print()
        print(random.choice(["you saw a goof piece and got it", "a goof piece fell on you head and you got it ", "there was a goof piece on the floor and you got it"]))
        print()
        pieces_of_goof += 1


find_goof_piece

location_suc = False
last = ""

pieces_of_goof = 0

def ez (number):
    time.sleep(number)

did_you_leave = "N/A"

goof = "N/A"
ez(1)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------")#start
print("  _______                    _______     _________     _________             _______     ______    _____              _____     ______    ______   _____")
print(" /       \    |       |      |           |                 |                 |          |     |    |   |             |     |   |     |   |     |  |")
print("|        |    |       |      |______     |_________        |                 |______    |     |    |___|             |         |     |   |     |  |_____")
print("|     \  |    |       |      |                    |        |                 |          |     |    | \               |   ___   |     |   |     |  |   ")
print(" \______\/     \_____/       |______      ________|        |                 |          |_____|    |   \             |_____|   |_____|   |_____|  |")
print("         \ ")
ez(3)
print("by ethan mettler")
ez(1)
print()
ez(1)
print()
ez(1)
print("login")
while log_corect != "yes".lower():
    name = input("what is your name: ")
    special_alib = input("choose one of these " + ", " .join(abilities)+": ").lower()
    while special_alib not in abilities:
        special_alib = input("try again, take something frome this list," + ", " .join(abilities)+": ")
    log_corect = input("is this correct, yes or no: ")
    print()
ez(1)
print("It's time to start your quest!")
ez(1)
print()
ez(1)
print()
ez(1)
print()
ez(3)
print("Your adventure starts when the GREAT AND ALL POWERFUL GOOF escapes the hall of goof!")
ez(4)
print("It is your job to go and catch goof to SAVE GOOFLANDEA!")
print()
ez(2)
print("good luck")
ez(1)
print()
print()
print()
print("Shopkeeper: But what is your name?!?!?!")
print()
ez(1)
print("Shopkeeper: It's",name,"right?")
print()
ez(1)
print("Shopkeeper: Go get goof," , name + "!")
print()
ez(1)
print("shopkeeper:Here take the goof catcher9000")
print()
ez(1)
print("[You got the goof catcher]")
print()
print("Shopkeeper:good luck", name + "!  and remember to find 5 goof pieces!! ")
ez(1)

##Loop until enough pieces are found
while pieces_of_goof < 5:
    ##Print choices of locations
    print()
    print("You can go to",', '.join(locationa))
    location_suc = False
    
    ##Loop until a valid location has been selected
    while location_suc == False  and has_been_in_goofs_house == False:

        location = input("where do you want to go?  ").lower()
        print()
        ## Checking to see if a valid location was chosen
        if location in [loc.lower()for loc in locationa]:

            ## Check if same location as last time
            if location == last:
                ez(1)
                print("Maybe try going somewhere else to look before coming back here")
                print()
            else:
                # Valid location, break loop
                location_suc = True
        else:
            if location == "goof's house":
                print("you found the secret location")
                ez(1)
                print("now take the goof pieces and leave before goof gets back")
                ez(1)
                print()
                pieces_of_goof = 5
                print("you have found",pieces_of_goof,"pieces of goof so far")
                print()
                has_been_in_goofs_house = True
                ez(1)
            else:
                ez(1)
                print("XD LOL THATS NOT A PLACE LOL XD")
                print()
                ez(1)
                print("try the " + random.choice(locationa))
                print()
    
    if has_been_in_goofs_house == False:
        ## Randomly find POG
        print("You went to ", location)
        last = location
        print()
        found_goof_piece = random.choice([True, False])           
            
        if found_goof_piece:
            print()
            print(random.choice(["You saw a goof piece and got it", "A goof piece fell on you head and you got it ", "There was a goof piece on the floor and you got it"]))
            print()
            pieces_of_goof += 1
        else:
            ##No POG, but second chance
            guessing_game_num = random.randint(1, 5)
            ez(1)
            print("you did not find a goof piece")
            ez(1)
            print("but then the goof challenges you to a guessing game")
            player_guess = input("Choose a number from one to five:")
            if int(player_guess)  == guessing_game_num:
                ez(1)
                print("you won, you got a piece of goof!")
                if special_alib == "detectives drum":
                    print("you hit your detectives drum")
                    ez(1)
                    print()
                    print("you figure out that you can go to goof's house")
                ez(1)
                print("you hear goof grumble")
                pieces_of_goof += 1
            else:
                ez(1)
                print("goof: YOU LOSE HEHE")
                print()
                ## Check for sneaky hat second chance
                if special_alib == "sneaky hat".lower():
                    ez(1)
                    print("goof:take another shot at it ")
                    player_guess = input("from one to five:")
                    if int(player_guess) == guessing_game_num:
                        ez(1)
                        print("you won, you got a piece goof!")
                        ez(1)
                        print("you hear goof grumbull")
                        pieces_of_goof += 1
                    else:
                        ez(1)
                        print("goof: YOU LOSE AGAIN HEHE")
        
        ##Check for special abilities
        if special_alib == "magic glasses".lower():
            ez(1)
            print("but you look again with your glasses")
            print()
            found_goof_piece = random.choice([True, False, False])
            if found_goof_piece:
                ez(1)
                print(random.choice(["you saw a goof piece and got it", "a goof piece fell on you head and you got it ", "there was a goof piece on the floor and you got it"]))
                print()
                pieces_of_goof += 1
            else:
                ez(1)
                print("but you saw nothing")
                print()

        ## Goof pieces score at the end of round
        if pieces_of_goof == 1:
            ez(1)
            ez(1)
            print("you have found",pieces_of_goof,"piece of goof so far")
        else:
            ez(1)
            ez(1)
            print("you have found",pieces_of_goof,"pieces of goof so far")
        print()
print("You put the goof pieces in the goof catcher9000 TM but it dosent work")#end
ez(3)
print("...so you SLAP IT")
ez(3)
print("and then it make the nose GIGGOOGAFFLLLOPLYSWOOSHBASHDONKWOMP")
ez(3)
print("Goof gets sucked in and is stuck in the goof catcher forever YIPPY")
ez(3)
print("\/     \  /\  / *")
ez(2)
print("|  O U  \/  \/  |  n")
ez(2)
print("for now")
print()
print("credits")
ez(2)
print()
print("Game coder and idea maker: Ethan Mettler")
ez(2)
print("Coding helper: chatGPT")
ez(2)
print("Playtester: Lynn Mettler NetEagle")
ez(1)
print("That's it, bye")
print()
print()