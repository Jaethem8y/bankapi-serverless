from fastapi import APIRouter, Request

from src.service import util_service as service

router = APIRouter()

@router.get("/tables", tags=["all_tables_get"])
async def get_all_table_name(request:Request):
    return await service.get_all_table_names(request.state.pool)

@router.get("/describe/{table_name}", tags=["describe"])
async def describe_single_table_controller(request:Request,table_name:str):
    print("here")
    return await service.describe_single_table_service(request.state.pool, table_name)
