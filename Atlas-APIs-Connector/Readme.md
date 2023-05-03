# MongoDB Atlas APIs Connector

## Introducton
This repo gives a boilerplate code on how a MongoDB connector using Atlas Data API should be built. It serves as a starter guide for building a connector and can be easily extended to fit your usecase. 
Lanuage chosen is Python but can it be easily transformed to any language of choice that can support REST calls.


## Structure
This architecture gives an idea on how the connector is build to put forward an overview : 
![image](https://user-images.githubusercontent.com/114057324/226342954-f7cc6021-9d63-469e-b5a6-63c7276deead.png)


## Supported functionalities : 
### 1.  **Client Initialization** :

  Follow [these](https://www.mongodb.com/docs/atlas/api/data-api/#get-started) steps to get started with Data API.
  Once the Data API is enabled update the following parameters in a config file. 

  The client needs to be initialized with the following parameters; 

      *   BASE_URL        : The URL recieved when creating the Data API via Atlas.
      *   DATA_SOURCE     : Cluster name available on MongoDB Atlas
      *   DATABASE_NAME   : Database name inside the cluster
      *   COLLECTION_NAME : Collection name 
      *   API_KEY         : API KEY recived for accessing the API, make sure correct permissions are provided.

  You will need to import the `pyAPI` module and initialize `DataAPIClient` using the above mentioned parameters, as shown below : 

  ```
  client = pyAPI.DataAPIClient(base_url=config.BASE_URL,
                               data_source=config.DATA_SOURCE,
                               database=config.DATABASE_NAME,
                               collection=config.COLLECTION_NAME,
                               api_key=config.API_KEY)
  ```


### 2.  **Authentication** : 

  The client authentication and authorization comes in as the most import part of the connector, you should be well aware that your client is authenticated and the connection established is secure for communication and data transfer.
  For this, you can use various different options available here.
  
  In this particular example, we are using API KEY which is already mentioned in the parameters above.


  To check if the client is properly initialized with proper values, below method can be utalized. 
  
  ```
  client.authenticate()
  ```
  
  Based on the response from the server it either responds with True or False, indicating if the API KEY is correct or not.
  
### 3.  **Running CRUD Operations** : 

   a.  Select the operation to be carried out ( All operations are listed [here](https://www.mongodb.com/docs/atlas/api/data-api-resources/) ): 
 
  ```
  # Set the operation to be performed
  client.set_operation(pyAPI.CRUD.FIND_ONE)
  ```
  
  b.  Set the payload as required : 
  
  ```
  # Set the payload, might include filter, projections.
  client.set_payload(
      filter={"st": "x+56200+002700"}, 
      projection={"_id": 1}
  )
  ```

  c.  Execute the operation :
  
  ```
  # Execute the client and get the response.
  response = client.execute()

  if response:
      # Check if response recieved.
      print("Response", response.text)
  
  ```
  
## Reference 
For getting an in-depth idea about the Data API and how it can help your product to be built with much ease refer the following link to documentation.

[https://www.mongodb.com/docs/atlas/api/data-api](https://www.mongodb.com/docs/atlas/api/data-api)
 
