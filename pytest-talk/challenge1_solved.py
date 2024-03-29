# TDD approach to solving day 1 of AoC 2022
# See https://adventofcode.com/2022/day/1

"""Problem breakdown.
Let's first think of the algorithm or approach we need to solve this problem. Again, one of the benefits(or curse) of TDD is that it prompts the programmer to think about the problem first, instead of coding straight ahead. Some times this approach is sensible, some times it is not, exercise your judgement.

1. We need to parse a multiline string.
2. Obtain a list of the strings.
3. Iterate until a space is found and sum all values, store those values.
3. Sum each list
4. Check which one is the largest.

We have the problem solution for the test set, so we can even assert that the fourth elf with 24000 calories is the one with the highest value.

Hint 1. Use string.splitlines() method.
Hint 2. Create accumulators and initializers
Hint 3. Transform string to int to be able to do sum, for loop.

"""

problem_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

calories = problem_input.splitlines()
assert isinstance(calories, list)

sum = 0
calories_carried_by_elf = []

calories.append("")
# Appending as a trick to make sure the the for loop captures all input. Show how it fails and then what you need to fix. Without the extra space, it doesn't take all the necessary input.

for pack in calories:
    if pack not in [""]:
        pack = int(pack)
        assert isinstance(pack, int)

        sum += pack

    if pack in [""]:
        calories_carried_by_elf.append(sum)
        sum = 0

assert len(calories_carried_by_elf) == 5
assert max(calories_carried_by_elf) == 24000
assert calories_carried_by_elf.index(max(calories_carried_by_elf)) == 3
