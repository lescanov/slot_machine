from random import choice

# Simulate random slot pull, with slot items represented as ints 1-9
def pull_random_slots() -> list[int]:
    slot_scores = [score for score in range(1, 10, 1)]
    
    # Randomly selecting a slot score 3 times
    pulled_slots = []
    for slot in range(1, 4, 1):
        random_slot = choice(slot_scores)
        pulled_slots.append(random_slot)
    
    return pulled_slots

# Calculate user score from pulled slots
def calculate_score_from_slots(pulled_slots:list[int]) -> int:
    if len(pulled_slots) == 0:
        raise Exception("No rolls detected")
    
    # Get sum of all elements in list pulled_slots
    score = 0
    for slot in pulled_slots:
        score += slot
    
    return score

# Calculates earnings won based on score of pulled slots
def calculate_earnings_from_score(earnings:int, bet_amount:int, score:int) -> int:
    if earnings <= 0:
        raise Exception("Insufficient funds")
    
    if bet_amount > earnings:
        raise Exception("Bet amount exceeds current funds")
    
    # Calculate earnings based on score
    if score <= 14:
        winnings = earnings - bet_amount
    elif score >= 23:
        winnings =  earnings + (bet_amount * 1.5)
    else:
        winnings = earnings

    return round(winnings)
    
# Determines if double or triple of slot item is present and rewards accordingly
def return_earnings_if_replicate_present(pulled_slots:list[int], bet_amount:int) -> int:
    if len(pulled_slots) == 0:
        raise Exception("No rolls detected")
    
    slot_item_occurence = {}
    for slot in pulled_slots:
        slot_item_occurence[slot] = slot_item_occurence.get(slot, 0) + 1
    
    for value in slot_item_occurence.values():
        if value == 2:
            replicate_winnings =  bet_amount * 2
        elif value == 3:
            replicate_winnings = bet_amount * 3
        else:
            replicate_winnings = 0
    
    return replicate_winnings
    
def calculate_earnings(
        pulled_slots:list[int], earnings:int, bet_amount:int) -> int:
    score = calculate_score_from_slots(pulled_slots)
    score_winnings = calculate_earnings_from_score(earnings, bet_amount, score)
    replicate_winnings = return_earnings_if_replicate_present(pulled_slots, bet_amount)
    total_winnings = score_winnings + replicate_winnings
    return total_winnings