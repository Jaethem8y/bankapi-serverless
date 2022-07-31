from email.encoders import encode_quopri
from src.repository import sql_methods as sql

from src.DTO.search_filter import DataDict, FdicFail, SingleTable

async def filter_data_dict(pool, dataDict:DataDict):
    query = "SELECT * FROM data_dict WHERE 1 = 1 "
    if dataDict.item_code != None:
        query += "AND item_code LIKE \'%" + dataDict.item_code + "%\' "
    if dataDict.meaning != None:
        query += "AND meaning LIKE \'%" + dataDict.meaning + "%\' "
    query += "Limit " +str(dataDict.start) + "," + str(dataDict.start+1000) +";"
    return await sql.get_multiple_rows(pool,query)

async def filter_data_dict_length(pool, dataDict:DataDict):
    query = "SELECT COUNT(*) AS length FROM data_dict WHERE 1 = 1 "
    if dataDict.item_code != None:
        query += "AND item_code LIKE \'%" + dataDict.item_code + "%\' "
    if dataDict.meaning != None:
        query += "AND meaning LIKE \'%" + dataDict.meaning + "%\' "
    query += ";"
    return await sql.get_single_row(pool,query)

async def filter_fdic_fail(pool, fdicFail:FdicFail):
    query = "SELECT * FROM fdic_fail WHERE 1 = 1 "
    if fdicFail.FDICCertificateNumber != None:
        query += "AND FDICCertificateNumber >= " + str(fdicFail.FDICCertificateNumber[0]) + " AND FDICCertificateNumber <= " + str(fdicFail.FDICCertificateNumber[1])+ " "
    if fdicFail.BankName != None:
        query += "AND BankName LIKE \'%" + fdicFail.BankName + "%\' " 
    if fdicFail.City != None:
        query += "AND City LIKE \'%" + fdicFail.City + "%\' "
    if fdicFail.ST != None:
        query += "AND ST LIKE \'%" + fdicFail.ST + "%\' " 
    if fdicFail.AcquiringInstitution != None:
        query += "AND AcquiringInstitution LIKE \'%" + fdicFail.AcquiringInstitution + "%\' "
    if fdicFail.ClosingDate != None:
        query += "AND ClosingDate BETWEEN " "\'"+ fdicFail.ClosingDate[0] +"\'" + "AND " + "\'" + fdicFail.ClosingDate[1] + "\' "
    query += "Limit " +str(fdicFail.start) + "," + str(fdicFail.start+1000) +";"
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def filter_fdic_fail_length(pool, fdicFail:FdicFail):
    query = "SELECT COUNT(*) AS length FROM fdic_fail WHERE 1 = 1 "
    if fdicFail.FDICCertificateNumber != None:
        query += "AND FDICCertificateNumber >= " + str(fdicFail.FDICCertificateNumber[0]) + " AND FDICCertificateNumber <= " + str(fdicFail.FDICCertificateNumber[1])+ " "
    if fdicFail.BankName != None:
        query += "AND BankName LIKE \'%" + fdicFail.BankName + "%\' " 
    if fdicFail.City != None:
        query += "AND City LIKE \'%" + fdicFail.City + "%\' "
    if fdicFail.ST != None:
        query += "AND ST LIKE \'%" + fdicFail.ST + "%\' " 
    if fdicFail.AcquiringInstitution != None:
        query += "AND AcquiringInstitution LIKE \'%" + fdicFail.AcquiringInstitution + "%\' "
    if fdicFail.ClosingDate != None:
        query += "AND ClosingDate BETWEEN " "\'"+ fdicFail.ClosingDate[0] +"\'" + "AND " + "\'" + fdicFail.ClosingDate[1] + "\' "
    query += ";"
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def filter_single_table(pool, table_name, singleTable:SingleTable):
    query = "SELECT * FROM " + table_name + " WHERE 1 = 1 "
    score = table_name[6:]
    if singleTable.bank_id != None:
        query += "AND bank_id >= " + str(singleTable.bank_id[0]) + " AND bank_id <= " + str(singleTable.bank_id[1]) + " "
    if singleTable.year != None:
        start_year = singleTable.year[0]
        end_year = singleTable.year[1]
        query += "AND year >= " + str(start_year) + " AND year <= " + str(end_year) + " "
    if singleTable.quarter != None:
        start_quarter = singleTable.quarter[0]
        end_quarter = singleTable.quarter[1]
        query += "AND quarter >= " + str(start_quarter) + " AND quarter <= " + str(end_quarter) + " "
    if singleTable.score != None:
        start_score = singleTable.score[0]
        end_score = singleTable.score[1]
        query += "AND " + score + " >= " + str(start_score) + " AND " + score + " <= " + str(end_score) + " "
    query += "Limit " +str(singleTable.start) + "," + str(singleTable.start+1000) +";"
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def filter_single_table_length(pool, table_name, singleTable:SingleTable):
    query = "SELECT COUNT(*) AS length FROM " + table_name + " WHERE 1 = 1 "
    score = table_name[6:]
    if singleTable.bank_id != None:
        query += "AND bank_id >= " + str(singleTable.bank_id[0]) + " AND bank_id <= " + str(singleTable.bank_id[1]) + " "
    if singleTable.year != None:
        start_year = singleTable.year[0]
        end_year = singleTable.year[1]
        query += "AND year >= " + str(start_year) + " AND year <= " + str(end_year) + " "
    if singleTable.quarter != None:
        start_quarter = singleTable.quarter[0]
        end_quarter = singleTable.quarter[1]
        query += "AND quarter >= " + str(start_quarter) + " AND quarter <= " + str(end_quarter) + " "
    if singleTable.score != None:
        start_score = singleTable.score[0]
        end_score = singleTable.score[1]
        query += "AND " + score + " >= " + str(start_score) + " AND " + score + " <= " + str(end_score) + " "
    query += ";"
    print(query)
    return await sql.get_multiple_rows(pool,query)

