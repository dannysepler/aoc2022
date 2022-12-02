def solve(inputs):
    answer, curr = 0, 0
    for weight in inputs:
        if weight == "":
            curr = 0
        else:
            curr += int(weight)
            answer = max(curr, answer)
    return answer

import pytest

@pytest.mark.parametrize(
    "inputs, answer", [
        (("1", "2", "", "5"), 5),
        (("1", "2", "3", "", "5"), 6),
    ]
)
def test_solve(inputs, answer):
    assert solve(inputs) == answer

with open("input.txt") as file:
    weights = [line.rstrip() for line in file]
    print(solve(weights))
