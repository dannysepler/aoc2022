def solve(games):
    results = {
        "A X": 3 + 0,
        "B X": 1 + 0,
        "C X": 2 + 0,
        "A Y": 1 + 3,
        "B Y": 2 + 3,
        "C Y": 3 + 3,
        "A Z": 2 + 6,
        "B Z": 3 + 6,
        "C Z": 1 + 6,
    }
    return sum(results[game] for game in games)

import pytest

@pytest.mark.parametrize(
    "inputs, answer", [
        (("A Y", "B X", "C Z"), 12),
        (("A Z",), 8),
        (("C X",), 2),
        (("A Z", "C X"), 10),
        (("A Y",), 4)
    ]
)
def test_solve(inputs, answer):
    assert solve(inputs) == answer

with open("input.txt") as file:
    lines = [line.strip() for line in file]
    print(solve(lines))
