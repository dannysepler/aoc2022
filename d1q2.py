def solve(inputs):
    elves = []
    curr = 0
    for weight in inputs:
        if weight == "":
            elves.append(curr)
            curr = 0
        else:
            curr += int(weight)
    elves.append(curr)
    elves.sort()
    return elves[-1] + elves[-2] + elves[-3]

import pytest

@pytest.mark.parametrize(
    "inputs, answer", [
        (("1", "2", "", "5", "", "3"), 11),
        (("1", "2", "", "5", "7", "", "3"), 18),
    ]
)
def test_solve(inputs, answer):
    assert solve(inputs) == answer

with open("input.txt") as file:
    weights = [line.rstrip() for line in file]
    print(solve(weights))
