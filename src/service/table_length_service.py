from src.repository import table_length_repository as repository

# query single table length (# of rows)
async def get_single_table_length(pool, table_name:str):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.get_single_table_length(pool,table_name)