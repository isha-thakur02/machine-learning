# pip install pygame==2.6.1

import gym
import numpy as np

# Environment initialization
env = gym.make('FrozenLake-v1', is_slippery=True, render_mode="human")

# Q-Table initialization
state_size = env.observation_space.n
action_size = env.action_space.n
Q = np.zeros((state_size, action_size))

# Hyperparameters
learning_rate = 0.8
discount_factor = 0.95
epsilon = 1.0
epsilon_decay = 0.99
min_epsilon = 0.01
episodes = 10000

# Training the Q-Learning model
for episode in range(episodes):
    state, _ = env.reset()
    done = False
    
    while not done:
        # Epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit
        
        next_state, reward, done, _, _ = env.step(action)
        
        # Update Q-Table
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + discount_factor * np.max(Q[next_state]) - Q[state, action]
        )
        state = next_state
    
    # Decay epsilon
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

# Testing the trained Q-Learning model
state, _ = env.reset()
done = False

print("Testing the trained model...")
while not done:
    action = np.argmax(Q[state])  # Choose the best action
    state, reward, done, _, _ = env.step(action)
    # Render each step
    env.render()
    if done:
        print(f"Game finished with reward: {reward}")
        break

env.close()
