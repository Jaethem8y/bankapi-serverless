from fastapi import APIRouter, Request

from src.service import filter_table_service as service

from src.DTO.search_filter import DataDict, FdicFail, SingleTable

router = APIRouter()

@router.post("/single/data_dict")
async def filter_data_dict(request:Request, dataDict:DataDict):
    return await service.filter_data_dict(request.state.pool,dataDict)

@router.post("/length/data_dict")
async def filter_data_dict(request:Request, dataDict:DataDict):
    return await service.filter_data_dict_length(request.state.pool,dataDict)

@router.post("/single/fdic_fail")
async def filter_fdic_fail(request:Request, fdicFail:FdicFail):
    return await service.filter_fdic_fail(request.state.pool,fdicFail)

@router.post("/length/fdic_fail")
async def filter_fdic_fail(request:Request, fdicFail:FdicFail):
    return await service.filter_fdic_fail_length(request.state.pool,fdicFail)

@router.post("/single/{table_name}")
async def filter_single_table(request:Request, table_name:str, singleTable:SingleTable):
    return await service.filter_single_table(request.state.pool, table_name, singleTable)
