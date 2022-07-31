from typing import List, Union
from pydantic import BaseModel

class DataDict(BaseModel):
    item_code: Union[str, None] = None
    meaning: Union[str, None] = None
    start: int = 0
    class Config:
        schema_extra = {
        "example": {
            "item_code": "RCFA",
            "meaning": "Total",
            "start":1
        }
    }

class FdicFail(BaseModel):
    FDICCertificateNumber: Union[List[int], None] = None
    BankName: Union[str, None] = None 
    City: Union[str, None] = None
    ST: Union[str, None] = None
    AcquiringInstitution: Union[str, None] = None
    ClosingDate: Union[List[str], None] = None
    start: int = 0
    class Config:
        schema_extra = {
        "example": {
            "FDICCertificateNumber": [80,100],
            "BankName": "Allied",
            "City":"Mu",
            "ST":"AR",
            "AcquiringInstitution":"Today",
            "ClosingDate":["2015-01-01","2018-01-01"],
            "start":0
        }
    }

class SingleTable(BaseModel):
    bank_id: Union[List[int],None] = None
    year: Union[List[int], None] = None
    quarter: Union[List[int], None] = None 
    score:Union[List[int], None] = None
    start: int = 0
    class Config:
        schema_extra = {
        "example": {
            "bank_id": [20,30],
            "year": [1990,1999],
            "quarter":[1,3],
            "score":[0,5],
            "start":0
        }
    }