from typing import List, Union
from pydantic import BaseModel

class DataDict(BaseModel):
    item_code: Union[str, None] = None
    meaning: Union[str, None] = None
    start: int = 0

class FdicFail(BaseModel):
    FDICCertificateNumber: Union[List[int], None] = None
    BankName: Union[str, None] = None 
    City: Union[str, None] = None
    ST: Union[str, None] = None
    AcquiringInstitution: Union[str, None] = None
    ClosingDate: Union[List[str], None] = None
    start: int = 0

class SingleTable(BaseModel):
    bank_id: Union[List[int],None] = None
    year: Union[List[int], None] = None
    quarter: Union[List[int], None] = None 
    score:Union[List[int], None] = None
    start: int = 0