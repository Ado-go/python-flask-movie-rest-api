# python-flask-movie-rest-api

This project is a simple flask rest API for movies. \
The data are not stored permanently.

# RUNNING

Option 1 
1. Clone repository 
2. Use docker(described below)

Option 2
1. Clone repository
2. pip install flask 
3. run main.py

After you successfully start the API use https://www.postman.com/ for easy GET, POST and PUT requests

# ENDPOINTS

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
# DOCKER
This project also contains Dockerfile.

1. Create image
2. Run container

To create an image run:
```
docker build -t any_name_you_want .
```
To run container run:
```
docker run -d -p 5000:5000 name_you_typed_in_build
```
