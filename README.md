# General Overview
- This API enables users to retrieve bank data via web. 

# Routes
- The specified documetation can be found at https://4yjz4qhd61.execute-api.us-east-2.amazonaws.com/dev/docs

# Resources
- For the general FastAPI info https://fastapi.tiangolo.com/lo/ 
- For informations on Pydantic https://docs.pydantic.dev/latest/
- For information on how to deploy this serverless https://www.youtube.com/watch?v=6fE31084Uks&t=717s

# How to run this code locally
- You can use uvicorn that are described in FastAPI 
- For ex: uvicorn src.main:app -> it could change as name of the directories change
- You would need to specify the db credentials -> create db.py at src folder, then put the credentials

# To deploy it to AWS using methods from video above

- cd bank-server_env/lib/python3.10/site-packages/
- zip -r9 ../../../../function.zip .
- back to the root
- zip -g ./function.zip -r src
