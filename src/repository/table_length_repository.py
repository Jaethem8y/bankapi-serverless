from src.repository import sql_methods as sql

async def get_single_table_length(pool, table_name:str):
    query = "SELECT COUNT(*) AS length FROM " + table_name +";"
    return await sql.get_single_row(pool,query)