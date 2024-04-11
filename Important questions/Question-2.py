'''
Mode
'''
from statistics import mode

def compute_mode(data):
        return mode(data)

animal = ['cat', 'tiger', 'dog', 'cat', 'lion', 'dog', 'cat', 'dog', 'cat', 'cow', 'cat', 'tiger', 'lion']

mode_animal = compute_mode(animal)
print("The mode of the animal dataset is:", mode_animal)

'''
The mode of the animal dataset is: cat
'''