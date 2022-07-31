from src.repository import util_repository as repository

# query showing all tables
async def get_all_table_names(pool):
    return await repository.get_all_table_name(pool)

# query describe table_name
async def describe_single_table_service(pool,table_name:str):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.describe_single_table(pool,table_name)