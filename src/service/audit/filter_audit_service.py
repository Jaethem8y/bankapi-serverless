from src.repository.audit import filter_audit_repository as repository
from src.DTO.search_filter import DataDict, FdicFail, SingleTable

async def filter_data_dict(pool,dataDict:DataDict):
    return await repository.filter_data_dict(pool,dataDict)

async def filter_data_dict_length(pool,dataDict:DataDict):
    return await repository.filter_data_dict_length(pool,dataDict)

async def filter_fdic_fail(pool, fdicFail:FdicFail):
    return await repository.filter_fdic_fail(pool, fdicFail)

async def filter_fdic_fail_length(pool, fdicFail:FdicFail):
    return await repository.filter_fdic_fail_length(pool, fdicFail)

async def filter_single_table(pool, table_name, singleTable:SingleTable):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.filter_single_table(pool,table_name, singleTable)

async def filter_single_table_length(pool, table_name, singleTable:SingleTable):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.filter_single_table_length(pool,table_name, singleTable)