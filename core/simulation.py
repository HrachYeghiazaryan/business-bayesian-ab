import numpy as np

def simulate(algorithm, bandit_probabilities, bandit_rewards, num_experiments=10000):
    """
    Simulates the usage of algorithm.

    Parameters
    ----------
    algorithm : EpsilonGreedy
        
    bandit_probabilities : array_like
        
    bandit_rewards : array_like
        
    num_experiments : int
         (Default value = 10000)

    Returns
    -------

    """
    for _ in range(num_experiments):
        selected_bandit = algorithm.infer_bandit()
        randnum = np.random.random()
        if randnum<bandit_probabilities[selected_bandit]:
            reward = bandit_rewards[selected_bandit]
        else:
            reward = 0
        algorithm.update_results(selected_bandit, reward)
    return algorithm