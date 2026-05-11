import numpy as np
import matplotlib.pyplot as plt

# Size
size = 100
beta = 0.3
gamma = 0.05
time_steps = 100

# 0 = susceptible, 1 = infected, 2 = recovered
population = np.zeros((size, size), dtype=int)

# Initialize infection
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# 8 neighboring directions
neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]

# Arrays to record data for line plot
sus = []
inf = []
rec = []
steps = []

# Create a single figure with two subplots
plt.ion()  # Turn on interactive mode
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: grid simulation
ax1.axis('off')
im = ax1.imshow(population, cmap='viridis', vmin=0, vmax=2)
title1 = ax1.set_title(f'Spread Simulation | Step = 0')

# Right plot: real-time line chart
line_s, = ax2.plot([], [], label='Susceptible', color='blue')
line_i, = ax2.plot([], [], label='Infected', color='red')
line_r, = ax2.plot([], [], label='Recovered', color='green')
ax2.set_xlabel('Time Step')
ax2.set_ylabel('Count')
ax2.set_title('Epidemic Curve')
ax2.legend()
ax2.grid(True)

# Main simulation loop
for step in range(time_steps):
    new_pop = population.copy()
    infected_cells = np.argwhere(population == 1)
    
    # Update each infected cell
    for (i, j) in infected_cells:
        # Recovery process
        if np.random.rand() < gamma:
            new_pop[i, j] = 2
        
        # Infection spread
        for di, dj in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < size and 0 <= nj < size:
                if new_pop[ni, nj] == 0 and np.random.rand() < beta:
                    new_pop[ni, nj] = 1
    
    population = new_pop
    
    # Count numbers
    s_num = np.sum(population == 0)
    i_num = np.sum(population == 1)
    r_num = np.sum(population == 2)
    
    sus.append(s_num)
    inf.append(i_num)
    rec.append(r_num)
    steps.append(step)
    
    # Update both plots in real time
    im.set_data(population)
    title1.set_text(f'Spread Simulation | Step = {step}')
    
    line_s.set_data(steps, sus)
    line_i.set_data(steps, inf)
    line_r.set_data(steps, rec)
    
    ax2.relim()
    ax2.autoscale_view()
    
    plt.draw()
    plt.pause(0.05)  # Control animation speed

plt.ioff()
plt.show()