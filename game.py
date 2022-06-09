# imports
from classes.ninja import Ninja
from classes.pirate import Pirate
import time
# import threading

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

class Game(Ninja, Pirate):
    # creating an attribute to hold the current tick of the game clock
    current_tick = 0

    def __init__(self):
        # super().__init__(name)
        self.michelangelo = Ninja("Michelanglo")
        self.jack_sparrow = Pirate("Jack Sparrow")
        self.current_tick = 0

    # define tick function to add tick to game clock and sleep for given sleep rate
    def tick(self):
        # sleep for given number of seconds
        time.sleep(.1)
        # increment current tick of current instance of Game class
        self.current_tick += 1

# class myThread(threading.Thread):
#     def __init__(self, thread_ID, name, counter):
#         threading.Thread.__init__(self)
#         self.thread_ID = thread_ID
#         self.name = name
#         self.counter = counter
    
#     def run(self):
#         print("Staring " + self.name)
#         threadLock.acquire()
#         count -= 1
        
# threadLock = threading.Lock()
# threads = []
print("1) Start new game")
print("2) Exit game")

# take input from player to start
option = input("Enter an option")
# check input for type and either start game or exit
if(option == "1"):
    new_game = Game() # start new instance of game
elif(option == "2"):
    print("Goodbye") # say goodbye to user if they select to exit

# checking to make sure both characters are not dead
while(new_game.michelangelo.health > 0 and new_game.jack_sparrow.health > 0):
    # print("1)attack")
    # action = input("Enter your action")
    # if current tick is 0, both players attack each other because there is no cooldown
    if(new_game.current_tick == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    # check modulas of current tick divided by character's speed attribute and if both are divisible with 0 remainder, both attack
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    # if just michaelangelo is divisible, he attacks
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed != 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.tick()
    # if just jack sparrow is divisible, he attacks
    elif(new_game.current_tick % new_game.jack_sparrow.speed == 0 and new_game.current_tick % new_game.michelangelo.speed != 0):
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    # if none are true, we will just tick and go back to beginning of loop
    else:
        new_game.tick()
    # print stats of both characters after each time the loop runs to show current health
    new_game.michelangelo.show_stats()
    new_game.jack_sparrow.show_stats()

if(new_game.michelangelo.health <= 0 and new_game.jack_sparrow.health > 0):
        print("Jack Sparrow is the winner.")
elif(new_game.jack_sparrow.health <= 0 and new_game.michelangelo.health > 0):
        print("Michaelangelo is the winner.")

print("1) Start new game")
print("2) Exit game")

option = input("Enter an option")