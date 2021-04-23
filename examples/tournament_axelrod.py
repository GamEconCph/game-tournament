import axelrod as axl
import numpy as np

players = [
    axl.Cooperator(),
    axl.Defector(),
    axl.TitForTat(),
    axl.Grudger(),
    axl.TitFor2Tats()
]

tournament = axl.Tournament(players)

results = tournament.play()