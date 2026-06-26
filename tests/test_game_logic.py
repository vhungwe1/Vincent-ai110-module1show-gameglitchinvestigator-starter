from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hints_not_backwards():
    # Bug fix verification: hints should not be backwards
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# ---- Edge Case Tests ----

def test_empty_input():
    # Empty string should return an error
    ok, guess_int, error = parse_guess("")
    assert ok == False
    assert error == "Enter a guess."

def test_non_numeric_input():
    # Text input should return an error
    ok, guess_int, error = parse_guess("abc")
    assert ok == False
    assert error == "That is not a number."

def test_negative_number():
    # Negative numbers should still parse correctly
    ok, guess_int, error = parse_guess("-5")
    assert ok == True
    assert guess_int == -5

def test_decimal_input():
    # Decimal numbers should be converted to integers
    ok, guess_int, error = parse_guess("42.7")
    assert ok == True
    assert guess_int == 42

def test_none_input():
    # None input should return an error
    ok, guess_int, error = parse_guess(None)
    assert ok == False
    assert error == "Enter a guess."