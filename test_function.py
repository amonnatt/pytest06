from function import number_to_month, validate_number
import pytest


@pytest.mark.code  # pytest -m code
def test_january_input_1():
    input = 1
    exected_result = "january"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_february_input_2():
    input = 2
    exected_result = "february"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_march_input_3():
    input = 3
    exected_result = "march"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_april_input_4():
    input = 4
    exected_result = "april"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_may_input_5():
    input = 5
    exected_result = "may"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_june_input_6():
    input = 6
    exected_result = "june"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_july_input_7():
    input = 7
    exected_result = "july"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_august_input_8():
    input = 8
    exected_result = "august"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_september_input_9():
    input = 9
    exected_result = "september"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_october_input_10():
    input = 10
    exected_result = "october"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_november_input_11():
    input = 11
    exected_result = "november"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.code  # pytest -m code
def test_december_input_12():
    input = 12
    exected_result = "december"
    actual_result = number_to_month(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_out_of_range_input_0():
    input = 0
    exected_result = "out of range"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_out_of_range_input_13():
    input = 13
    exected_result = "out of range"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_out_of_range_input_10():
    input = -10
    exected_result = "out of range"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_out_of_range_input_22():
    input = 22
    exected_result = "out of range"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_1_1():
    input = 1.1
    exected_result = "input integer"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_13_1():
    input = 13.1
    exected_result = "out of range"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_a():
    input = "a"
    exected_result = "input integer"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_sharp():
    input = "#"
    exected_result = "input integer"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_1_input_1():
    input = 1
    exected_result = 1
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_12_input_12():
    input = 12
    exected_result = 12
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_out_of_range_input_0_5():
    input = 0.5
    exected_result = "out of range"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_out_of_range_input_minus_1_5():
    input = -1.5
    exected_result = "out of range"
    actual_result = validate_number(input)
    assert exected_result == actual_result


@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_1_5():
    input = 1.5
    exected_result = "input integer"
    actual_result = validate_number(input)
    assert exected_result == actual_result
