# business_bayesian_ab

A package for running Bayesian A/B testing in business environment.

### Features

- Epsilon greedy algorithm usage.
- Simulating the business environment.
- Plotting the performance cumulative average.

### Usage

```
from business_bayesian_ab.core.algorithms import EpsilonGreedy

eps = EpsilonGreedy(epsilon_function=lambda x: 1/np.sqrt(x), num_bandits=4)
eps_fit = test_function(algorithm=eps, bandit_probabilities=[0.1,0.6,0.4,0.25], bandit_rewards=[6,9,1,3])
eps_fit.report()

```
