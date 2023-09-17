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

plt.figure(figsize=(8, 6))
plt.stem(np.unique(Z), z_Freq, markerfmt='ro', basefmt=' ', linefmt='k-')
plt.title('Stem Plot of Z = X - Y ')
plt.xlabel('Z (Difference of X and Y)')
plt.ylabel('Probability')
plt.xticks(np.arange(-5, 6))
plt.grid(True)
plt.savefig('../figs/Z.png')

print(z_Vals, ' , ', z_Freq)


