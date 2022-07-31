from src.repository import sql_methods as sql

async def describe_single_table(pool,table_name:str):
    query = "DESCRIBE " + table_name + ";"
    return await sql.get_multiple_rows(pool, query)

async def get_all_table_name(pool):
    query = "SHOW TABLES;"
    return await sql.get_multiple_rows(pool,query)

