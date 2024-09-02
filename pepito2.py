from pepito import Weapon,NPC,Player,Enemy
import random
import time

def timer(func):
    def wrapper():
        func()

notnamed = True

scythe = Weapon("Strife","Scythe","Medium",9)
hammer = Weapon("JetHell","Hammer","Huge",9)
Glaive = Weapon("Journey Below","Glaive","Medium",11)
Holy_Sword = Weapon("Tears of Memory","Sword","Medium",50)
rapier = Weapon("Haven","Rapier","Huge",15)

fool = Enemy("fool",40,3,2,"none")
Marksman = Enemy("Cassius",55,0,2,"none")
Titan = Enemy("Bob",750,0,10,"Hell")
somedude = NPC("Guy",10,2)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

print("----------------------------------")
print("My first videogame ever, even.. if its just a text game, i want to thank anyone, who is watching this..")
print("by just taking the time of being here with me, playing this stupid ass game, i thank you..")
print("I wont talk, but id like if you react to everything via chat or gameplay, remember to type everything in uppercase...")


print("Xid Presents:")
time.sleep(3)
print("Forsaken")
time.sleep(4)




print("....")
time.sleep(2)
print("You wake up in a dark.. cave..")
time.sleep(3)
print("...")
time.sleep(1)



while notnamed == True:
    
    
    name = input("Introduce Your Name: ")
    

    if name != type(int):
        
        questionname = input(f"is this the name you want '{name}'? (Y/N): ")
        questionname = questionname.upper()
        
        if questionname == "Y":
            print("Alright then")
            time.sleep(1)
            print("...")
            time.sleep(1)
            notnamed = False
        
        elif questionname == "N":
            print("ok rename then")
        else:
            print("Y OR N NIGGA")
    
            
player = Player(name,10,0,"block",0)
time.sleep(2)

print(f"Current stats: ")
player.stats()

unweaponed = True

while unweaponed == True:
    questionwep = input("What weapon do you want? (S, S1 for stats)scythe (H, H1 for stats)hammer? ")
    questionwep = questionwep.upper()
    
    if questionwep == "S":
        mainwep = scythe
        print(f"YOU OBTAINED..{mainwep.wpname}!!")
        time.sleep(3)
        unweaponed = False
        
    elif questionwep == "H":
        mainwep = hammer
        print(f"YOU OBTAINED..{mainwep.wpname}!!")
        time.sleep(3)
        unweaponed = False
        
    elif questionwep == "S1":
        scythe.stats()
        
       
    elif questionwep == "H1":
        hammer.stats()
        
    else:
        print("what?")
        
print(f"This is you now then.....")
time.sleep(1)
mainwep.stats()
time.sleep(4)
player.stats()
time.sleep(4)
print("you do not know where you are")
time.sleep(2)
print("find a way out of this bizarre place")
time.sleep(3)
print("----------------------")
print("ACT 1: Forgotten Memory")
print("----------------------")
time.sleep(4)

