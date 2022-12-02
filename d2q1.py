def solve(games):
    score = 0
    mult = {
        # rock
        "X": 1,
        "A": 1,
        # paper
        "Y": 2,
        "B": 2,
        # scissors
        "Z": 3,
        "C": 3,
    }
    for game in games:
        theirs, ours = game.split(" ")
        score += mult[ours]
        if mult[ours] == mult[theirs]:
            score += 3
        elif mult[ours] == mult[theirs] + 1 or mult[ours] == mult[theirs] - 2:
            score += 6
    return score

import pytest

@pytest.mark.parametrize(
    "inputs, answer", [
        (("A Y", "B X", "C Z"), 15),
        (("A Z",), 3),
        (("C X",), 7),
    ]
)
def test_solve(inputs, answer):
    assert solve(inputs) == answer

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    print(solve(lines))
