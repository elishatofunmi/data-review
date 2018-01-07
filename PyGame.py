from random import *

def stringCheck(string):
    if isinstance(string, (str)):
        pass

    else:
        raise ValueError
def IntCheck(integer):
    if isinstance(integer, (int)):
        return ''
    else:
        raise ValueError

def recursion(n):
    """recursive call function, it operates n times and returns a list.
    it is a recursive function that receives input  n times and appends all in input into a list
    and returns the list"""
    family = []
    if n >= 0:
        x = raw_input("Enter name of a member in your family: ")
        family.append(n) 
        n -= n
        recursion(n)
    else:
        return family

def pop_value(entry, value_type = int):
    list_return = entry
    for value in entry:
        if type(value) == str(value_type):
            list_return.pop(value_type)
        else:
            pass
    return list_return

def call_me_again(my_call):
    set_call = my_call
    call, me,value, game_on = ('', 0, '', '')
    while me:
        call = random.choice(my_call)
        value = raw_input("make your choice: ")
        if call == value:
            print "you are right"
            game_on = raw_input('do you want to play this game again: ')
            if game_on.lower() == 'yes':
                call_me_again(set_call) # recursion
            else:
                break
    return 0

class PyGame:
    def __init__(self):
        print "welcome to my PyGame "
        start = self.start
        stop = self.stop
        step = self.step
        sequence = self.seqence
        value = self.value
        self.x, self.y = ('', '')
        x = self.x
        y = self.y
        self.family_members= []
    
    def take_args(self, *args, **kwd):
        return "guess it will work"
    def Guess_my_number(self,start, stop, step):
        sequence = range(start, stop, step)
        value  = random.randrange()
        x = raw_input("Enter your number guess: ")

        if x == value:
            print "you are right"
            x = raw_input("Do you want to play this game again: ")
            if x.lower() == "yes":
                Guess_my_number(start, stop, step)
            else:
                pass
        elif x < value:
            print "value entered is less"
            x = raw_input("Do you want to play this game again: ")
            if x.lower() == "yes":
                Guess_my_number(start, stop, step)
            else:
                pass
        else:
            print 'value entered is more'
            x = raw_input("Do you want to play this game again: ")
            if x.lower() == "yes":
                Guess_my_number(start, stop, step)
            else:
                pass
        return 
    

    def Guess_family(self):
        my_family = self.my_family
        self.make_choice = ''
        make_choice = self.make_choice
        my_fam = []
        self.y = raw_input("how many family members do you have: ")
        if IntCheck(self.y) == '':
            my_fam = recursion(self.y)
            my_family= pop_value(my_fam, value_type = int)
            make_choice = random.choice(my_family)
            take_choice = raw_input("Guess family member\'s name: ")
            if make_choice == take_choice:
                print "you are right"
                play_again = raw_input("do you want to play the game again: ")
                if play_again.lower() == 'yes':
                    call_me_again(my_family)
                else:
                    pass
            else:
                print "you are wrong"
        else:
            self.Guess_family()
        Guess_family = staticmethod(Guess_family) # defining the function as a static method
        return 

    def random_pick(self,n):
        game_again = ''
        self.n = n
        self.random_value =list(raw_input("Enter your list of values: ")) # receives inputs as a list
        if len(self.random_value) > n:
            value =  random.sample(self.random_value, n)
            self.guess_n = list(raw_input("Guess random values: ")) 
            if value == self.guess_n:
                print "you are right"
                game_again = raw_input("do you want to play this game again: ")
                if game_again.lower() == 'yes':
                    self.random_pick(self.n)
                else:
                    pass

            else:
                print 'you are wrong'
                game_again = raw_input("do you want to play this game again: ")
                if game_again.lower() == 'yes':
                    self.random_pick(self.n)
                else:
                    pass
        else:
            raise Exception, "Values to select are more than what you can ever have"
        return
    
    def pick_rand(self, a,b):
        value = ''
        value = random.uniform(a,b)
        return value

        
            



        