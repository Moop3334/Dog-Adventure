import time
#gets the 'time' directory for me to use

global loop
loop = 0

global ore
ore = 0

global sword
sword = 0

#defines the 'lose' function
def lose():
    print ("UH OH, YOU LOST")
    #UH OH, STINKY
    time.sleep(0.5)
    print ()
    print("To quit type 0, to try agian type 1")
    print ()
    time.sleep(0.5)
    ext = int(input(""))     
    if ext == 0:
        print ("Thanks for playing!")
        time.sleep(1)
        quit ()
    #Tells the game to stop if you inputed 0
        
    else:
        sword = 0
        loop = 0
        ore = 0
        return(loop)
    #restarts the game
    

def win():
    print ("YOU'RE A WIN!!!")
    print ()
    print ("CONGLATURATIONS!!!")
    #Intended spellings   
    print ()
    print ("...")
    time.sleep(2)  
    print ()
    time.sleep(0.5)
    print ()
    time.sleep(0.5)
    print ("Thank you for playing Doggo Quest!")
    #victory message
    time.sleep(0.5)
    print ()    
    print ("Made by u/Moop3334")
    #go follow me on Reddit
    
    print("To quit type 0, to play again type 1")
    print ()
    ext = int(input(""))
    if ext == 0:
        quit ()
    #ends the game
        
    else:
        sword = 0
        loop = 0
        ore = 0
        return(loop)
    #restarts the game


print ("Welcome to Doggo Quest 2.0!")
time.sleep(0.5)
print("Game made by u/Moop3334.")
time.sleep(0.5)
print('Orignally made during the end of 2019 for a school project. Remake finished on the 17th of Febuary, 2021.')
time.sleep(0.5)
print ()
print ("In this game you are a Dog heading off in search of adventure, treats, and head pats.")
time.sleep(0.5)
print ()
print ("You are in a meadow. After sniffing everything to check for snacks, you take a look at your surroundings. ")
time.sleep(0.5)
print ()

