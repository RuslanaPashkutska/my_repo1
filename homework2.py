from random import randint

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= max_val <= 1000) or not (1 <= quantity <= (max_val - min_val + 1)):
        return []

    result_array = set()
    while len(result_array) < quantity:
        result_array.add(randint(min_val, max_val))

    return sorted(result_array)


lottery_numbers = get_numbers_ticket(10,14, 6)
print("Your lottery numbers:", lottery_numbers)
