import random

class Weapon:
    def __init__(self, name, damage, description):
        self.name = name
        self.damage = damage
        self.description = description

    def __str__(self):
        return f"{self.name} - Damage: {self.damage}\nDescription: {self.description}"


class Key:
    def __init__(self, name, description, door_type):
        self.name = name
        self.description = description
        self.door_type = door_type

    def __str__(self): 
        return f"{self.name}\nDescription: {self.description}"

class TEXTGAME:
    def __init__(self, player_name):
        self.Lives = 3
        self.player_name = player_name
        
        self.chosen_key = None
        self.chosen_weapon = None
        
        self.weapons =None
        self.keys = None 
    
    def SolveRiddle(self):
        Riddle_list ={
            "If an airplane crashed exactly on the border of the United States and Canada, how many people would you count if each survivor has 2 legs? If there are 4 survivors, what the total count of legs?": 8,

            "An orange has a diameter of 6 cm. If you cut it into 3 equal pieces, what is the total number of pieces you have?": 3 ,
            "A cowboy rides into town on Friday, stays for 3 days, and leaves on es on Friday. If you count the days he spent in town, what is the sum of the digits in that number?": 3,

            "What number do you get when you say 'silence and count the letters in it ?":7,
            "If a raspberry' contains 10 letters, how many letters are in the word 'berry'?": 5,
            "If a boy snowman has 2 features and a girl girl snowman has 3 features, what is the total number of features beturen them": 5,
            "You walk 1 mile south, 1 mile east, and then 1 mile north. How many miles did you walk in total": 3,
            "In a relationship, if one person has 2 hands and the other has 2 hands, how many hands are there in total?":4
        }
        random_riddle_question = random.choice(list(Riddle_list.keys()))
        random_riddle_answer = int(Riddle_list[random_riddle_question])
        print(random_riddle_question)
        try:
            Answer = int(input("Enter the answer in numbers "))
            if Answer == random_riddle_answer:
                return True
            return False
        
        except(IndexError,ValueError):
            print("Invalid answer, please give correct answer")

    def choose_weapon(self):
        self.weapons = [
            Weapon("Sword of Destiny", 10, "A gleaming sword that shines with a mysterious light."),
            Weapon ("Axe of the Ancients", 12,"A heavy axe that can cleave through armor."),
            Weapon("Bow of Shadows", 8,"A silent bow that strikes from the darkness."),
        ]
        print("Pick up any and one Weapon you wanted from the store")
        
        for idx, weapon in enumerate(self.weapons, start=1):
            print(f"{idx}. {weapon}")
        choice = input("Enter the number of your choice:")
        
        try:
            self.chosen_weapon = self.weapons[int(choice) - 1]
            print(f"\nYour have choden: {self.chosen_weapon.name}!")
            print("Prepare for your adventure with this powerful weapon!")
        except(IndexError,ValueError):
            print("Invalid choice. Please choose a valid weapon number.")
            
    def choose_key(self):
        self.keys = [
            Key("Golden Key", "A shimmering key that unlocks the treasures of the ancient vault.", "golden door"),
            Key("Rusty Key", "An old, rusty key that seems to unlock something long forgotten.", "rusty door"),
            Key("Iron Key", "A sturdy key, reliable and strong, made for heavy locks.","iron door")        
        ]
        print("Choose your key:")
        
        for idx, key in enumerate(self.keys, start=1):
            print(f"{idx}. {key}")
        choice = input("Enter the number of your choice: ")
        
        try:
            self.chosen_key = self.keys[int(choice) - 1]
            print(f"\nYou have chosen: {self.chosen_key.name}!")
            print(f"This key can open: {self.chosen_key.door_type}.")
        except (IndexError, ValueError):
            print("Invalid choice. Please choose a valid key number.")
    
    
    def first_level(self):
        print(f"{self.player_name} Your Total Lives: {self.Lives}")
        print("The game is begin !!!!!")
        ##----------------------------------------------------------------FIRST LEVEL
        print(f"{self.player_name} Answer the riddle ")
        while (self.Lives > 0):
            if self.SolveRiddle() is True:
                print(f"Great you completed the task {self.player_name}!!!!")
                break
            else:
                print("You lost one lives")
                self.Lives = 1
                print(f"{self.player_name} lives left: {self.Lives}")

        if self.Lives > 0:
            print("                                 COMPLETED ONE riddle")
        else:
            print("GAME OVER")
            query = input("If you want to restart the game (y/n)") 
            if query.lower() == 'y':
                self.StartGame()
            else:
                return False
        #---------------------------------------------------------------------------------------------------------------------------------------
        self.choose_weapon ()
        self.choose_key()
        while True:
            if self.chosen_key.name == "Golden Key":
                print("The door opens with a click! You have successfully unlocked the golden door!") 
                break # Exit the loop if the correct key is chosen
            else:
                print(f"This key cannot open the door. You chose: {self.chosen_key.door_type}.")
                print("WARNING!!! Please choose another key.")
                self.choose_key()
        return True
    
    def check_weapon(self):
        correct_weapon = "Sword of Destiny"  # Example of the correct weapon
        
        while self.chosen_weapon.name != correct_weapon:
            print(f"\nThe {self.chosen_weapon.name} is not the right weapon to defeat this villain!")
            print("You need to choose another weapon.")
            self.choose_weapon()  # Redirect the player to choose the weapon again
        
        print(f"Great! The {self.chosen_weapon.name} is the right weapon to defeat the villain.")
        return True
    
    def fight_villain(self):
        villain_health = 20
        print("\nYou encounter a fearsome villain!")
        print(f"Villain's Health: {villain_health}")
        print(f"{self.player_name}, you are armed with: {self.chosen_weapon.name} (Damage: {self.chosen_weapon.damage})")

        # Check if the player has the correct weapon
        self.check_weapon()  
        

        while villain_health > 0 and self.Lives > 0:
            print("\nYou attack the villain...")
            hit_chance = random.randint(0, 1)  # 50% chance to hit
            
            if hit_chance == 1:
                print(f"Success! You deal {self.chosen_weapon.damage} damage to the villain.")
                villain_health -= self.chosen_weapon.damage
            else:
                print("Your attack missed!")
            
            if villain_health <= 0:
                print("You defeated the villain!")
                break
            
            # Villain attacks back
            print("The villain strikes back!")
            villain_damage = random.randint(1, 5)
            self.Lives -= 1
            print(f"The villain hits you for {villain_damage} damage. Lives left: {self.Lives}")

            if self.Lives <= 0:
                print("You were defeated by the villain...")
                break

        if villain_health <= 0:
            print("CONGRATULATIONS! You won the battle!")
        elif self.Lives <= 0:
            print("GAME OVER.")

    def second_level(self):
        print("                             CONGRATULATIONS NOW THE 2ND LEVEL STARTED")
        if self.Lives<3:
            self.Lives+=1
        
        print(f"{self.player_name}, you have {self.Lives} lives. Prepare for battle!")
        self.fight_villain()             
        
        print(f"{self.player_name} Answer the riddle ")
        while (self.Lives > 0):
            if self.SolveRiddle() is True:
                print(f"Great you completed the task {self.player_name}!!!!")
                break
            else:
                print("You lost one lives")
                self.Lives = 1
                print(f"{self.player_name} lives left: {self.Lives}")

        if self.Lives > 0:
            print("                                 COMPLETED ONE riddle")
        else:
            print("GAME OVER")
            query = input("If you want to restart the game (y/n)") 
            if query.lower() == 'y':
                self.StartGame()
            else:
                return False

    def StartGame(self):
        first_level = self.first_level()

        if first_level:
            self.second_level()


if __name__ == "__main__":

    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to visit Paris.")
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's start with your name: ")
    player_name = input()
    print("Good luck, " + player_name + ".")

    obj = TEXTGAME(player_name)
    obj.StartGame()