while loop == 0:
    print ("There is a gate to the north(1.), A desert to the west(2.), and a forest to the east(3.)")
    time.sleep(0.5)
    print ()
    Start = int(input("Which direction do you go? (1=North 2=West 3=East 4=South) "))
    time.sleep(0.5)
    print ()
    if Start == 4:
        print ("As soon as you take one step South your life Bluescreens and Existence.exe crashes. You lose.")
        lose()
        
    elif Start == 1:
        print ("As you approach you see a wolf guarding the gate. He looks strong.")
        time.sleep(0.5)
        print ()
        wc1 = int(input("Do you go back(0) or try and fight the wolf(1)? "))
        time.sleep(0.5)
        print ()
        if wc1 == 1:
            if sword == 1:
                print ("You use your cool sword to slay the wolf.")
                time.sleep(0.5)
                print ()
                print ("You go through the Gate.")
                time.sleep(0.5)
                print ()
                print ("You enter a room with all the treats you could ever want.")
                time.sleep(0.5)
                print ()
                win()
            else:
                print ("You get mauled by the wolf. You die.")
                time.sleep(0.5)
                print ()
                lose()
                
    elif Start == 2:
        print ("After trecking through the desert, You come across an Old Western town.")
        time.sleep(0.5)
        print ()
        wloop = 0
        while wloop < 2:
            print ("You see the Saloon(1), and the Blacksmith(2) are open.")
            time.sleep(0.5)
            print ()
            wc2 = int(input("Do you go to the Saloon or the Blacksmith? (Saloon=1 Blacksmith=2) "))
            time.sleep(0.5)
            print ()
            if wc2 == 1:
                print ("You trot into the Saloon. It seems to be a pretty old buiding, lots of creaking floorboards and cobwebs.")
                time.sleep(0.5)
                print ()
                print ("There are a few tables and chairs scatterd around, some with one or two legs missing.")
                time.sleep(0.5)
                print ()
                print ("You can't see anyone except for the bartender, who's at the bar scratching his ear.")
                time.sleep(0.5)
                print ()
                print ("You walk up to the bar and sit.")
                time.sleep(0.5)
                print ()
                print ("'Woof Bork?'")
                time.sleep(0.5)
                print ()
                print ("He inquirs if you'd want anything to drink.")
                time.sleep(0.5)
                print ()
                drunk = int(input("Do you order a drink?(Yes=1/No=0) "))
                time.sleep(0.5)
                print ()
                if drunk == 1:
                    print ("He pours you a bowl of whisky.")
                    time.sleep(0.5)
                    print ()
                    print ("You drink the whiskey.")
                    time.sleep(0.5)
                    print ()
                    print ("The alcohol is very strong.")
                    time.sleep(0.5)
                    print ()
                    print ("It's so strong your vision immediately blurs.")
                    time.sleep(0.5)
                    print ()
                    print ("You pass out.")
                    time.sleep(0.5)
                    print ()
                    print ("Later you die from alcohol posining!")
                    time.sleep(0.5)
                    print ()
                    print ("Don't drink too much.")
                    time.sleep(0.5)
                    print ()
                    lose()
                else:
                    print ("The bartender talks to you about what happend to the town.")
                    time.sleep(0.5)
                    print ()
                    print ("Bark woof.")
                    time.sleep(0.5)
                    print ("Bark woof, woof woof bark. Barkwoof.")
                    time.sleep(0.5)
                    print ("Bark woof woof.")
                    time.sleep(0.5)
                    print ()
                    print ("You undestand that you're the first person to come through here in a while.")
                    time.sleep(0.5)
                    print ()
                    print ("The town's recently been ransacked by a Wolf from the North, driving most people away.")
                    time.sleep(0.5)
                    print ()
                    print ("You know you'll need a weapon to face the Wolf.")
                    time.sleep(0.5)
                    print ()
                    wloop = (wloop+1)
            elif wc2 == 2:
                print ("You walk into the Blacksmith.")
                time.sleep(0.5)
                print ()
                print ("The room you walk into is small and dark, the only ligh coming from the fire, blazing in the forge.")
                time.sleep(0.5)
                print ()
                print ("By the door you see a pile of coals and some smithing tools.")
                time.sleep(0.5)
                print ()
                print ("There's a counter by the right wall, on the opposite side of the room to the forge.")
                time.sleep(0.5)
                print ()
                print ("You can barely make out the shape of an anvil and dousing bowl scatterd near the forge.")
                time.sleep(0.5)
                print ()
                print ("You see a figure working the forge, who you think is the blacksmith.")
                time.sleep(0.5)
                print ()
                print ("There is a bell on the counter, you ring it, hoping to get the figures attention.")
                time.sleep(0.5)
                print ()
                print ("He takes a white hot object out of the forge and dunking it in the dousing bowl sitting beside the forge.")
                time.sleep(0.5)
                print ()
                print ("He then trodds over to the counter, lifting his cracked, dark smithing goggles.")
                time.sleep(0.5)
                print ()
                if ore == 0:
                    print ("Woof bark.")
                    time.sleep(0.5)
                    print ("Woof woof bark.")
                    time.sleep(0.5)
                    print ("Bark bark woof.")
                    time.sleep(0.5)
                    print ("Woof bark.")
                    time.sleep(0.5)
                    print ()
                    print ("You can gather from this that he was in the middle of making the hilt of a sword but has run out of ore, so he can't make the blade.")
                    time.sleep(0.5)
                    print ()
                    print ("He says that he was recently ransacked by a Wolf, which is why he doesn't have that much.")
                    time.sleep(0.5)
                    print ()
                    print ("He also says that you should head to the tavern to learn more about that Wolf.")
                    time.sleep(0.5)
                    print ()
                    print ("He said if you want the sword you'll need to get him more ore which you can find to the east.")
                    time.sleep(0.5)
                    print ()
                    print ("You ask about payment, but he says that won't be necessary, saying the ore is payment enough.")
                    time.sleep(0.5)
                    print ()
                    wloop = (wloop+1)
                elif ore == 1:
                    print ("You drop the ore in front of the blacksmith.")
                    time.sleep(0.5)
                    print ()
                    print ("He picks it up and starts working the metal into shape.")
                    time.sleep(0.5)
                    print ()
                    print ("After many hours of back-breaking work he returns to you, dropping his creation on the counter.")
                    time.sleep(0.5)
                    print ()
                    print ("!!YOU OBTAINED THE COOL SWORD!!")
                    time.sleep(0.5)
                    print ()
                    sword = (sword+1)
                    wloop = (wloop+2)
        print ("You decide to head back to the meadow, seeing nothing else to do.")
        time.sleep(0.5)
        print ()
    elif Start == 3:
        print ("You walk alnog the forest's path.")
        time.sleep(0.5)
        print ()
        print ("It's supprisingly quiet as you walk.")
        time.sleep(0.5)
        print ()
        print("The tree canopy blocks more and more sunlight as you walk deeper and deeper into the forest.")
        time.sleep(0.5)
        print ()
        print ("You come across a set of stone doors with ornate engravings imbeded into the side of a small hill.")
        time.sleep(0.5)
        print ()
        false = int(input("Do you open the doors? (Yes=1/No=0) "))
        print ()
        time.sleep(0.5)
        if false == 0:
            print ("Just as you were about to leave the doors open on their own.")
            time.sleep(0.5)
            print ()
            print ("You decide that this is a sign and you should probably go through the doors.")
            time.sleep(0.5)
            print ()
        print ("Beyond the doors is a long set of stone stairs.")
        time.sleep(0.5)
        print ()
        print ("The person who built this must have really liked stone because the walls and celing are also mage of stone.")
        time.sleep(0.5)
        print ()
        print ("You also note they bear the same ornate engravings as the door.")
        time.sleep(0.5)
        print ()
        print ("You decend down the staircase.")
        time.sleep(0.5)
        print ()
        print ("The staircase isn't lit, but your natural good-boy aura illuminates the way.")
        time.sleep(0.5)
        print ()
        print ("After walking for what feels like hours, you finally see a light at the bottom of the staircase.")
        time.sleep(0.5)
        print ()
        print ("As you reach the bottom you enter into a large cavern.")
        time.sleep(0.5)
        print ()
        print ("On the walls you see torches blazing in steel brackets.")
        time.sleep(0.5)
        print ()
        print ("In Front of you you see three hallways.")
        time.sleep(0.5)
        print ()
        print ("There's an intense glow coming from the left hallway, like something really shiny is reflecting light.(1)")
        time.sleep(0.5)
        print ()
        print ("You hear a metallic clancking, like metal slamming aginst stone, coming from the middle hallway.(2)")
        time.sleep(0.5)
        print ()
        print ("The right hallway is quiet, almost too quiet...(3)")
        time.sleep(0.5)
        print ()
        hall = int(input("Do you go down the left, right, or the middle hallway? (left=1/middle=2/right=3) "))
        print ()
        time.sleep(0.5)
        if hall == 1:
            print ("It turns out what you thought was gold was, in fact, A blazing wall of fire!")
            time.sleep(0.5)
            print ()
            print ("You get incinerated. You die.")
            time.sleep(0.5)
            print ()
            lose()
        if hall == 2:
            print ("You enter the hallway.")
            time.sleep(0.5)
            print ()
            print ("There's small holes all over the walls and celing.")
            time.sleep(0.5)
            print ()
            print ("You hear the clanking sound again.")
            time.sleep(0.5)
            print ()
            print ("Spears shoot out of the holes and impale you.")
            time.sleep(0.5)
            print ()
            print ("You die.")
            time.sleep(0.5)
            print ()
            lose()
        if hall == 3:
            print ("You walk down the right corridor.")
            time.sleep(0.5)
            print ()
            print ("You notice small deposits of Cool Ore scattering the walls and ceiling of the hallway.")
            time.sleep(0.5)
            print ()
            print ("The farther you go in the hallway the bigger and more numerous the deposits seem to get.")
            time.sleep(0.5)
            print ()
            if ore == 1:
                print ("It appears you already got the ore.")
                time.sleep(0.5)
                print ()
                
            else:
                print ("Once you reach the end of the hallway you find a large block of Cool Ore.")
                time.sleep(0.5)
                print ()
                print ("You dig out the ore from the block.")
                time.sleep(0.5)
                print ()
                print ("!!YOU OBTAINED 'COOL ORE'!!")
                time.sleep(0.5)
                print ()
                ore = (ore+1)
            print ("You decide to head back to the meadow.")
            time.sleep(0.5)
            print ()
