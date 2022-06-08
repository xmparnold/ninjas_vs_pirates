from classes.ninja import Ninja
from classes.pirate import Pirate
import time
# import threading

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

class Game(Ninja, Pirate):

    current_tick = 0

    def __init__(self):
        # super().__init__(name)
        self.michelangelo = Ninja("Michelanglo")
        self.jack_sparrow = Pirate("Jack Sparrow")
        self.current_tick = 0

    def tick(self):
        time.sleep(.1)
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

option = input("Enter an option")

if(option == "1"):
    new_game = Game()
elif(option == "2"):
    print("Goodbye")

while(new_game.michelangelo.health > 0 and new_game.jack_sparrow.health > 0):
    # print("1)attack")
    # action = input("Enter your action")
    if(new_game.current_tick == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed != 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.tick()
    elif(new_game.current_tick % new_game.jack_sparrow.speed == 0 and new_game.current_tick % new_game.michelangelo.speed != 0):
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    else:
        new_game.tick()
    new_game.michelangelo.show_stats()
    new_game.jack_sparrow.show_stats()

if(new_game.michelangelo.health <= 0 and new_game.jack_sparrow.health > 0):
        print("Jack Sparrow is the winner.")
elif(new_game.jack_sparrow.health <= 0 and new_game.michelangelo.health > 0):
        print("Michaelangelo is the winner.")

print("1) Start new game")
print("2) Exit game")

option = input("Enter an option")