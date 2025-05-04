from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validator_body(body)
        calculated_number = self.__process_data(input_data)
        response = self.__format_response(calculated_number)

        print(calculated_number)

        return response
        
    
    def __validator_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def __process_data(self,input_data: List[float]) -> float:
        if not all(isinstance(n, (int, float)) for n in input_data):
            raise HttpBadRequestError("Lista não compatível")
        
        result_data = sum(input_data) / len(input_data)
        return result_data
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(calc_result, 2)
            }
        }