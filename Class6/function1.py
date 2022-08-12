# Performance, A is best, B is good, C needs improvement

def calculate_bonus(salary, rating):

    # bonus = 0.00
    bonus_lookup ={"A": 0.05, "B": .10, "C": .20}

    bonus = bonus_lookup.get(rating, 0.00)

    # if rating == "A":
    #     bonus = .05
    # if rating =="B":
    #     bonus = .10
    # if rating == "C":
    #     bonus = .20

    return salary * (1 + bonus)

salary =60000

salary_with_bonus_level1 = calculate_bonus(salary, "C")
print(salary_with_bonus_level1)

# salary_with_bonus_level1 = salary * 1.05
# print(salary_with_bonus_level1)
#
# salary_with_bonus_level2 = salary * 1.10
# print(salary_with_bonus_level2)
#
# salary_with_bonus_level3 = salary * 1.20
# print(salary_with_bonus_level3)

