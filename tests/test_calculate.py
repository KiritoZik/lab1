import pytest  # type: ignore
from src.errors import (CountBracketError, InvalidCharacterError,
                        NullBracketError, LotOperatorError, LastOperatorError,
                        FirstOperatorError, IntegerOperationError, SeamBracketsError,
                        LotPointError, NegativeSqrtError,
                        NotNumberError, NotOperatorError, UnderscoreError, NullExpressionError)
from src.calculate import calculate, lot_float


def test_operators_without_integer_and_power():
    assert calculate('125 + 5') == 130
    assert calculate('125 - 5') == 120
    assert calculate('5 * 5') == 25
    assert calculate('5 / 5') == 1
    with pytest.raises(ZeroDivisionError):
        calculate('5 / 0')
    with pytest.raises(LotOperatorError):
        calculate('5 ++ 0')
    with pytest.raises(LotOperatorError):
        calculate('5 -- 0')
    with pytest.raises(FirstOperatorError):
        calculate('*10+5')
    with pytest.raises(FirstOperatorError):
        calculate('/10+5')


def test_integer_operator():
    assert calculate('5 // 5') == 1
    assert calculate('5 % 5') == 0
    assert calculate('15 % 8') == 7
    assert calculate('125 // 30') == 4
    with pytest.raises(ZeroDivisionError):
        calculate('5 // 0')
    with pytest.raises(ZeroDivisionError):
        calculate('5 % 0')
    with pytest.raises(LotOperatorError):
        calculate('5 %% 5')
    with pytest.raises(LotOperatorError):
        calculate('5 //// 5')
    with pytest.raises(IntegerOperationError):
        calculate('(5/3)//5')
    with pytest.raises(IntegerOperationError):
        calculate('(5/3)%5')
    with pytest.raises(FirstOperatorError):
        calculate('//10+5')
    with pytest.raises(FirstOperatorError):
        calculate('%10+5')


def test_power():
    assert calculate('5 ** 2') == 25
    assert calculate('5 ** 2 ** 3') == 390625
    assert calculate('5 ** 2 + 2 * 2') == 29
    with pytest.raises(OverflowError):
        calculate('25 ** 545454545452')
    with pytest.raises(NegativeSqrtError):
        calculate('(-50) ** 0.5')
    with pytest.raises(FirstOperatorError):
        calculate('**10+5')
    with pytest.raises(LotOperatorError):
        calculate('105 **** 5')


def test_operators_errors():
    with pytest.raises(LotOperatorError):
        calculate('5++6')
    with pytest.raises(LotOperatorError):
        calculate('///5+6')
    with pytest.raises(LotOperatorError):
        calculate('65-5***4')
    with pytest.raises(LastOperatorError):
        calculate('5*6%5/')
    with pytest.raises(FirstOperatorError):
        calculate('*10+5')
    with pytest.raises(FirstOperatorError):
        calculate('/10+5')
    with pytest.raises(NotOperatorError):
        calculate('65')
    with pytest.raises(NotOperatorError):
        calculate('-65')


def test_brackets():
    assert calculate('(5+5) * (1+4)') == 50
    assert calculate('  (5*5**2) - (3 + 4) * 5 - 20 * (1 - 5) * (-1)') == 10
    assert calculate('( 5 + 2 * (-2) - (2//2) ) + 5 * 8') == 40
    with pytest.raises(NullBracketError):
        calculate('5 +  (                  )')
    with pytest.raises(CountBracketError):
        calculate(')5+5')
    with pytest.raises(SeamBracketsError):
        calculate('(3*8)(89//2)')
    with pytest.raises(CountBracketError):
        calculate('(5*5+(8+8)')

def test_lot_float():
    assert lot_float(52123135.54545, '3') == 52123135.545
    assert lot_float(52.444, '') == 52.444
    assert lot_float (52.52, '0') == 53.0

def test_other_errors():
    with pytest.raises(InvalidCharacterError):
        calculate('(5+4)*5&9')
    with pytest.raises(InvalidCharacterError):
        calculate('54.5454 + 5454 .')
    with pytest.raises(InvalidCharacterError):
        calculate('532.555.2 + 54')
    with pytest.raises(NullExpressionError):
        calculate('')
    with pytest.raises(LotPointError):
        calculate('5..4+5')
    with pytest.raises(UnderscoreError):
        calculate('656_889_665_ + 5')
    with pytest.raises(UnderscoreError):
        calculate('_656_889_665 + 5')
    with pytest.raises(UnderscoreError):
        calculate('5 + 656_889_665_')
    with pytest.raises(NotNumberError):
        calculate('asd')
    with pytest.raises(NotNumberError):
        calculate('+asd')
    with pytest.raises(NotNumberError):
        calculate('+-')
    with pytest.raises(NotNumberError):
        calculate('+')
