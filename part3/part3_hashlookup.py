# Define the family members and their characteristic scores
family_members = {
'Jones Marshall': {'rudeness': 10, 'money_motive': 0.1, 'playfulness': 0, 'ability': 7},
'Jenna Marshall': {'rudeness': 2, 'money_motive': 0.7, 'playfulness': 3,'ability': 5},
'Peter Marshall': {'rudeness': 4, 'money_motive': 5, 'playfulness': 7,'ability': 5},
'Penelope Marshall': {'rudeness': 1, 'money_motive': 0.5, 'playfulness': 9,'ability': 2},
'Will Marshall': {'rudeness': 0, 'money_motive': 10, 'playfulness': 0,'ability': 10}
}


# Define the weights for each characteristic
weights = {
    'rudeness': 0.7,
    'money_motive': 0.9,
    'playfulness': 0.5,
    'ability': 0.5,
}


# Calculate the weighted scores for each family member
weighted_scores = {member: sum(scores[characteristic] * weight for characteristic, weight in weights.items())
                   for member, scores in family_members.items()}


# Find the family member with the highest weighted score
suspect_motive = max(weighted_scores, key=weighted_scores.get)


# Print the results
for member, weighted_score in weighted_scores.items():
    print(f"{member}: {weighted_score}")