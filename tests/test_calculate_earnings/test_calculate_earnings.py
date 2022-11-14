import pytest
from slot_machine import calculate_earnings

@pytest.fixture
def simulate_random_roll():
    return [1, 9, 8]

@pytest.fixture
def earnings():
    return 100

@pytest.fixture
def bet_amount():
    return 25

def fail_score_calculation():
    return 6

def fail_replicate_calculation():
    return 6


def test_calculate_score_from_roll(simulate_random_roll:list[int]):
    assert calculate_earnings.calculate_score_from_slots(simulate_random_roll) == 18

def test_low_score_earnings(earnings:int, bet_amount:int):
    score = 5
    total_earnings = earnings - bet_amount
    assert calculate_earnings.calculate_earnings_from_score(earnings, bet_amount, score) == total_earnings
    
def test_mid_score_earnings(earnings:int, bet_amount:int):
    score = 20
    total_earnings = earnings
    assert calculate_earnings.calculate_earnings_from_score(earnings, bet_amount, score) == total_earnings
    
def test_high_score_earnings(earnings:int, bet_amount:int):
    score = 27
    total_earnings = round(earnings + (bet_amount * 1.5))
    assert calculate_earnings.calculate_earnings_from_score(earnings, bet_amount, score) == total_earnings
    
def test_earnings_if_duplicate(bet_amount:int):
    roll = [1, 1, 2]
    duplicate_earnings = bet_amount * 2
    assert calculate_earnings.return_earnings_if_replicate_present(roll, bet_amount) == duplicate_earnings
    
def test_triplicate_earnings(earnings:int):
    roll = [1, 1, 1]
    triplicate_earnings = earnings * 3
    assert calculate_earnings.return_earnings_if_replicate_present(roll, bet_amount) == triplicate_earnings

def test_total_earnings(earnings:int, bet_amount:int):
    # Declaring expected earnings from particular roll
    roll = [5, 5, 9]
    total_earnings = earnings + (bet_amount * 2)
    
    # Calciating with function
    computed_earnings = calculate_earnings.calculate_earnings(roll, earnings, bet_amount)
    
    assert total_earnings == computed_earnings
    
def test_return_error_if_negative_earnings(bet_amount:int):
    negative_earnings = -50_000
    score = 27
    assert calculate_earnings.calculate_earnings_from_score(negative_earnings, bet_amount, score) is Exception
    
def test_return_error_if_bet_amount_less_than_earnings(earnings:int):
    bet_amount = 50_000
    score = 27
    assert calculate_earnings.calculate_earnings_from_score(earnings, bet_amount, score) is Exception

def test_return_error_if_no_roll_supplied():
    roll = []
    assert calculate_earnings.calculate_score_from_slots(roll) is Exception
    assert calculate_earnings.return_earnings_if_replicate_present(roll) is Exception