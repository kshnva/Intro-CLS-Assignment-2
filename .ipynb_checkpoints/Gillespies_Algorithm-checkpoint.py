import numpy as np
import matplotlib.pyplot as plt

def process_probabilities(state, params):
    S, I, R = state['S'], state['I'], state['R']
    a = np.zeros(2)   
    a[0] = params['beta'] * S * I 
    a[1] = params['gamma'] * I   
    return a

def process(probs):
    r = np.random.random() * sum(probs)
    which = 0
    cumulative_sum = probs[0]    
    while r > cumulative_sum:
        which += 1
        cumulative_sum += probs[which]
    return which + 1

def plot_results(meanTime, meanS, meanI, meanR):
    plt.figure(figsize=(10, 6))      
    plt.plot(meanTime, meanS, label='Susceptible', linestyle='-')
    plt.plot(meanTime, meanI, label='Infected', linestyle='-')
    plt.plot(meanTime, meanR, label='Recovered', linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.title('Mean SIR Model Simulation (No Deaths)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def SIR_stoch(params, initial, end_time):

    state = initial.copy()
    time = 0
    result = {'time': [], 'S': [], 'I': [], 'R': []}
    while time < end_time and state['I'] > 0:
        
        probs = process_probabilities(state, params)
        tau = (1 / sum(probs)) * np.log(1 / np.random.random())
        time += tau
        which = process(probs)

        if which == 1:
            state['S'] -= 1  # infection
            state['I'] += 1
        elif which == 2:
            state['I'] -= 1  # recovery
            state['R'] += 1

        result['time'].append(time)
        result['S'].append(state['S'])
        result['I'].append(state['I'])
        result['R'].append(state['R'])    
    return result


def SIR_stoch_run():

    params = {
        'beta': 0.3,  
        'gamma': 0.1    
    }
    initial = {
        'S': 99,     
        'I': 1,     
        'R': 0      
    }
    
    end_time = 50  # end of simulation time span starting at 0
    run_count = 50 # number of runs

    result = {'time': [], 'S': [], 'I': [], 'R': []}

    for n in range(run_count):
        out = SIR_stoch(params, initial, end_time)
        result['time'].extend(out['time'])
        result['S'].extend(out['S'])
        result['I'].extend(out['I'])
        result['R'].extend(out['R'])
    
    #Extract all the unique time points from the simulations 
    time, unique_indices = np.unique(result['time'], return_index=True)
    S = np.array(result['S'])[unique_indices]
    I = np.array(result['I'])[unique_indices]
    R = np.array(result['R'])[unique_indices]

    #Calculate moving averages of the State Variables  
    N = 20
    meanTime, meanS, meanI, meanR = [], [], [], []
    for i in range(0, len(time) - N + 1, N):
        meanTime.append(np.mean(time[i:i+N]))
        meanS.append(np.mean(S[i:i+N]))
        meanI.append(np.mean(I[i:i+N]))
        meanR.append(np.mean(R[i:i+N]))    
    plot_results(meanTime, meanS, meanI, meanR)

SIR_stoch_run()
