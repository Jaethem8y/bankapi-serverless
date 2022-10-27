from src.repository.audit import single_audit_repository as repository

# query table by table_name
async def get_single_table(pool, table_name:str, start:int):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    res = await repository.get_single_table(pool,table_name, start)
    print( "here the length " + str(len(res)))
    return res


