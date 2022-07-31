from src.repository import sql_methods as sql

async def get_single_table(pool,table_name:str,start:int):
    query = "SELECT * FROM " + table_name + " "
    query += "LIMIT " + str(start) + "," + str(start +1000) + ";"
    return await sql.get_multiple_rows(pool, query)

