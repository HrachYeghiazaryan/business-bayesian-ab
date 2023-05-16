import numpy as np
import pandas as pd
import datetime

class EpsilonGreedy():
    def __init__(self, epsilon_function, num_bandits):
        self.epsilon = epsilon_function
        self.bandit_list = [i for i in range(num_bandits)]
        self.bandit_experiment_numbers = [0]*num_bandits
        self.bandit_expectations = [0]*num_bandits
        self.creation_moment = datetime.datetime.now().replace(microsecond=0).strftime('%d-%B-%Y %H:%M')
        self.last_update_moment = datetime.datetime.now().replace(microsecond=0).strftime('%d-%B-%Y %H:%M')
        self.df = pd.DataFrame({'experiment_number': [], 'bandit': [], 'reward': [], 'datetime': []})

    def __repr__(self):
        """
        A description for the class.     
        """
        return 'A complete class to run Epsilon Greedy algorithm'

    @property
    def num_explorations(self):
        """ 
        Number of overall experiments performed.
        """
        return len(self.df)

    def infer_bandit(self):
        """ 
        Returns
        -------
        The next bandit to perform experiment on.
        """
        current_epsilon = self.epsilon(self.num_explorations+1)
        randnum = np.random.random()
        if randnum<current_epsilon:
            return np.random.choice(self.bandit_list)
        else:
            return np.argmax(self.bandit_expectations)
        
    def update_results(self, bandit, reward):
        """
        Updates the experiments data for the class based on passed information.

        Parameters
        ----------
        bandit : int
            
        reward : float
        """
        self.last_update_moment = datetime.datetime.now().replace(microsecond=0).strftime('%d-%B-%Y %H:%M')
        self.df.loc[self.num_explorations] = [self.num_explorations+1, bandit, reward, self.last_update_moment]
        self.bandit_experiment_numbers[bandit] += 1
        if self.bandit_experiment_numbers[bandit]==1:
            self.bandit_expectations[bandit] += reward
        else:
            self.bandit_expectations[bandit] = ((self.bandit_expectations[bandit]*(self.bandit_experiment_numbers[bandit]-1)) + reward)/self.bandit_experiment_numbers[bandit]

    def write_results(self, path, format):
        """
        Writes the results of all recorded experiments.

        Parameters
        ----------
        path : str
            
        format : str

        """
        if format=='csv':
            self.df.to_csv(path, index=False)
        elif format=='parquet':
            self.df.to_parquet(path, index=False)
        else:
            raise Exception(f'Please specify a supported format, one of ["csv","parquet"]. You specified {format}')

    def report(self, show_top=5):
        """
        Prints the statistics for the results of the experiments.

        Parameters
        ----------
        show_top : int
             (Default value = 5)

        """
        bandit_df = pd.DataFrame({'bandit': self.bandit_list, 'exp_reward': self.bandit_expectations, 'experiment_num': self.bandit_experiment_numbers})
        bandit_df = bandit_df.sort_values(by='exp_reward', ascending=False)
        print('Summary of Epsilon Greedy Results')
        print('=================================')
        print('>>>General information')
        print(f'Class creation moment:             {self.creation_moment}')
        print(f'Last update moment:                {self.last_update_moment}')
        print('Number of experiments:',' '*(28-len(str(self.num_explorations))),f'{self.num_explorations}')
        print('Number of bandits:', ' '*(33-len(str(self.num_explorations))), f'{len(self.bandit_list)}')
        print('=================================')
        print(f'>>>Statistics on top {show_top} bandits')
        print(f'Rank        Bandit        Expected Reward        Number of Experiments')
        for i in range(min(show_top, len(self.bandit_list))):
            cur_row = bandit_df.iloc[i,:].tolist()
            print(f' {i+1}', ' '*(11-len(str(i+1))) ,f'{int(cur_row[0])}',' '*int(np.ceil((33-len(str(cur_row[1])))/2)),f'{cur_row[1]}',' '*int(np.floor((43-len(str(cur_row[1])))/2)),f'{int(cur_row[2])}')