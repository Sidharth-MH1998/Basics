import random

my_list=[10,20,30,40,50,55,95]

def generate_random():
    variable = random.random()  # Access the `random` method from the `random` module
    print(variable)             #Returns a random floating-point number between 0.0 and 1.0


def randint(a,b):
    variable=random.randint(a,b)
    print(variable)             #Returns a random variable between a and b


def uniform(a,b):
    variable=random.uniform(a,b)  ##Returns a floating point number between a and b
    print(variable)


def choice(name_of_list):
    variable=random.choice(name_of_list)    #Returns a random element from a non-empty sequence (like a list, tuple, or string).
    print(variable)


def sample(name_of_list,Number_of_sample):
    variable=random.sample(name_of_list,Number_of_sample)  #Returns a new list containing k unique random elements from the sequence.
    print (variable)                                        #sample number <= length of list
    

def shuffle(name_of_list):
    random.shuffle(name_of_list)        #Shuffles the elements of a sequence in place (modifies the original sequence).
    print (name_of_list)


def seed(seed_value):
    random.seed(seed_value)
    variable=random.randint(1,10)
    print (variable)


def gauss(mean,std):
    variable=random.gauss(mean,std)     #Generates a random number based on a Gaussian (normal) distribution with mean and standard deviation
    print(variable)

seed(12)
seed(1)
seed(58)
seed(12)