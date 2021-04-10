import numpy as np
import copy


def find_undominated_actions(U_in, i, A, DOPRINT=False):
    """find_undominated_actions: finds the actions for player i that are
    not strictly dominated by another action

    INPUTS:
        U_in: (matrix, na1*na2) Payoffs (player 1, player 2)
        i: (integer) Which player we are currently examining
        A: (list) List of actions (len = # of actions for this player)

    OUTPUT:
        AA: (list) undominated actions
        IA: (list of integers) integers i s.t. AA = [A[i] for i in IA]
        ANYDOMINATED: (bool) True if at least one action was strictly dominated
    """

    AA = []
    IA = []
    nA = len(A)

    # 1. ensure that U has actions of player i along 0th dimension
    if i == 0:
        # 1.a already the case
        U = np.copy(U_in)
    else:
        # 1.b transpose
        U = U_in.T

    # 2. determine if each action has other dominated actions
    for ia in range(nA):
        DOMINATED = False

        for ia_ in range(nA):
            # 2.a loop through all *other* strategies
            if ia_ == ia:
                continue

            # 2.b check if ia_ always gives a higher payoff than ia (i.e. domination)
            if np.all(U[ia_] > U[ia]):
                DOMINATED = True
                break  # exit search: enough that we have found one

        # 2.c append or not
        if DOMINATED:
            if DOPRINT:
                print(f"Player {i+1}: {A[ia]} is dominated by {A[ia_]}")
        else:
            AA.append(A[ia])
            IA.append(ia)

    # 3. convenient boolean
    ANYDOMINATED = len(AA) < len(A)

    return AA, IA, ANYDOMINATED


def IESDS(A, U, DOPRINT=False, maxit=10000):
    """Iterated Elimination of Strictly Dominated Strategies
    INPUTS:
        A: (list of lists) n lists (one for each player),
                each has len = # of actions to player i
        U: (list, len=n) list of na1*na2 matrices of payoffs
        DOPRINT: (bool) whether to print output to terminal
        maxit: (int) break algorithm if this count is ever reached
    OUTPUT: Actions and payoffs for the undominated game
        A_undominated: (n-list of vectors)
        U_undominated: (n-list of matrices of payoffs)
    """

    U_undominated = copy.copy(U)
    A_undominated = copy.copy(A)

    n = len(U)
    na1, na2 = U[0].shape

    # checks
    assert len(A) == n
    for i in range(n):
        assert len(A[i]) == U[i].shape[i]
        assert U[i].shape == (
            na1,
            na2,
        ), f"Payoff matrix for player {i+1} is {U[i].shape}, but {(na1,na2)} for player 1"

    # initialize flags
    D = np.ones((n,), dtype="bool")

    for it in range(maxit):

        for i in range(n):
            # find undominated actions
            A_undominated[i], IA, D[i] = find_undominated_actions(
                U_undominated[i], i, A_undominated[i], DOPRINT
            )

            # if we found at least one, remove it/them from the game
            if D[i]:
                # remove from both players' payoff matrices
                for j in range(n):
                    if i == 0:
                        U_undominated[j] = U_undominated[j][IA, :]
                    elif i == 1:
                        U_undominated[j] = U_undominated[j][:, IA]
                    else:
                        raise Exception(f"Code only implemented for 2-player games")

        # break once we have run an iteration without finding any strategies to remove
        if D.any() == False:
            break

    return A_undominated, U_undominated


class player:
    def __init__(self, name="Player1"):
        self.name = name  # used for printing
        self.i = np.nan  # player number, not assigned yet

    def __str__(self):
        return f"Player {self.i}: {self.name}"

    def play(self, state, DOPRINT=False):
        i = self.i
        j = 1 - i  # opponent

        # 0. unpack state variables
        U = state["payoffs"]
        A = state["actions"]

        # 1. perform IESDS on the game
        A_undominated, U_undominated = IESDS(A, U, DOPRINT)

        # 2. select random action from surviving set of players actions
        action_choice = np.random.choice(A_undominated[i])

        # 3. find the index in the *original* strategy set
        for action_index, a in enumerate(A[i]):
            if a == action_choice:
                break

        return action_index