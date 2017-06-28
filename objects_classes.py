class Person(object):
    
    def __init__(self, name, email, phone):
        self.friends = []
        self.name = name
        self.email = email
        self.phone = phone
        self.greet_count = 0

    def add_friends(self, friend):
        # last friend in get attribute is default
        self.friends.append(getattr(friend, "name", friend))
        

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greet_count = self.greet_count + 1

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)
        print "Their friends are: %s" % self.friends

sonny = Person("Sonny", "sonny@hotmail.com", "482-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# sonny greets jordan
sonny.greet(jordan)
# jordan greets sonny
jordan.greet(sonny)
# add sonny to jordan's friends list
jordan.add_friends(sonny)
# add jordan to sonny's friend list
sonny.add_friends(jordan)
# prints entirtiy of contact information
sonny.print_contact_info()
# prints entirtiy of contact information
jordan.print_contact_info()
# length of jordans friends (how many people are his friends)
len(jordan.friends)
len(sonny.friends)

# class Vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print car.make
#         print car.model
#         print car.year

# car = Vehicle('Nissan', 'Leaf', 2015)

# car.print_info()



# counting number of times person is greeted
sonny.greet(jordan)
jordan.greet(sonny)
print sonny.greet_count
print jordan.greet_count
sonny.greet(jordan)
jordan.greet(sonny)
print sonny.greet_count
print jordan.greet_count