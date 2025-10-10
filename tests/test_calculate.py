import pytest
from src.errors import *
from src.calculate import calculate

def test_calculate():
    assert calculate('5-5') == 0
    assert calculate('5+5') == 10
    assert calculate('5+5*5') == 30
    assert calculate('5+5*5*5') == 130
    assert calculate('+  7            - 2') == 5
    assert calculate('2 ** (1 + 2)') == 8
    assert calculate('10 // 9 + 1') == 2
    assert calculate('5%    2 + 5  - 2') == 4
    assert calculate('((3 * 5 * 4 * 1) + 57+ (4 + 4 * (-8))) * (-2) ') == -178
    assert calculate('5/2') == 2.5
    assert calculate('16//5') == 3
    assert calculate('16%5') == 1
    assert calculate('5/2 + (2*4+1)') == 11.5


def test_raises():
    with pytest.raises(ZeroDivisionError): calculate(' 5 / 0 ')
    with pytest.raises(ZeroDivisionError): calculate(' 5 // 0 ')
    with pytest.raises(ZeroDivisionError): calculate(' 5 % 0 ')
    with pytest.raises(CountBracketError): calculate('(5*5+(8+8)')
    with pytest.raises(NullBracketError): calculate('5 +  (                  )')
    with pytest.raises(InvalidCharacterError): calculate('(5+4)*5&9')
    with pytest.raises(InvalidCharacterError): calculate('54.5454 + 5454 .')
    with pytest.raises(InvalidCharacterError): calculate('532.555.2 + 54')
    with pytest.raises(CountBracketError): calculate(')5+5')
    with pytest.raises(NullExpressionError): calculate('')
    with pytest.raises(LotOperatorError): calculate('5++6')
    with pytest.raises(LastOperatorError): calculate('5*6%5/')
    with pytest.raises(FirstOperatorError): calculate('*10+5')
    with pytest.raises(IntegerOperationError): calculate('(5/3)//5')
    with pytest.raises(IntegerOperationError): calculate('(5/3)%5')
    with pytest.raises(SeamBracketsError): calculate('(3*8)(89//2)')
    with pytest.raises(LotPointError): calculate('5..4+5')
    with pytest.raises(NotOperatorError): calculate('65')
    with pytest.raises(NotOperatorError): calculate('-65')
    with pytest.raises(UnderscoreError): calculate('656_889_665_ + 5')
    with pytest.raises(UnderscoreError): calculate('_656_889_665 + 5')
    with pytest.raises(UnderscoreError): calculate('5 + 656_889_665_')
    with pytest.raises(NegativeSqrtError): calculate('(-53)**0.5')
    with pytest.raises(NotNumberError): calculate('asd')
    with pytest.raises(NotNumberError): calculate('+asd')
    with pytest.raises(NotNumberError): calculate('+-')
    with pytest.raises(NotNumberError): calculate('+')
    with pytest.raises(OverflowError): calculate('25**6545351315')

