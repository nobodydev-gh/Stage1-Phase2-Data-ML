import numpy as np
import matplotlib.pyplot as plt



try:
    logo = np.load('/01_Numpy/data/numpy-logo.npy')

    #Display
    plt.figure(figsize=(10,5))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title("Numpy logo")
    plt.grid(False)

    dark_logo = 1 - logo

    plt.subplot(121)
    plt.imshow(dark_logo)
    plt.title("Numpy logo")
    plt.grid(False)
   


except FileNotFoundError:
        print("numpy logo file not found")