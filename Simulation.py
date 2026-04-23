# ============================================================
# Entropic Process Ontology - Simulation Framework (Final)
# Author: Atakan Akbulut
# ============================================================

"""
This simulation implements a minimal entropic dynamical system
to illustrate observer-dependent projections in a shared state space.

It supports the theoretical framework proposed in:
"Entropic Process Ontology: A Multi-Layered Model of Reality"
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# -------------------------------
# 1. SYSTEM PARAMETERS
# -------------------------------
DIM = 10            # state dimension
T = 200             # number of time steps
ALPHA = 0.1         # nonlinearity strength
SIGMA = 0.05        # Gaussian noise standard deviation

np.random.seed(42)

# -------------------------------
# 2. DIRECTORY SETUP
# -------------------------------
os.makedirs("figures", exist_ok=True)
os.makedirs("results", exist_ok=True)

# -------------------------------
# 3. INITIAL STATE
# -------------------------------
x = np.random.uniform(-1, 1, size=DIM)
trajectory = [x.copy()]

# -------------------------------
# 4. DYNAMICAL SYSTEM
# x_{t+1} = x_t + α·tanh(x_t) + ε_t
# -------------------------------
def evolve(x):
    interaction = np.tanh(x)
    noise = np.random.normal(0, SIGMA, size=DIM)
    return x + ALPHA * interaction + noise

# -------------------------------
# 5. OBSERVER DEFINITIONS
# -------------------------------
def observer_linear(x):
    """Observer 1: Linear projection"""
    return x[:3]

def observer_nonlinear(x):
    """Observer 2: Nonlinear transformation"""
    return np.sin(x[:3] * 2)

def observer_sparse(x):
    """Observer 3: Sparse selective perception"""
    return x[[0, 3, 6]]

# -------------------------------
# 6. ENTROPY FUNCTION
# -------------------------------
def compute_entropy(data, bins=20):
    hist, _ = np.histogram(data, bins=bins, density=True)
    hist = hist + 1e-12  # avoid log(0)
    return -np.sum(hist * np.log(hist))

# -------------------------------
# 7. SIMULATION LOOP
# -------------------------------
obs1_list, obs2_list, obs3_list = [], [], []
entropy_list = []

for t in range(T):
    x = evolve(x)
    trajectory.append(x.copy())

    o1 = observer_linear(x)
    o2 = observer_nonlinear(x)
    o3 = observer_sparse(x)

    obs1_list.append(o1)
    obs2_list.append(o2)
    obs3_list.append(o3)

    entropy_list.append(compute_entropy(x))

trajectory = np.array(trajectory)
obs1 = np.array(obs1_list)
obs2 = np.array(obs2_list)
obs3 = np.array(obs3_list)

# -------------------------------
# 8. PLOTTING (FIGURE 1)
# -------------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# (A) State evolution
axs[0, 0].plot(trajectory[:, :3])
axs[0, 0].set_title("State Evolution (First 3 Dimensions)")
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("State Value")

# (B) Observer 1
axs[0, 1].plot(obs1)
axs[0, 1].set_title("Observer 1 (Linear)")

# (C) Observer 2
axs[1, 0].plot(obs2)
axs[1, 0].set_title("Observer 2 (Nonlinear)")

# (D) Observer 3
axs[1, 1].plot(obs3)
axs[1, 1].set_title("Observer 3 (Sparse)")

plt.tight_layout()
plt.savefig("figures/observer_projections.png", dpi=300)
plt.close()

# -------------------------------
# 9. ENTROPY PLOT
# -------------------------------
plt.figure(figsize=(6, 4))
plt.plot(entropy_list)
plt.title("Entropy Over Time")
plt.xlabel("Time")
plt.ylabel("Entropy")
plt.tight_layout()
plt.savefig("figures/entropy_curve.png", dpi=300)
plt.close()

# -------------------------------
# 10. QUANTITATIVE COMPARISON
# -------------------------------
def mean_distance(a, b):
    return np.mean(np.linalg.norm(a - b, axis=1))

d12 = mean_distance(obs1, obs2)
d13 = mean_distance(obs1, obs3)
d23 = mean_distance(obs2, obs3)

print("\n--- Quantitative Observer Differences ---")
print(f"Observer1 vs Observer2: {d12:.4f}")
print(f"Observer1 vs Observer3: {d13:.4f}")
print(f"Observer2 vs Observer3: {d23:.4f}")

# Save results
with open("results/quantitative_results.txt", "w") as f:
    f.write("Observer Differences:\n")
    f.write(f"O1-O2: {d12:.4f}\n")
    f.write(f"O1-O3: {d13:.4f}\n")
    f.write(f"O2-O3: {d23:.4f}\n")

print("\nSimulation complete. Figures saved in 'figures/' directory.")