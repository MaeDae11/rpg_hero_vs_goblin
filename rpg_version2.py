from time import sleep

def main():
    class Hero(object):
        def __init__(self):
            self.health= 10
            self.power = 5

        def attack(self, enemey):
            while enemey.health > 0 and hero.health> 0:
                print "You have %d health and %d power." % (self.health, self.power)
                print "The goblin has %d health and %d power." % (enemey.health, enemey.power)
                print "**********************"
                print "What do you want to do?\n\t1. fight goblin\n\t2. do nothing\n\t3. flee\n\t> "
                input = raw_input()
                if input == "1":
                    # Hero attacks goblin
                    print "Fighting!!"
                    print "  > . > --- +++    X . 0 "
                    sleep(2)
                    enemey.health = hero.alive(enemey)
                    print "You do %d damage to the goblin." % self.power
                    if enemey.health <= 0:
                        print "The goblin is dead."
                elif input == "2":
                    pass
                elif input == "3":
                    print "Goodbye."
                    break
                else:
                    print "Invalid input %r" % input

                if enemey.health > 0:
                    # Goblin attacks hero
                    self.health-= enemey.power
                    print "The goblin does %d damage to you." % enemey.power
                    if self.health<= 0:
                        print "You are dead."

        def alive(self, enemey):
            if self.health > 0:
                enemy.health -= self.power
                return enemey.health

            
    class Goblin(object):
        def __init__(self):
            self.health = 6
            self.power = 2

        def attack(self, hero):
            while self.health > 0 and hero.health> 0:
                print "You have %d health and %d power." % (self.health, self.power)
                print "The hero has %d health and %d power." % (hero.health, hero.power)
                print "**********************"
                print "What do you want to do?\n\t1. fight hero\n\t2. do nothing\n\t3. flee\n\t> "
                input = raw_input()
                if input == "1":

                    # goblin attacks hero
                    print "Fighting!!"
                    print "  > . > --- +++    X . 0 "
                    sleep(2)
                    hero.health-= self.power
                    print "You do %d damage to the hero." % self.power
                    if hero.health<= 0:
                        print "The hero is dead."
                elif input == "2":
                    pass
                elif input == "3":
                    print "Goodbye."
                    break
                else:
                    print "Invalid input %r" % input

                # hero attacks if goblin does nothing and if goblin attacks
                if self.health > 0:
                    # hero attacks goblin
                    self.health -= hero.power
                    print "The hero does %d damage to you." % hero.power
                    if self.health <= 0:
                        print "You are dead."
        
       


    # declaring hero_person is Hero()
    hero = Hero()
    # declaring goblin_person is Goblin()
    goblin = Goblin()


    # self      attacks     enemey
    hero.attack(goblin)

    # self        attacks     hero
    # goblin_person.attack(hero_person)

main()