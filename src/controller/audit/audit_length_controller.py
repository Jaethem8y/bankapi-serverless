from fastapi import APIRouter, Request

from src.service.audit import audit_length_service as service

router = APIRouter()

@router.get(path="/{table_name}",tags=["get"])
async def get_table_length(request:Request,table_name:str):
  return await service.get_single_table_length(request.state.pool,table_name)