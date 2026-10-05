from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)


# --- parse_guess ---

def test_parse_valid_int_string():
    ok, value, err = parse_guess("42", 1, 50)
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_valid_float_string():
    ok, value, err = parse_guess("42.9", 1, 50)
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_empty_string():
    ok, value, err = parse_guess("", 1, 50)
    assert ok is False
    assert err is not None

def test_parse_none():
    ok, value, err = parse_guess(None, 1, 50)
    assert ok is False
    assert err is not None

def test_parse_non_numeric_string():
    ok, value, err = parse_guess("banana", 1, 50)
    assert ok is False
    assert err is not None

def test_parse_below_range():
    ok, value, err = parse_guess("0", 1, 50)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_above_range():
    ok, value, err = parse_guess("51", 1, 50)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_lower_boundary_is_valid():
    ok, value, err = parse_guess("1", 1, 50)
    assert ok is True
    assert value == 1
    assert err is None

def test_parse_upper_boundary_is_valid():
    ok, value, err = parse_guess("50", 1, 50)
    assert ok is True
    assert value == 50
    assert err is None


# --- check_guess ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- update_score ---

def test_score_on_win_first_attempt():
    # attempt_number is 0-indexed on the first guess
    score = update_score(current_score=0, outcome="Win", attempt_number=0)
    assert score == 90

def test_score_on_win_never_goes_below_floor():
    score = update_score(current_score=0, outcome="Win", attempt_number=20)
    assert score == 10

def test_score_on_too_high():
    score = update_score(current_score=100, outcome="Too High", attempt_number=0)
    assert score == 95

def test_score_on_too_low():
    score = update_score(current_score=100, outcome="Too Low", attempt_number=0)
    assert score == 95

def test_score_unchanged_on_unknown_outcome():
    score = update_score(current_score=100, outcome="Invalid", attempt_number=0)
    assert score == 100
