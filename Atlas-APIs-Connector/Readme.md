# MongoDB Atlas APIs Connector

## Introducton
This provides a template code to follow for building a MongoDB connector using [Data API](https://www.mongodb.com/docs/atlas/api/data-api/). 

## Structure



## Supported functionalities : 
- Client Initialization :
  Follow [these](https://www.mongodb.com/docs/atlas/api/data-api/#get-started) steps to get started with Data API.
  Once the Data API is enabled update the following parameters in a config file.
  
  
  
  The client needs to be initialized with the following parameters; 
    *   BASE_URL        : The URL recieved when creating the Data API via Atlas.
    *   DATA_SOURCE     : Cluster name available on MongoDB Atlas
    *   DATABASE_NAME   : Database name inside the cluster
    *   COLLECTION_NAME : Collection name 
    *   API_KEY         : API KEY recived for accessing the API, make sure correct permissions are provided.
  ```
  client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                             data_source=config.DATA_SOURCE,
                             database=config.DATABASE_NAME,
                             collection=config.COLLECTION_NAME,
                             api_key=config.API_KEY)
  ```


- Authentication : 

  To check if the client is properly initialized with proper values, below method can be utalized. 
  
  ```client.authenticate()``` : Return `True` or `False`
  
  
- Running CRUD Operations : 
  1.  Select the operation to be carried out:
  ```
  # Set the operation to be performed
  client.set_operation(pyAPI.CRUD.FIND_ONE)
  ```
  
  2.  Set the payload as required : 
  ```
  # Set the payload, might include filter, projections.
  client.set_payload(
      filter={"st": "x+56200+002700"}, 
      projection={"_id": 1}
  )
  ```

  3.  Execute the operation :
  ```
  # Execute the client and get the response.
  response = client.execute()

  if response:
      # Check if response recieved.
      print("\n\n Response\n", response.text)
  
  ```
