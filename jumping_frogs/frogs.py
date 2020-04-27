from itertools import permutations


def path_finder(graph, paths, goal):

    if not paths:
        return

    for path in paths:

        last = path[-1]

        if last == goal:
            yield path

        new_paths = []
        for neighbor in graph[last]:
            if neighbor != 'Game Over':
                new_paths.append(path + [neighbor])

        yield from path_finder(graph, new_paths, goal)


def mutate(swamp):
    lily = swamp.find('_')
    mutant_swamp = str()
    mutated_swamps = list()

    if lily - 1 > -1:
        if swamp[lily - 1] == 'R':

            for i, char in enumerate(swamp):
                if i == lily - 1:
                    mutant_swamp += '_'
                elif i == lily:
                    mutant_swamp += 'R'
                else:
                    mutant_swamp += char

            mutated_swamps.append(mutant_swamp)
            mutant_swamp = str()

    if lily - 2 > -1:
        if swamp[lily - 2] == 'R':

            for i, char in enumerate(swamp):
                if i == lily - 2:
                    mutant_swamp += '_'
                elif i == lily:
                    mutant_swamp += 'R'
                else:
                    mutant_swamp += char

            mutated_swamps.append(mutant_swamp)
            mutant_swamp = str()

    if lily + 1 <= len(swamp) - 1:
        if swamp[lily + 1] == 'L':

            for i, char in enumerate(swamp):
                if i == lily + 1:
                    mutant_swamp += '_'
                elif i == lily:
                    mutant_swamp += 'L'
                else:
                    mutant_swamp += char

            mutated_swamps.append(mutant_swamp)
            mutant_swamp = str()

    if lily + 2 <= len(swamp) - 1:
        if swamp[lily + 2] == 'L':

            for i, char in enumerate(swamp):
                if i == lily + 2:
                    mutant_swamp += '_'
                elif i == lily:
                    mutant_swamp += 'L'
                else:
                    mutant_swamp += char

            mutated_swamps.append(mutant_swamp)
            mutant_swamp = str()

    if mutated_swamps:
        return mutated_swamps
    else:
        return ['Game Over']


def frogs():
    frog_count = input('How many frogs on each side? ')
    assert frog_count.isnumeric(), 'Frog count must be an int.'

    initial_swamp = 'R' * int(frog_count) + '_' + 'L' * int(frog_count)
    final_swamp = 'L' * int(frog_count) + '_' + 'R' * int(frog_count)

    string_perms = [''.join(p) for p in permutations(initial_swamp)]
    swamp_states = {swamp: mutate(swamp) for swamp in string_perms}

    solutions = path_finder(swamp_states, [[initial_swamp]], final_swamp)

    for solution in solutions:
        for i, move in enumerate(solution):
            print(f'{i}. {move}')
        print('\nOR\n')


if __name__ == '__main__':
    frogs()
