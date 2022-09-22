from cgitb import reset
from fastapi import APIRouter, Request

from src.service import single_tables_service as service


router = APIRouter()


@router.get("/{table_name}",tags=["get"])
async def get_single_table(request:Request, table_name:str, start:int=0):
    res =  await service.get_single_table(request.state.pool, table_name, start)
    print("at controller "+ str(len(res)))
    return res