import numpy as np


class Player:
    def __init__(self, name):
        self.name = name  # used for printing
        self.i = np.nan  # player number, not assigned yet

    def __str__(self):
        return f"Player {self.i}: {self.name}"

    def play(self, state):
        # fill this out
        pass


# A game class for pure strategy games of complete and perfect information


class DiscreteGame:
    n = 2  # only for 2-player games

    def __init__(self, player1, player2, U1, U2, action_names=[]):
        """Matrix game
        player1, player2: player classes, must have method "play()"
        U1, U2: payoff matrices. Rows = # of actions of player 1,
                cols = # of actions of players 2
        action_names: [optional] (list of lists). A list of lists
            of names of actions, [iplayer, iaction].
        """

        assert U1.shape == U2.shape
        n_actions_player1, n_actions_player2 = U1.shape

        self.players = [player1, player2]

        self.name = f"{self.players[0].name} vs. {self.players[1].name}"

        # assign player number
        for i in [0, 1]:
            self.players[i].i = i

        self.state = dict()
        self.state["payoffs"] = [U1, U2]

        if action_names == []:
            action_names = [
                [
                    f"P{player_i+1}A{player_i_action+1}"
                    for player_i_action in range(U1.shape[player_i])
                ]
                for player_i in [0, 1]
            ]
        else:
            assert (
                len(action_names) == 2
            ), f"Must be one list of action names per player"
            assert (
                len(action_names[0]) == U1.shape[0]
            ), f"One name per action (player 1)"
            assert (
                len(action_names[1]) == U1.shape[1]
            ), f"One name per action (player 2)"

        self.state["actions"] = action_names

        self.history = []

    def flip_player_roles(self):
        """flip_player_roles: Makes the previous player 1 into player 2 and
        vice versa. Also resets the history of the game.
        """
        self.players.reverse()

        # update the player numbers
        for i in range(self.n):
            self.players[i].i = i

        self.name = f"{self.players[0].name} vs. {self.players[1].name}"

        # reset history
        self.history = []

    def payoffs(self, actions):

        pay = np.empty((self.n,))
        assert len(actions) == self.n

        actions_player1 = actions[0]
        actions_player2 = actions[1]

        for i in range(self.n):
            self.check_action(actions[i], i)
            U = self.state["payoffs"][i]
            pay[i] = U[actions_player1, actions_player2]

        return pay

    def check_action(self, action, i):
        U = self.state["payoffs"][i]
        n_actions_player_i = U.shape[i]

        if action in range(n_actions_player_i):
            return True
        else:
            return False

    def play_round(self, DOPRINT=False):
        """play_round: plays a single round of the game, storing actions in the history"""
        actions_played = np.zeros((self.n,), dtype="int")
        for i in range(self.n):
            action_index = self.players[i].play(self.state)
            if not self.check_action(action_index, i):
                j = 1 - i
                raise Exception(
                    f"{self.players[i].name} did something illegal (action_index={action_index}) and is disqualified! {self.players[j].name} wins!"
                )
            else:
                actions_played[i] = action_index

        if DOPRINT:
            u = self.payoffs(actions_played)
            for i in range(self.n):
                a_ = self.state["actions"][i][actions_played[i]]
                print(f"{self.players[i].name} played {a_} getting {u[i]}")

        self.history.append(actions_played)

    def compute_total_payoff_from_history(self, beta=1.0):
        """compute_total_payoff_from_history: uses the history of
        the game and computes total discounted sum of winnings
        """
        T = len(self.history)
        assert T > 0, f"History is empty!"
        payoffs = np.empty((T, self.n))
        for t, actions_played in enumerate(self.history):
            payoffs[t, :] = self.payoffs(actions_played) * beta ** t

        tot_winnings = payoffs.sum(0)

        return tot_winnings

    def declare_winner(self, T=1):
        """This might not make sense in a matrix game"""

        # reset any history
        self.history = []

        # play game T times with default coniguration
        for t in range(T):
            self.play_round()
        winnings1 = self.compute_total_payoff_from_history(beta=1.0)

        # flip roles of players and do the same
        self.flip_player_roles()

        for t in range(T):
            self.play_round()
        winnings2 = self.compute_total_payoff_from_history(beta=1.0)

        self.flip_player_roles()
        winnings2 = np.flip(winnings2)

        tot_winnings = winnings1 + winnings2

        # determine winner or if draw
        if tot_winnings[0] > tot_winnings[1]:
            print(f"{self.players[0].name} won!")
            return 0
        elif tot_winnings[0] < tot_winnings[1]:
            print(f"{self.players[1].name} won!")
            return 1
        elif tot_winnings[0] == tot_winnings[1]:
            print(f"Draw in {self.name}!")
            return -1
        else:
            # this should never happen! means the game has an error somehow
            raise Exception(
                f"Unexpected outcome for total winnings: {tot_winnings}! Maybe NaNs?"
            )
