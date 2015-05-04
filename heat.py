import numpy as np
import matplotlib.pyplot as plt

N = 25
image = np.zeros((N,N))
buffer = np.zeros((N,N))

for i in range(1,N-1):
    image[i,N-1] = i * (N-1-i)


for t in range(5*N):
    for i in range (1,N-1):
        for j in range(1,N-1):
            buffer[i,j] = (image[i-1,j]+image[i+1,j] + image[i,j-1] + image[i,j+1])/4.0

    for i in range(1,N-1):
        for j in range(1,N-1):
            image[i,j] = buffer[i,j]

fig, ax = plt.subplots()
ax.imshow(image, cmap=plt.cm.gray, interpolation = 'nearest')

plt.savefig("heatflow.pdf", format = "pdf")
plt.show()