def game():
    
    def explore():
    
       
        
        def finale():
            
            time.sleep(2)
            print("Shadow: WHAT??? HOW CAN THIS BE??")
            time.sleep(4)
            print("Shadow: DEFEATED BY SUCH A LOWLY AND SHITTY HUMAN??")
            time.sleep(5)
            print(f"{player.name} approches the shadow and gives it the final slash")
            time.sleep(5)
            print("the shadow then falls to the ground.. and says")
            time.sleep(5)
            print("'very well.. but just you remember.. ill....'")
            time.sleep(5)
            print("come....")
            time.sleep(1)
            print("back..")
            time.sleep(5)
            print("and it.. disappears..")
            time.sleep(9)
            print("----------------------")
            print("Epilogue: Forsaken Memory")
            print("----------------------")
            time.sleep(5)
          
            print("you wake up.. in your bed.. its a nice one.. and is currently 6 AM")
            time.sleep(5)
            print("And you feel surprisingly well...")
            time.sleep(7)
            print("Later that day.. you approved an exam you were scared of..")
            time.sleep(7)
            print("The next day.. you managed to ask out the girl that you thought didn't like you")
            time.sleep(7)
            print("The next week.... you got your first car..")
            time.sleep(7)
            print("The next year.... you got married with the girl of your dreams..")
            time.sleep(7)
            print("and in the next decade.... everything that happened in that dream... had been....")
            time.sleep(8)
            print("Forsaken")
            time.sleep(10)
            print("The end.")
            time.sleep(5)
            print("")
            print("CREDITS:")
            time.sleep(3)
            print("Character selection screen music by Heaven pierce her 'The fire is gone'")
            time.sleep(3)
            print("Hub 1 music by potatoteto 'Dilapidated Dungeon'")
            time.sleep(3)
            print("Alley theme By Potatoteto 'Delirious Acting'")
            time.sleep(3)
            print("Mountain theme by pluswplus 'Obscure voices'")
            time.sleep(3)
            print("Fool fight theme by Xid 'Foolish determination'")
            time.sleep(3)
            print("Shop theme By Xid 'Stellar Nighty Shop'")
            time.sleep(3)
            print("Cassius fight By Keygen Church 'Tenebre rosso sangue calm'")
            time.sleep(3)
            print("Forest theme by Heaven Pierce her 'Suffering Leaves Suffering leaves'")
            time.sleep(3)
            print("Desert Music by Heaven pierce her 'Danse Macabre'")
            time.sleep(3)
            print("Revelation Music by heaven pierce her 'The world looks white'")
            time.sleep(3)
            print("Shadow fight Music by heaven pierce her 'Order'")
            time.sleep(5)
            print("This music.. By  Tinfernum 'Sky after the rain'")
            time.sleep(3)
            print("")
            time.sleep(3)
            print("")
            time.sleep(3)
            print("")
            time.sleep(3)
            print("")
            time.sleep(3)
            print("Programmer and creator: Xid")
            time.sleep(3)
            print("")
            time.sleep(1)
            print("")
            time.sleep(1)
            print("")
            time.sleep(3)
            print(f"Thank you for playing.. {player.name}!")
            time.sleep(4)
            input("leave your calification from 1 to 10: ")
            time.sleep(2)
            print("""all reviews and commentaries:
                  Shad: 10/10 "Foreskin"
                  
                  
                  
                  
                  
                  
                  """)
            time.sleep(29)
            quit()
            
        def finale2():
            pass
        
        def garden():
            time.sleep(3)
         
            print("you step onto the garden.. a beautiful... great garden...")
            time.sleep(2)
            print("you see a door, an odd one.. in the middle of the garden.., but you know that this shall wake you up from this terrible nightmare")
            time.sleep(6)
            print("the garden is like if you were in paradise.. something completely different from oscuraby, the sky is white, the flowers are blue")
            time.sleep(6)
            print("But your sword is painted in black")
            time.sleep(4)
            print("you keep moving through.. and get to the door.. but then.. ")
            time.sleep(4)
            print("a shadow appears behind you.... but the door is right infront of you...")
            time.sleep(4)
            print(f"The shadow speaks: going somewhere... {player.name}?, don't you forget about.. something?")
            time.sleep(4)
            print(f"you turn around...")
            time.sleep(2)
            finaldecision = "S"

            
            
            if finaldecision == "D":
                finale2()
            elif finaldecision == "S":
                time.sleep(1)
                print(f"{player.name}: No.. i won't go.. not until you are dead..")
                time.sleep(2)
                print("shadow: i am.. surprised indeed.. you were always a coward.. i know it better myself..")
                time.sleep(4)
                print(f"{player.name}: Just.. Who are you?")
                time.sleep(2)
                print("shadow: i am the personification of your fears.. i created this place.. to torment you")
                time.sleep(4)
                print("shadow: i am The reason you're in such a dream")
                time.sleep(3)
                print("shadow: i am the root of your insecurities, defects and horrible decisions")
                time.sleep(5)
                print(f"shadow: i am you, {player.name}. ")
                time.sleep(3)
                print(f"{player.name}: i am.. nothing like you")
                time.sleep(4)
                print(f"the shadow chuckles.. and responds: is that what you think?, isn't everything here familiar?")
                time.sleep(5)
                print(f"the shadow then mimics your form and keeps talking: just look at me.. i am your greatest failure, your greatest sin")
                time.sleep(4)
                print(f"shadow: and you shall keep being a horrendous and pathetic human being.. {player.name},")
                time.sleep(4)           
                print(f"{player.name}: I.. i don't understand.. what.. do you mean?")
                time.sleep(3)
                print(f"shadow: my job here is not to have such a pathetic coward who even FUCKED AN IMAGINARY WHORE.. to understand ")
                time.sleep(6)
                print(f"shadow: my job here.. is to restrain you in this place... ")
                time.sleep(5)
                print(f"shadow: FOREVER!")
                
                time.sleep(2)
                print("YOU GET AMBUSHED.. BY THE PERSONIFICATION OF YOUR WICKEDNESS!")
                time.sleep(2)
                FINALFIGHTING = True
                while FINALFIGHTING == True:
                    if player.health <= 0:
                        
             
                        time.sleep(2)
                        print("...")
                        time.sleep(1)
                        print("but this causes you to die...")
                        time.sleep(3)
                        print("GAME OVER") 
                        time.sleep(1) 
                        print("final stats:")
                        time.sleep(3)
                        print("... huh???")
                        time.sleep(3)
                        print("Shadow: oh no... we are not done YET!")
                       
                        time.sleep(2)
                        print("YOU HEAL AND STAND BACK UP. YOU HAVE BEEN ADDED A FEW POTIONS")
                        time.sleep(2)
                        player.health = 10
                        player.potion += 3
                        player.spotion += 2
                        Titan.Nhealth += 80
                    elif Titan.Nhealth <= 0:
                        FINALFIGHTING = False
                    
                        finale()
                        
                    enemy_pool = ["A","B","H","D","A","A","H"]
                    dialogue_pool = ["Shadow: A true deception","Shadow: A great and horrendous bulk of crap","Shadow: BE GONE!","Shadow: THIS IS HOW YOU DIE","Shadow: Do not worry, you won't be remembered","Shadow: A true bless for you to die","Shadow: DIE","Shadow: YOU MAKE EVEN THE DEVIL CRY",]
                    if player.burning == True:
                        player.health -= 1
                        time.sleep(1)
                        print("youre still burning and your health decreases by 1!")
                        time.sleep(2)
                    
                    print(f"you have {player.health} health.. and the shadow has {Titan.Nhealth} Health")
                    finalfight = input(f"""
                                       What will you do? {player.name}.
                                       (A)Attack
                                       (D)Drink Potion |Normal potion: {player.potion} |Super potion: {player.spotion}
                                       (S)Drink super Potion
                                       (B)Block
                                       :
                                       """)
                    finalfight = finalfight.upper()
                    if finalfight == "A":
                        time.sleep(1)
                        print(f"You deal {mainwep.damage} damage to The shadow ")
                        Titan.Nhealth -= mainwep.damage
                        time.sleep(1)
                        dialogue = random.choice(dialogue_pool)
                        selected = random.choice(enemy_pool)
                        if selected == "A":
                            time.sleep(1)
                            print(dialogue)
                            player.health -= 8
                            time.sleep(1)
                            print(f"SHADOW ATTACKED YOU AND YOU RECEIVE 8 DAMAGE! your health is {player.health}")
                            time.sleep(2)
                        elif selected == "B":
                            time.sleep(1)
                            print(dialogue)
                            time.sleep(1)
                            print("SHADOW BLOCKS AND NEGATES YOUR DAMAGE! RETALIATING AND DEALING YOU 2 DAMAGE!")
                            player.health -= 2
                            time.sleep(2)
                            Titan.Nhealth += mainwep.damage
                        elif selected == "H":
                            time.sleep(2)
                            print(f"the shadow snaps his fingers.. and regens by 10!")
                            Titan.Nhealth += 10
                            time.sleep(2)
                            
                        elif selected == "D" and player.burning != True:
                            time.sleep(2)
                            print(dialogue)
                            time.sleep(1)
                            print("SHADOW RAINS DOWN FIRE, AND YOU BURN!")
                            player.burning = True
                            time.sleep(2)
                        elif selected == "D" and player.burning == True:
                            time.sleep(1)
                            print("Shadow: DIE SHIT!")
                            time.sleep(1)
                            print("the shadow deals you 5 damage!")
                            player.health -= 5
                            time.sleep(2)
                    elif finalfight == "D" and player.potion >= 1:
                        time.sleep(1)
                        print("you pull out the potion..") 
                        time.sleep(2)
                        print("drinking...")
                        player.potion -= 1
                        time.sleep(2)
                        print("You have been healed by 5!.. and you are not burning")
                        player.burning = False
                        player.health += 5
                        selected = random.choice(enemy_pool)
                        if selected == "A":
                            time.sleep(2)
                            print(dialogue)
                            player.health -= 6
                            time.sleep(1)
                            print(f"SHADOW ATTACKED YOU AND YOU RECEIVE 6 DAMAGE! your health is {player.health}")
                            time.sleep(2)
                        elif selected == "B":
                            time.sleep(2)
                            print(dialogue)
                            time.sleep(1)
                            print("SHADOW ENRAGES AND DEALS YOU 10 DAMAGE!")
                            player.health -= 10
                            time.sleep(2)
                            Titan.Nhealth += mainwep.damage
                        elif selected == "H":
                            time.sleep(2)
                            print(f"the shadow snaps his fingers.. and regens by 5!")
                            Titan.Nhealth += 5
                            time.sleep(2)
                            
                        
                    elif finalfight == "D" and player.potion <= 0:
                        time.sleep(1)
                        print("You have no potions!")
                        time.sleep(1)
                    elif finalfight == "S" and player.spotion >= 1:
                        time.sleep(1)
                        print("you pull out the potion..") 
                        time.sleep(2)
                        print("drinking...")
                        player.spotion -= 1
                        time.sleep(2)
                        print("You have been healed by 20!")
                        player.health += 20
                        selected = random.choice(enemy_pool)
                        
                        if selected == "A":
                            time.sleep(2)
                            print(dialogue)
                            player.health -= 6
                            time.sleep(1)
                            print(f"SHADOW ATTACKED YOU AND YOU RECEIVE 6 DAMAGE! your health is {player.health}")
                            time.sleep(2)
                     
                        elif selected == "H":
                            time.sleep(2)
                            print(f"the shadow snaps his fingers.. and regens by 5!")
                            Titan.Nhealth += 5
                            time.sleep(2)
                            
                        elif selected == "D" and player.burning != True:
                            time.sleep(2)
                            print(dialogue)
                            time.sleep(1)
                            print("SHADOW RAINS DOWN FIRE, AND YOU BURN!")
                            player.burning = True
                            time.sleep(2)
                        elif selected == "D" and player.burning == True:
                            time.sleep(1)
                            print("Shadow: DIE SHIT!")
                            time.sleep(1)
                            print("the shadow deals you 5 damage!")
                            player.health -= 5
                            time.sleep(2)
                        
                    elif finalfight == "S" and player.spotion <= 0:
                        time.sleep(1)
                        print("You have no super potions!")
                        time.sleep(1)
                        
                    elif finalfight == "B":
                        time.sleep(1)
                        print("YOU BLOCK!")
                        time.sleep(1)
                        selected = random.choice(enemy_pool)
                        if selected == "A":
                            time.sleep(2)
                            print(dialogue)
                            player.health -= 2
                            time.sleep(1)
                            print(f"SHADOW ATTACKED YOU AND YOU AND PIERCED THROUGH YOUR DEFENSE AND RECEIVE 2 DAMAGE! your health is {player.health}")
                            time.sleep(2)
                     
                        elif selected == "H":
                            time.sleep(2)
                            print(f"the shadow snaps his fingers.. and regens by 5!")
                            Titan.Nhealth += 5
                            time.sleep(2)
                            
                        elif selected == "D" and player.burning != True:
                            time.sleep(2)
                            print(dialogue)
                            time.sleep(1)
                            print("SHADOW RAINS DOWN FIRE, AND YOU BURN!")
                            player.burning = True
                            time.sleep(2)
                        elif selected == "D" and player.burning == True:
                            time.sleep(1)
                            print("Shadow: DIE SHIT!")
                            time.sleep(1)
                            print("the shadow deals you 5 damage!")
                            player.health -= 5
                            time.sleep(2)
                    else:
                        print("WHAT???")
            
                
                
            
        
        def desert():
       
            
            print("you arrive at the desert.. a gray.. dead.. desert")
            time.sleep(3)
            deserting = True
            while deserting == True:
                print("there is two ways.. one with a (C)chest.. guarded by strange looking figures.. and the other a (H)house similar to the one before.. or (R)return?")
                desertchoice = input(": ")
                desertchoice = desertchoice.upper()
                if desertchoice == "R":
                    time.sleep(2)
                    print("you return")
                    time.sleep(1)
                    forest()
                elif desertchoice == "H":
                    print("you enter the house and close the door..")
                
                    time.sleep(2)
                    housing = True
                    while housing == True:
                        print("there is a weird looking (G)guy and some (B)boxes.. (R)return?")
                        housechoice = input(":")
                        housechoice = housechoice.upper()
                        if housechoice == "B":
                            time.sleep(2)
                            print("Searching through it...")
                            time.sleep(1)
                            print("found 1 'potion'!")
                            player.potion += 1
                            time.sleep(2)
                        elif housechoice == "G":
                            time.sleep(2)
                            print("Peyton: uh?, hey you uh. wanna buy sum stuff?")
                            merchanting = True
                            while merchanting == True:
                                print(f"your coins: {player.coins}")
                                buying = input("""
                                        (1): Potion (1 Coin)
                                        (2): Super Potion (4 coin)
                                        (R): Return
                                        :
                                        """)
                                buying == buying.upper()
                                if buying == "1" and player.coins != 0:
                                    time.sleep(1)
                                    print("you obtained 1 'potion'!")
                                    player.potion += 1
                                    player.coins -= 1
                                    time.sleep(2)
                                    print("Peyton: SEE? its good quality!, it even takes off burns")
                                    time.sleep(2)
                                
                                elif buying == "2" and player.coins >= 4:
                                    time.sleep(1)
                                    print("you obtained 'Super Potion'!")
                                    player.coins -= 4
                                    player.spotion += 1
                                    time.sleep(2)
                                    print("Peyton: THAT'LL HEAL YOU A TON DUDE..")
                                    time.sleep(2)
                                  
                                elif buying == "R":
                                    time.sleep(2)
                                    print(f"Peyton: not even a bye?, huh")
                                    time.sleep(1)
                                    print("you go back")
                                    time.sleep(2)
                                    merchanting = False
                                    desert()
                        elif housechoice == "R":
                            time.sleep(1)
                            print("you get out of the house")
                            time.sleep(2)
                            desert()
                
                
                elif desertchoice == 'C' and player.chestcusion != True:
                    time.sleep(1)
                    print("you venture forth, in direction to the chest..")
                    time.sleep(3)
                    print("...")
                    player.health += 10
                    time.sleep(1)
                    print("BUT YOU GET AMBUSHED BY SHADOWS!")
                    time.sleep(2)
                    print(f"You have {player.health} health.. enemy has no health???")  
                    input("""Will you
                                (A)attack
                                (D)Drink Potion
                                (P)pass
                                (S)Special attack
                                :""")
                    time.sleep(2)
                    print(f"you deal {mainwep.damage} Damage to SHADOW")
                    time.sleep(2)
                    print("SHADOW HAS BEEN DEFEATED!.. BUT ANOTHER ONE COMES IN")
                    time.sleep(2)
                    print(f"You have {player.health} health.. enemy has no health???")  
                    input("""Will you
                                (A)Attack
                                (D)Drink Potion
                                (P)pass
                                (*_01#9)DIE
                                :""")
                    time.sleep(2)
                    print(f"you deal {mainwep.damage} Damage to SHADOW")
                    time.sleep(2)
                    print("SHADOW HAS BEEN DEFEATED!.. BUT ANOTHER ONE COMES IN")
                    time.sleep(2)
                    print(f"You have {player.health} health.. enemy has no health???")  
                    input("""Will you
                                (A)ATTACK
                                (D)Drink Potion
                                (:;'1-_*&)DIE
                                (*_01#9)DIE
                                :""")
                    time.sleep(2)
                    print(f"you deal {mainwep.damage} Damage to SHADOW")
                    time.sleep(2)
                    print("SHADOW HAS BEEN DEFEATED!.. BUT ANOTHER ONE COMES IN")
                    time.sleep(2)
                    print(f"You have {player.health} health.. enemy has no health???")
                      
                    input("""Will you
                                (A)ATTACK
                                (0]\|1`~)DIE
                                (-+=1>/)DIE
                                (*&5%12)DIE
                                :""")
                    time.sleep(2)
                    print(f"you deal {mainwep.damage} Damage to SHADOW")
                    time.sleep(2)
                    print("SHADOW HAS BEEN DEFEATED!.. BUT ANOTHER ONE COMES IN")
                    time.sleep(2)
                    print("ANOTHER ONE COMES IN")
                    time.sleep(1)
                    print("AND ANOTHER ONE COMES IN")
                    time.sleep(1)
                    print("AND ANOTHER ONE COMES IN")
                    time.sleep(1)
                    print("AND ANOTHER ONE COMES IN")
                    time.sleep(1)
                    print("AND ANOTHER ONE COMES IN")
                    time.sleep(1)
                    print("AND ANOTHER ONE COMES IN")
                    time.sleep(1)
                    print("AND ANOTHER ONE COMES IN")
                    time.sleep(3)
                    print("but they... do not fight you no more..")
                    time.sleep(3)
                    print("they see your figure. with your motivation shining")
                    time.sleep(4)
                    print("the shadows retreat...")
                    time.sleep(3)
                    print("you make your way to the chest.. open it.. and see the key.. you.. take it..")
                    time.sleep(2)
                    print("YOU OBTAINED 'THE GARDEN KEY'.. YOUR NIGHTMARE IS ALMOST OVER!")
                    player.gardenkey = True
                    player.chestcusion = True
                    time.sleep(3)
                    desert()
                elif desertchoice == "C" and player.chestcusion == True:
                    time.sleep(1)
                    print("i will not go there again")
                    time.sleep(1)
                    
                
                else:
                    print("what?")
            
            
        
        def forest():
            foresting = True
            while foresting == True:
    
                print("a path.. to a (G)garden lies infront of you.. but a small deviation appears on the (L)left.. what.. do.. you.. do or (R)Return? ")
                forest_question = input(": ")
                forest_question = forest_question.upper()
            
                if forest_question == "G" and player.enemy2def == False:
                            print("...")
                            time.sleep(2)
                          
                            
                            
                            time.sleep(2)
                            print(f"YOU GET AMBUSHED BY {Marksman.Nname}")
                            time.sleep(2)
                            print(f"Cassius: You shall stay here FOREVER")
                            time.sleep(2)
                            
                            
                            fight1 = True
                            while fight1 == True:
                              enemy_pool = ["A","B","H"]
                              
                              if player.health <= 0:
                             
                      
                               time.sleep(2)
                               print("...")
                               time.sleep(1)
                               print("but this causes you to die...")
                               time.sleep(3)
                               print("GAME OVER") 
                               time.sleep(1) 
                               player.stats()
                               print("final stats:")
                               time.sleep(6)
                               print("cassius will try to deceive you.. break through it!")
                               time.sleep(4)
                               player.health = 5
                               Marksman.Nhealth = 50
                               hub2()
                               
                              if Marksman.Nhealth <= 0:
                                print(".. Cassius.. HAS BEEN DEFEATED!") 
                                time.sleep(1)
                                print("you gain 15 coins!")
                                player.coins += 15
                                time.sleep(2)
                                player.enemy2def = True
                                fight1 = False
                                forest()
                                 
                                 
                              print(f"You have {player.health} health.. enemy has {Marksman.Nhealth} health")  
                              attack = input("""Will you
                                             (A)attack
                                             (D)Drink potion
                                             (P)Drink super potion
                                             (S)special """)
                              attack = attack.upper()
                              
                              
                                  
                              if attack == "A":
                                Marksman.Nhealth -= mainwep.damage
                                print(f"you dealt {mainwep.damage} damage to {Marksman.Nname} and he has {Marksman.Nhealth} Health")
                                time.sleep(2)
                                selected = random.choice(enemy_pool)
                                
                                if selected == "A":
                                    print(f"{Marksman.Nname} attacks you!, hurting you by 4!")
                                    player.health -= 4
                                    time.sleep(2)
                                
                                elif selected == "B":
                                    print(f"Cassius blocks!, negating your damage")
                                    Marksman.Nhealth += mainwep.damage
                                    time.sleep(2)
                                
                                elif selected == "H" and Marksman.potion >= 1:
                                    print("Cassius takes out a potion..")
                                    time.sleep(2)
                                    print("he drinks it...")
                                    time.sleep(2)
                                    print("Cassius has been healed by 5!")
                                    Marksman.potion -= 1
                                    Marksman.Nhealth += 5
                                    time.sleep(2)
                                    
                                elif selected == "H" and Marksman.potion <= 0:
                                    print("Marksman.. tries to heal but has no potion")
                                    time.sleep(2)
                            
                              elif attack == "D" and player.potion >= 1:
                                print("you pull out the drink..")
                                time.sleep(2)
                                print("drinking...")
                                time.sleep(2)
                                player.potion -= 1
                                player.health += 5
                                print("you have been healed by 5!")
                                time.sleep(1)
                                selected = random.choice(enemy_pool)
                                
                                if selected == "A":
                                    print(f"{Marksman.Nname} attacks you!, hurting you by 4!")
                                    player.health -= 4
                                    time.sleep(2)
                                
                                
                                elif selected == "H" and Marksman.potion >= 1:
                                    print("Cassius takes out a potion..")
                                    time.sleep(2)
                                    print("he drinks it...")
                                    time.sleep(2)
                                    print("Cassius has been healed by 3!")
                                    Marksman.potion -= 1
                                    Marksman.Nhealth += 3
                                    time.sleep(2)
                                    
                                elif selected == "H" and Marksman.potion <= 0:
                                    print("Cassius.. tries to heal but has no potion")
                                    
                                    
                                
                              elif attack == "D" and player.potion <= 0:
                                print("you have no potions..")
                                
                              elif attack == "S":
                                  print("you block!")
                                  time.sleep(1)
                                  
                                  selected = random.choice(enemy_pool)
                                  
                                  if selected == "A":
                                    print(f"{Marksman.Nname} attacks you!, but you blocked..")
                                    
                                    time.sleep(2)
                            
                                
                                  elif selected == "H" and Marksman.potion >= 1:
                                    print("Cassius takes out a potion..")
                                    time.sleep(2)
                                    print("he drinks it...")
                                    time.sleep(2)
                                    print("Cassius has been healed by 4!")
                                    Marksman.Nhealth += 4
                                    Marksman.potion -= 1
                                    time.sleep(2)
                                    
                                  elif selected == "H" and Marksman.potion <= 0:
                                    print("cassius.. tries to heal but has no potion")
                                    
                              elif attack == "P" and player.spotion >= 1:
                                  time.sleep(1)
                                  print("you take out the massive drink..")
                                  time.sleep(2)
                                  print("drinking it..")
                                  time.sleep(2)
                                  print("You have been healed by 15!")
                                  player.spotion -= 1
                                  player.health += 15
                                  time.sleep(1)
                                  selected = random.choice(enemy_pool)
                                
                                  if selected == "A":
                                    print(f"{Marksman.Nname} attacks you!, hurting you by 4!")
                                    player.health -= 4
                                    time.sleep(2)
                                
                                
                                  elif selected == "H" and Marksman.potion >= 1:
                                    print("Cassius takes out a potion..")
                                    time.sleep(2)
                                    print("he drinks it...")
                                    time.sleep(2)
                                    print("Cassius has been healed by 3!")
                                    Marksman.potion -= 1
                                    Marksman.Nhealth += 3
                                    time.sleep(2)
                                    
                                  elif selected == "H" and Marksman.potion <= 0:
                                    print("Cassius.. tries to heal but has no potion")
                                    
                              elif attack == "P" and player.spotion == 0:
                                  print("you have no super potions")
                                  
                                  
                                 
                              else:
                                print("what")  
                    
                             
                
                
                elif forest_question == "G" and player.enemy2def == True:
                   time.sleep(2)
                   print("you go forth")
                   time.sleep(1)
                   print("...")
                   time.sleep(2)
                   if player.gardenkey == False:
                       print("there is a massive gate.. its closed.. you will need a key")
                       time.sleep(2)
                       forest()
                   elif player.gardenkey == True:
                       time.sleep(1)
                       print("if you go forth.. you wont be able to go back... this is the end of your journey..")
                       time.sleep(3)
                       finaledec = True
                       while finaledec == True:
                           
                           finaldec = input("will you go to the (G)garden.. or (R)return?")
                           finaldec = finaldec.upper()
                           if finaldec == "R":
                               
                               time.sleep(1)
                               print("wise choice")
                               time.sleep(2)
                               finaledec = False
                               forest()
                           
                           elif finaldec == "G":
                               finaledec = False
                               garden()
                     
                     
                 
                
                elif forest_question == "L":
                    time.sleep(2)
                    print("you proceed through the small hole... but on your way out.. you find a strange man..")
                    time.sleep(3)
                    print(f"Accius: Greetings... {player.name}")
                    talking = True
                    while talking == True:
                        npctalk = input("""
                                         (1): How do you know my name?
                                         (2): who or what are you?
                                         (3): what is this place?
                                         (4): Goodbye.
                                         """)
                        if npctalk == "1":
                            
                            time.sleep(2)
                            print(f"Accius: because dear {player.name}..")
                            time.sleep(2)
                            print( "this... is a dream")
                        
                            time.sleep(2)
                            print(f"{player.name}: What????")
                            time.sleep(6)
                            print(f"Accius: i am also a product of this wretched dream.. your mind is in deep pain and depression")
                            time.sleep(4)
                            print(f"Accius: and if.. if you do not defeat the source of your pain... you will be here.. forever.. tormented in your own..")
                            time.sleep(5)
                            print("perfect")
                            time.sleep(1)
                            print("hell")
                            time.sleep(3)
                          
                            
                        elif npctalk == "2":
                            print(f"Accius: i'm Accius.. you know me. im certain you do.. and im here to help you get out.. im no demon. i am a man..")
                            time.sleep(2)
                    
                        elif npctalk == "3":
                            print(f"{somedude.Nname}: its called Oscuraby, a place that is composed of your worst memories that had been.. forsaken")
                            time.sleep(5)
                            print(f"the key to the garden lies ahead.. proceed {player.name} and make me proud.")
                            time.sleep(3)
                            print(f"i shall lend you.. my sword, so you can rend the demons apart...")
                            time.sleep(4)
                            print(f"YOU OBTAINED {Holy_Sword.wpname}!, your previous weapon has been destroyed, return to hub to see stats")
                            mainwep.type = Holy_Sword.type
                            mainwep.damage = Holy_Sword.damage
                            mainwep.size = Holy_Sword.size
                            mainwep.wpname = Holy_Sword.wpname
                            time.sleep(3)
                            
                
                            
                        
                        elif npctalk == "4":
                            print("Accius: Hope and light.. be upon you")
                            talking = False
                            desert()
                if forest_question == "R":
                        hub2()
                        
        
                     
                
                else:
                    print("what?")
            
        def hub2():
            helldoing = True
            while helldoing == True:
               print(f"what will you do...{player.name}?....")
               hell_question = input("(W)See weapon, (C)See character, (G)Go forth in the forest, (R)Rest, (D)drink potion, (Q)Quit: ")
               hell_question = hell_question.upper()
                 
               match hell_question:
                    case "W":
                          mainwep.stats()
                    case "C":
                          player.statshelll()
                    case "G":
                        print("you venture forth.. into the forest..")
                        time.sleep(2)
                        forest()
                    
                    case "R":
                         print("you rest amidst the horrible darkness..")
                         player.health += 2
                         player.motivation += 1
                         time.sleep(2)
                         print("you feel like youre healed.... and your motivation increases..")
                         time.sleep(1)
                    case "Q":
                         print("its too late.. for that")
                
               if hell_question == "D" and player.potion != 0:
            
                  print("Opening potion..")
                  time.sleep(1)
            
                  print("drinking....")
                  time.sleep(2)
            
                  player.potion -= 1 
                  player.health += 5
            
                  print("You have been healed by 5!")
                  time.sleep(2)
            
               elif hell_question == "D" and player.potion <= 0:
                   print("you have no potions")
                 
      
                
        def act2intro():
            time.sleep(3)
            print("----------------------")
            print("ACT 2: Wake up call")
            print("----------------------")
            time.sleep(6)
            print("...")
            print("you wake up... the sky is gray a great black spot on it, a great storm is occurring..")
            time.sleep(4)
            print("this is like a nightmare")
            time.sleep(3)
            print("youre now in what it seems like a forest.. a dark.. twisted one...")
            time.sleep(5)
            print("you")
            time.sleep(1)
            print("must")
            time.sleep(1)
            print("find")
            time.sleep(1)
            print("a")
            time.sleep(1)
            print("way")
            time.sleep(1)
            print("out.")
            time.sleep(4)
            print("hopefully there was a potion bottle beside you, how convenient")
            player.potion += 1
            time.sleep(2)
            hub2()
            
        
            
    
        
        
        def alley():
            alleying = True
            while alleying == True:
               print("There is some dude named (G)Guy, Some (S)spines and uh.. a (W)whore.. wachu gon do or (R)return?")
               alleyquest = input("tip.. (C) of see character will always work: ")
               alleyquest = alleyquest.upper()
               
               if alleyquest == "G":
                   time.sleep(2)
                   print("you approach the man")
                   time.sleep(1)
                   talkedto = False
                   if talkedto != True:
                       
                       talking = True
                       
                       while talking == True:
                        print(f"Unknown: Uh?, Hi, Name's {somedude.Nname} nice to meet you, wachu need?")
                        npctalk = input("""
                                        (1): Wachu doing here?
                                        (2): Fuck off nerd
                                        (3): whats this foolish place?
                                        (4): *threathen*
                                        (5): see yah
                                        :
                                        """)
                        if npctalk == "1":
                            print(f"""{somedude.Nname}: Im trying to find some stuff, id normally tell you to find it but xid
                                  aint gon write a whole quest for that and we know that""")
                            time.sleep(3)
                            
                        elif npctalk == "2":
                            print(f"{somedude.Nname}: ALRIGHT THEN FUCK YOU")
                            
                            talkedto = True
                            talking = False
                    
                        elif npctalk == "3":
                            print(f"{somedude.Nname}: its called Grimsby, a forsaken land of weird people, you will not be welcome here")
                            time.sleep(5)
                            print(f"im certain of it, but you got some weapon.. its a {mainwep.type} right?, it'll help you and uh there is an entrance in that mountain.. here have a key for it")
                            time.sleep(2)
                            print("YOU OBTAIN, THE MOUNTAIN KEY!")
                            time.sleep(2)
                            player.key = True
                            time.sleep(6)
                            
                        
                        elif npctalk == "4":
                            somedude.treathened()
                        
                        elif npctalk == "5":
                            print(f"{somedude.Nname}: See you too {player.name}....")
                            talking = False
        
                        else:
                            print(f"{somedude.Nname}: what? ")
                            time.sleep(1)
                        
                   else:
                     print(f"{somedude.Nname}: Go away, i dont wanna talk to you")
               elif alleyquest == "R":
                   print("you return")
                   time.sleep(2)
                   explore()
                   alleying = False
                
               elif alleyquest == "S":
                   time.sleep(1)
                   print("you try to touch the spines but..")
                   time.sleep(2)
                   print("you get hit by them spines and.. your health decreases by 2...!")
                   time.sleep(3)
                   print("but you see something in the spines.. D7..")
                   time.sleep(2)
                   player.health -= 2
                   if player.health <= 0:
                      
                      time.sleep(2)
                      print("...")
                      time.sleep(1)
                      print("but this causes you to die...")
                      time.sleep(3)
                      print("GAME OVER") 
                      time.sleep(1) 
                      player.stats()
                      print("final stats:")
                      time.sleep(6)
                     
                      quit()
                
               elif alleyquest == "W" and player.aidsonce != True:
                   time.sleep(1)
                   print("you approach the whore..")
                   time.sleep(2)
                
                   print("the beautiful woman seduces you to have a passionate night cost free... she whispers 'A2'...")
                   time.sleep(2)
                   print("...")
                   time.sleep(1)
                  
                   print("AND NOW YOU GET AIDS!.. your health decreases by 7!")
                   player.aidsonce = True
                   time.sleep(2)
                   player.health -= 7
                   player.aids = True
                   if player.health <= 0:
    
                      
                      time.sleep(2)
                      print("...")
                      time.sleep(1)
                      print("but this causes you to die...")
                      time.sleep(3)
                      print("GAME OVER") 
                      time.sleep(1) 
                      player.stats()
                      print("final stats:")
                      time.sleep(6)
                      quit()
                   
                   
               elif alleyquest == "W" and player.aidsonce == True:
                   time.sleep(1)
                   print("i dont think i want more aids dude.. but she said A2")
                   time.sleep(1)
                   
                   
                      
               elif alleyquest == "C":
                   player.stats()
                
               else:
                  print("what?")
                    
            
            
        def house(mainwp):
            housing = True
            while housing == True:
               print("you enter a house, its been forsaken, there is a (D)drawer and some (S)sink.. wachu gon do? or will you (R)return?")
               explorehou = input(":")
               explorehou = explorehou.upper()
               
               if explorehou == "D":
                   
                   if mainwp.type != Glaive.type:
                       checkingwep = True
                       while checkingwep == True:
                          print(f"you find a...{Glaive.type}!.. will you take it instead of {mainwp.wpname}?")
                          schoice = input("(T)take (L)leave (C)compare stats: ")
                          schoice = schoice.upper()
                       
                          if schoice == "T":
                              mainwep.type = Glaive.type
                              mainwep.damage = Glaive.damage
                              mainwep.size = Glaive.size
                              mainwep.wpname = Glaive.wpname
                              mainwp = Glaive
                              print(f"YOU OBTAINED A NEW WEAPON! '{Glaive.wpname}' Has been obtained!.. your previous weapon has been destroyed")
                              time.sleep(3)
                              checkingwep = False
                          elif schoice == "L":
                              print("yeah screw that")
                              checkingwep == False
                              explore()
                             
                          elif schoice == "C":
                              mainwp.stats()
                              Glaive.stats()
                          
                   else:
                       print("nothing to see here..")
                   
               elif explorehou == "S":
                   if player.potion <= 0:
                     print("found a potion!")
                     print("and see a number in the sink.. 'B0'")
                     time.sleep(3)
                     player.potion += 1
                   else:
                       print("you see a number in the sink.. 'B0'")
                       time.sleep(3)
                   
               
               elif explorehou == "C":
                   player.stats()
               
               elif explorehou == "R":
                   explore()
                   
               elif explorehou == "W":
                   mainwep.stats()
                   
               else:
                   print("what?")
            
        def mountain():
           
            def mountain_inside():
                if player.key != False:
                    print("Door is open, pass..")
                    mountain_explore = True 
                    while mountain_explore == True:
                        
                        print("2 paths, (L)left or (E)even lefter? or (R)return?")
                        mountchoice = input(":")
                        mountchoice = mountchoice.upper()
                        
                        if mountchoice == "R":
                            mountain()
                            mountain_explore = False
                        elif mountchoice == "L":
                            print(f"there is a big wooden door, you cant chop it with {mainwep.wpname} cause story reasons")
                            print("it says 'only those with the forgotten pass may get through here'.. looks like a 4 digit password")
                            password = input("enter pass or (R)return: ")
                            
                            if password == "R":
                                mountain_explore = False
                                mountain_inside()
                            elif password == "2007":
                                print("YES THAT WAS IT")
                                time.sleep(3)
                                print("... there is.. a massive hole..")
                                time.sleep(3)
                                actdec = True
                                while actdec == True:
                                    print("will you.. (T)throw yourself down...? or (R)return?, (if you do, you will not be able to return here")
                                    decision = input(":")
                                    decision = decision.upper()
                                    if decision == "T":
                                        
                                        print("and so, you fall through the hole..")
                                        time.sleep(3)
                                        print("and.. its an empty void, you cant see the surface, or where youre falling to")
                                        time.sleep(5)
                                        print("you can only hear the wind blasting through your ears")
                                        time.sleep(3)
                                        actdec = False
                                        act2intro()
                                    elif decision == "R":
                                        actdec = False
                                        mountain_inside()
                                    
                            elif password == "6969":
                                print("Haha funny but no")
                            elif password == "1987":
                                print("WAS THAT THE BITE OF 87?")
                            else:
                                print("wrong pass")
                        elif mountchoice == "E" and player.enemy1def != True:
                            print("...")
                            time.sleep(2)
                          
                            
                            time.sleep(2)
                            print(f"YOU GET AMBUSHED BY {fool.Nname}")
                            time.sleep(2)
                            print(f"fool: GIVE ME ALL OF YOUR STUFF!")
                            time.sleep(2)
                            
                            
                            fight1 = True
                            while fight1 == True:
                              enemy_pool = ["A","B","H"]
                              
                              if player.health <= 0:
                           
                      
                               time.sleep(2)
                               print("...")
                               time.sleep(1)
                               print("but this causes you to die...")
                               time.sleep(3)
                               print("GAME OVER") 
                               time.sleep(1) 
                               player.stats()
                               print("final stats:")
                               time.sleep(6)
                               quit()
                               
                              if fool.Nhealth <= 0:
                                print(".. fool HAS BEEN DEFEATED!") 
                                time.sleep(1)
                                print("you gain 4 coins!")
                                player.coins += 4
                                time.sleep(2)
                                player.enemy1def = True
                                fight1 = False
                             
                                mountain_inside()
                                 
                                 
                              print(f"You have {player.health} health.. enemy has {fool.Nhealth} health")  
                              attack = input("""Will you
                                             (A)attack
                                             (D)Drink potion
                                             (P)Pass 
                                             (S)special """)
                              attack = attack.upper()
                              
                              
                                  
                              if attack == "A":
                                fool.Nhealth -= mainwep.damage
                                print(f"you dealt {mainwep.damage} damage to {fool.Nname} and he has {fool.Nhealth} Health")
                                time.sleep(2)
                                selected = random.choice(enemy_pool)
                                
                                if selected == "A":
                                    print(f"{fool.Nname} attacks you!, hurting you by 2!")
                                    player.health -= 2
                                    time.sleep(2)
                                
                                elif selected == "B":
                                    print(f"fool blocks!, negating your damage")
                                    fool.Nhealth += mainwep.damage
                                    time.sleep(2)
                                
                                elif selected == "H" and fool.potion >= 1:
                                    print("fool takes out a potion..")
                                    time.sleep(2)
                                    print("he drinks it...")
                                    time.sleep(2)
                                    print("fool has been healed by 3!")
                                    fool.potion -= 1
                                    fool.Nhealth += 3
                                    time.sleep(2)
                                    
                                elif selected == "H" and fool.potion <= 0:
                                    print("fool.. tries to heal but has no potion")
                                    time.sleep(2)
                            
                              elif attack == "D" and player.potion >= 1:
                                print("you pull out the drink..")
                                time.sleep(2)
                                print("drinking...")
                                time.sleep(2)
                                player.potion -= 1
                                player.health += 5
                                print("you have been healed by 5!")
                                time.sleep(1)
                                selected = random.choice(enemy_pool)
                                
                                if selected == "A":
                                    print(f"{fool.Nname} attacks you!, hurting you by 2!")
                                    player.health -= 2
                                    time.sleep(2)
                                
                                
                                elif selected == "H" and fool.potion >= 1:
                                    print("fool takes out a potion..")
                                    time.sleep(2)
                                    print("he drinks it...")
                                    time.sleep(2)
                                    print("fool has been healed by 3!")
                                    fool.potion -= 1
                                    fool.Nhealth += 3
                                    time.sleep(2)
                                    
                                elif selected == "H" and fool.potion <= 0:
                                    print("fool.. tries to heal but has no potion")
                                    
                                    
                                
                              elif attack == "D" and player.potion <= 0:
                                print("you have no potions..")
                                
                              elif attack == "S":
                                  print("you block!")
                                  time.sleep(1)
                                  
                                  selected = random.choice(enemy_pool)
                                  
                                  if selected == "A":
                                    print(f"{fool.Nname} attacks you!, but you blocked..")
                                    
                                    time.sleep(2)
                            
                                
                                  elif selected == "H" and fool.potion >= 1:
                                    print("fool takes out a potion..")
                                    time.sleep(2)
                                    print("he drinks it...")
                                    time.sleep(2)
                                    print("fool has been healed by 3!")
                                    fool.Nhealth += 3
                                    fool.potion -= 1
                                    time.sleep(2)
                                    
                                  elif selected == "H" and fool.potion <= 0:
                                    print("fool.. tries to heal but has no potion")
                                  
                                 
                              else:
                                print("what")  
                        
                        elif mountchoice == "E" and player.enemy1def == True:
                            print("you continue on the path.. and see a funny fellow infront of you with a tent")
                            time.sleep(2)
                   
                            print("Devol: Oh?, greetings.. foreigner.. to my humble shop.. what may you buy?")
                            time.sleep(2)
                            
                            merchanting = True
                            while merchanting == True:
                                print(f"your coins: {player.coins}")
                                buying = input("""
                                        (1): Potion (1 Coin)
                                        (2): TAR "aids cure" (1 coin)
                                        (3)(3W to see stats): Rapier (2 coins)
                                        (R): Return
                                        :
                                        """)
                                buying = buying.upper()
                                
                                if buying == "1" and player.coins >= 1:
                                    time.sleep(1)
                                    print("you obtained 1 'potion'!")
                                    player.potion += 1
                                    player.coins -= 1
                                    time.sleep(2)
                                    print("Devol: Groovy.. aint it?")
                                    time.sleep(2)
                                
                                elif buying == "2" and player.aids == True and player.coins >= 1:
                                    time.sleep(1)
                                    print("you obtained TAR, Cure for aids!'!")
                                    player.aids = False
                                    player.coins -= 1
                                    time.sleep(2)
                                    print("you quickly swallow the tar.. THE AIDS DISAPPEAR!")
                                    time.sleep(2)
                                    print("Devol: Lucky fella, dont go around weird women next time hehe")
                                    time.sleep(2)
                                    
                                elif buying == "2" and player.aids == False:
                                    print("i Do not have aids")
                                    time.sleep(1)
                                elif buying == "3" and player.rapierbought != True and player.coins >= 2:
                                    print(f"YOU OBTAINED.. {rapier.wpname}!, Your previous weapon has been destroyed")
                                    player.coins -= 2
                                    mainwep.type = rapier.type
                                    mainwep.wpname = rapier.wpname
                                    mainwep.damage = rapier.damage
                                    mainwep.size = rapier.size
                                    player.rapierbought = True
                                    time.sleep(3)
                                elif buying == "3" and player.rapierbought == True:
                                    print("devol: i'm afraid you already bought it friend..")
                                    time.sleep(1)
                                elif buying == "3W":
                                    time.sleep(1)
                                    rapier.stats()
                                    time.sleep(2)
                                  
                                elif buying == "R":
                                    print(f"Devol: ill be seeing you again.. {player.name}")
                                    time.sleep(2)
                                    print("why do everyone.. know my name?")
                                    time.sleep(1)
                                    print("you go back")
                                    time.sleep(2)
                                    merchanting = False
                                    mountain_inside()


                else: 
                    print("there is a massive rock door.. seems like you need a key...")
                
            
            mountaning = True
            while mountaning == True:
              print("you go to the mountain, there is some (S)stairs, and an (E)entrance, wachu gon do or will you (R)return?")
              mountainquest = input(":")
              mountainquest = mountainquest.upper()
              
              if mountainquest == "E":
                  mountain_inside()
              elif mountainquest == "R":
                  hub()
                
              elif mountainquest == "S":
                  print("going up the stairs..")
                  time.sleep(2)
                  stairexploration = True
                  while stairexploration == True:
                      print("There is a dude, looks threathening but.. he doesnt move an inch...") 
                      stairchoice = input("wachu do? (T)talk with him (R)Return: ")
                      stairchoice = stairchoice.upper()
                      
                      if stairchoice == "R":
                          print("going down the stairs..")
                          time.sleep(1)
                          stairexploration = False
                          
                      elif stairchoice == "T":
                          if player.aids == True:
                             time.sleep(1)
                             print("The dude snaps, and says 'im not talking to a filthy aids carrier'")
                             time.sleep(2)
                             print("seems like you will need to get rid of it to talk to this man..")
                             time.sleep(2)
                             
                          elif player.aids == False:
                              time.sleep(1)
                              print("The dude mumbles 'C0' ")
                              time.sleep(2)
                  
              elif mountainquest == "C":
                  player.stats()
                  
              
            
        exploring = True
        while exploring == True:
      
           
            
            print("There is an (A)alley, a (H)house and a (M)mountain.. which one you wanna see? or (R)return?")
            exploringquest = input(":")
            exploringquest = exploringquest.upper()
            
            if exploringquest == 'R':
                time.sleep(2)
                print("you venture back into the cave")
                time.sleep(1)
                exploring = False
                hub()
            elif exploringquest == 'A':
                time.sleep(2)
                print("you go to the cheery but bizarre alley")
                time.sleep(1)
                alley()
                
            elif exploringquest == 'H':
                house(mainwep)
                
            elif exploringquest == 'M':
                time.sleep(2)
                print("you venture into the massive and somewhat spooky mountain")
                time.sleep(1)
                mountain()
            elif exploringquest == "1983":
                finale()
            
            
            else:
                print("what?")
            
        
    
   
            
        
    def hub(): 
      gaming = True
      
      
      while gaming == True:
        
        print("(W)See weapon, (C)See character, (E)Explore, (R)Rest, (D)drink potion, (Q)Quit, ")  
        main_question = input(f"What do you want to do {player.name}?: ")
        main_question = main_question.upper()
        
        
        match main_question:
            case "W":
                mainwep.stats()
            case "C":
                player.stats()
            case "E":
                explore()
                print("you adventure out of the cave..")
                time.sleep(2)
                gaming = False
            case "R":
                print("you rest..")
                player.health += 1
                time.sleep(2)
                print("you feel like youre healed..")
                time.sleep(1)
            case "Q":
                print("Bye then fool")
                quit()
    
                
                
                
        if main_question == "D" and player.potion != 0:
            
            print("Opening potion..")
            time.sleep(1)
            
            print("drinking....")
            time.sleep(2)
            
            player.potion -= 1 
            player.health += 5
            
            print("You have been healed by 5!")
            time.sleep(2)
            
        elif main_question == "D" and player.potion <= 0:
            print("you have no potions")
            
            
       
        
    hub() 
   
game()















#me likey mc and cheese nigga













