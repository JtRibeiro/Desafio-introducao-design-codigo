from typing import Dict
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"numbers": [10,5,7, 3, 3.,1, 1]})
    calculator_4 = Calculator4()

    response = calculator_4.calculate(mock_request)
    print()
    print(response)
    
    #Formato da Resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    #Assertividade da Resposta
    assert isinstance(response, dict)
    assert response == {"data": { "Calculator": 4, "result": 4.29 }}
    assert response["data"]["result"] == 4.29
    assert response["data"]["Calculator"] == 4

def test_calculate_with_error():
    mock_request = MockRequest(body={"numbers": [10,5,7, 3, "3", 5,1, 1]})
    calculator_4 = Calculator4()

    with raises(Exception) as excinfo:
        response = calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "Lista não compatível"

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"somethings": [10,5,7, 3, 3.,1, 1]})
    calculator_4 = Calculator4()

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "Body mal formatado"

 