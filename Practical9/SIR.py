import numpy as np
import matplotlib.pyplot as plt

N=10000
beta=0.3
gamma=0.05
time_steps=1000

I=1
R=0
S=N-I-R
S_list=[S]
I_list=[I]
R_list=[R]
for i in range(time_steps):
    infection_probability = beta * (I / N)
    new_infected = np.random.binomial(S, infection_probability)
    new_recovered = np.random.binomial(I, gamma)
    # Update
    S -= new_infected      
    R += new_recovered     
    I = I + new_infected - new_recovered 
    # Save
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Simple SIR Model')
plt.legend()
plt.savefig('SIR.png')
plt.show()