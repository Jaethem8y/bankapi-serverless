from src.repository import single_table_repository as repository

# query table by table_name
async def get_single_table(pool, table_name:str, start:int):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.get_single_table(pool,table_name, start)



