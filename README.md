# Python-flask-movie-rest-api

This project is a simple Flask REST API for movies.
The data is not stored permanently.

# Installation

### Option 1  
1. Clone the repository.  
2. Use Docker (described below).  

### Option 2  
1. Clone the repository.  
2. Run `pip install flask`.  
3. Run `main.py`.  

After you successfully start the API, use [Postman](https://www.postman.com/) for easy GET, POST, and PUT requests.

# Endpoints

GET http://127.0.0.1:5000/movies

RESPONSE
```
[{
  "id": 1,
  "title": "Computer",
  "description": "Film about that computer",
  "release_year": 1993
},{
  "id": 2,
  "title": "Slippery Floor",
  "description": "The floor was very slippery",
  "release_year": 2013
}]
```

GET http://127.0.0.1:5000/movies/1

RESPONSE
```
{
  "id": 1,
  "title": "Computer",
  "description": "Film about that computer",
  "release_year": 1993
}
```

POST http://127.0.0.1:5000/movies

REQUEST
```
{
  "title": "Last Episode vol.156",
  "description": "This one is definitely the last episode",
  "release_year": 1987
}
```

RESPONSE
```
{
  "id": 3,
  "title": "Last Episode vol.156",
  "description": "This one is definitely the last episode",
  "release_year": 1987
}
```

PUT http://127.0.0.1:5000/movies/1

REQUEST
```
{
  "title": "The Walk",
  "description": "Young man walking through park...",
  "release_year": 2020
}
```

RESPONSE
```
{
  "id": 1,
  "title": "The Walk",
  "description": "Young man walking through park...",
  "release_year": 2020
}
```
# Docker
This project also contains Dockerfile.

1. Create the image
2. Run the container

To create an image run:
```
docker build -t any_name_you_want .
```
To run container run:
```
docker run -d -p 5000:5000 name_you_typed_in_build
```
