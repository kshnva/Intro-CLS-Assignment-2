# Network-Based Epidemic Simulation Using Gillespie's Algorithm

Stochastic simulation of SIR and SIS epidemic models on various network topologies, developed for the Computational Life Sciences course at the University of Amsterdam.

## Overview

This project implements Gillespie's stochastic simulation algorithm to model the spread of infectious diseases over network structures. The simulations explore how network topology affects epidemic dynamics by comparing results across different graph models.

### Network Models

- Erdos-Renyi random graphs
- Watts-Strogatz small-world networks
- Barabasi-Albert scale-free networks
- Spatial networks

### Methods

- **Gillespie's Algorithm**: Exact stochastic simulation of SIR compartmental dynamics (Susceptible, Infected, Recovered)
- **Parameter sweeps**: Varying transmission rate (lambda), basic reproduction number (R0), initial infected nodes, and node centrality measures
- **Network analysis**: Degree distribution histograms for each network model

## Project Structure

```
├── Gillespies_Algorithm.py          # Core SIR stochastic simulation
├── networkmodels.py                 # Network generation utilities
├── Potesilova_15884392_Singha_15663388_assignment2.ipynb  # Main assignment notebook
├── spatial.ipynb                    # Spatial network experiments
├── transmission_network.csv         # Transmission data
└── *.pdf                            # Result plots
```

## Requirements

- Python 3
- NumPy
- Matplotlib
- NetworkX

## Usage

Run the main assignment notebook:

```bash
jupyter notebook Potesilova_15884392_Singha_15663388_assignment2.ipynb
```

Or run the standalone Gillespie simulation:

```bash
python Gillespies_Algorithm.py
```

## Authors

- Anezka Potesilova
- Kushnava Singha

University of Amsterdam, 2024
