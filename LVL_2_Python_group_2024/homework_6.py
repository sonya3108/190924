# 1
def count_states(file_name):
    candidate_states = {}

    with open(file_name, 'r') as file:
        for line in file:
            candidate, _ = line.split()
            if candidate in candidate_states:
                candidate_states[candidate] += 1
            else:
                candidate_states[candidate] = 1

    return candidate_states

file_name = "C:/Users/Admin/Desktop/190924/LVL_2_Python_group_2024/input.txt"
result = count_states(file_name)
print(result)

# 2
def total_votes(file_name):
    candidate_votes = {}

    with open(file_name, 'r') as file:
        for line in file:
            candidate, votes = line.split()
            votes = int(votes)

            if candidate in candidate_votes:
                candidate_votes[candidate] += votes
            else:
                candidate_votes[candidate] = votes

    return candidate_votes


file_name = "C:/Users/Admin/Desktop/190924/LVL_2_Python_group_2024/input.txt"
result = total_votes(file_name)
print(result)

# 3
def election_winner(file_name):
    candidate_votes = total_votes(file_name)
    max_votes = max(candidate_votes.values())

    winners = [candidate for candidate, votes in candidate_votes.items() if votes == max_votes]

    if len(winners) > 1:
        return "Третій тур необхідний", winners
    else:
        return "Переможець", winners[0]


file_name = "C:/Users/Admin/Desktop/190924/LVL_2_Python_group_2024/input.txt"
result = election_winner(file_name)
print(result)




