import numpy as np
import matplotlib.pyplot as plt

def diceRoll():
    dice = np.array(np.random.randint(1, 7, size = 1000000))
    return dice

X = diceRoll()
Y = diceRoll()

Z = X-Y

z_Vals, z_Freq = np.unique(Z, return_counts = True)
z_Freq = z_Freq/1000000

print(z_Vals, ' , ', z_Freq)


