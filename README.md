# Entropic Process Ontology: Simulation Framework

This repository contains the computational implementation supporting the manuscript:

**"Entropic Process Ontology: A Multi-Layered Model of Reality"**

---

## Overview

This project implements a minimal dynamical system to illustrate the core claims of entropic process ontology:

- Reality emerges as a dynamic process driven by entropy
- Observers act as projection functions over a shared state space
- Different observers produce structurally distinct representations of the same underlying system

This implementation serves as a computational illustration of the theoretical framework presented in the manuscript.

---

## Model Description

The system evolves according to:

x_{t+1} = F(x_t, E_t)

with:

F(x_t, E_t) = x_t + α · tanh(x_t) + ε_t

where:
- α = 0.1 (nonlinearity parameter)
- ε_t ~ N(0, σ²), σ = 0.05 (Gaussian noise)

---

## Observer Models

Three observer projections are implemented:

- **Observer 1 (Linear):** extracts dominant features
- **Observer 2 (Nonlinear):** applies nonlinear transformation
- **Observer 3 (Sparse):** selects partial information

These simulate different perceptual or measurement systems.

---

## Outputs

Running the simulation produces:

- observer_projections.png → panels (A–D)
- entropy_curve.png → panel (E)

These correspond to Figure 1 in the manuscript.

---

## How to Run

pip install -r requirements.txt  
python simulation.py

---

## Reproducibility

All results presented in the manuscript can be reproduced using the provided code.

- Random seed is fixed (seed = 42)
- Parameters are explicitly defined
- Figures are generated directly from the simulation script

---

## Repository Structure

entropic-process-ontology/

- simulation.py  
- README.md  
- requirements.txt  

- figures/  
  - observer_projections.png  
  - entropy_curve.png  

- supplementary/  
  - supplementary_material.pdf  

---

## Supplementary Material

supplementary/supplementary_material.pdf

---

## Limitations

This is a minimal illustrative model designed to demonstrate structural consistency rather than full physical realism.

---

## License

MIT License
