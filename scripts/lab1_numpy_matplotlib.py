import numpy as np

array = np.arange(1,101)

squard_array = array**2

mean = np.mean(squard_array)
sd = np.std(squard_array)

print(array)
print(squard_array)
print(mean)
print(sd)


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,101)

y = x**2

mean = np.mean(y)

plt.figure()

plt.plot(x,y,label="Squard Array")
plt.xlabel("Normal Array")
plt.ylabel("Squared Array")

plt.axhline(mean,linestyle="--",label =f"Mean is: {mean:.2f}")

plt.legend()
plt.show()
