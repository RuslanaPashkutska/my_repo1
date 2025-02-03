from random import randint
def get_numbers_ticket(min, max, quantity):
    result_array = set()
    while len(result_array) != quantity:
        result_array.add(randint(min,max))
        numbers = sorted(list(result_array))
    return numbers
lottery_numbers = get_numbers_ticket(1,55, 3)
print("Your lottery numbers:", lottery_numbers)
