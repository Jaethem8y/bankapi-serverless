description = """
#### Authors and Acknowledgement
    This API consumes data from bank_database which is built by Dr. Eric Manley and Dr. Sean Severe of Department of Computer Science and Department of Economics at Drake University. Without their supervision and help, this API could not be brought. 
    
    The authors of this API are Jaehyeok Choi and Jacob Danner, both of who are seniors at Drake Univeristy studying computer science.
    
    The source code of this API is available at https://github.com/Jaethem8y/bankapi-serverless

    In case of error, please inform authors at jaehyeok.choi@drake.edu

#### General Overview
    Most of the get request will have a query parameter named start. Start indicates from which row in table should be queried. 
    The default value of start is always 0, including when it is not specified.

    For example, GET request to url_to_server/single/data_dict?start=10 would query rows from data_dict table row starting from 10th to 1010th. the range will always be 1000.
    if the GET request url changes to url_to_server/single/data_dict?start=100, then the result would be from 100th row to 1100th row

    To specifiy the requirements, which would corresponds to WHERE clause in SQL, the request needs to be made with POST which will be describe below
"""

tags_metadata = [
    {
        "name":"all_tables_get",
        "description":"Returns the name of all the tables in bank_database. No query parameters"
    },{
        "name":"describe",
        "description":"SQL equivalent of describe requested table"
    },
    {
        "name":"get",
        "description":"For length, returns the length of table. Takes no query parameter. For the /single/ start needs to be specified to access data with higher rows than 1000"
    },
    {
        "name":"post",
        "description":"With the JSON body object, the specific of each column would be considered to make query. If the value is integer or date, it takes array, but only two values needed. start and end. For example if there is a date column and the desired date is between 2018 and 2019, then the request body would be looking like \{ \'date\': [\'2018-01-01\',\'2019-12-31\'] \}. the start field indicates which row to start query from. Choose the object/schema from bottom where it fits your usage."
    }
]