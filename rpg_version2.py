"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    class Hero(object):
        def __init__(self):
            self.hero_health = 10
            self.hero_power = 5
        def attack(self, enemey):
            while enemey.goblin_health > 0 and self.hero_health > 0:
                print "You have %d health and %d power." % (self.hero_health, self.hero_power)
                print "The goblin has %d health and %d power." % (enemey.goblin_health, enemey.goblin_power)
                print
                print "What do you want to do?"
                print "1. fight goblin"
                print "2. do nothing"
                print "3. flee"
                print "> ",
                input = raw_input()
                if input == "1":
                    # Hero attacks goblin
                    enemey.goblin_health -= self.hero_power
                    print "You do %d damage to the goblin." % self.hero_power
                    if enemey.goblin_health <= 0:
                        print "The goblin is dead."
                elif input == "2":
                    pass
                elif input == "3":
                    print "Goodbye."
                    break
                else:
                    print "Invalid input %r" % input

                if enemey.goblin_health > 0:
                    # Goblin attacks hero
                    self.hero_health -= enemey.goblin_power
                    print "The goblin does %d damage to you." % enemey.goblin_power
                    if self.hero_health <= 0:
                        print "You are dead."


            
    class Goblin(object):
        def __init__(self):
            self.goblin_health = 6
            self.goblin_power = 2

    # declaring hero_person is Hero()
    hero_person = Hero()
    goblin_person = Goblin()


    # self      attack     enemey
    hero_person.attack(goblin_person)

main()