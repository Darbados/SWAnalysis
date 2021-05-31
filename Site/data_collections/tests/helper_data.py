collection_data = """name,height,mass,hair_color,skin_color,eye_color,birth_year,gender,homeworld,date
Luke Skywalker,172,77,blond,fair,blue,19BBY,male,Tatooine,2014-12-20
C-3PO,167,75,n/a,gold,yellow,112BBY,n/a,Tatooine,2014-12-20
R2-D2,96,32,n/a,"white, blue",red,33BBY,n/a,Naboo,2014-12-20
Darth Vader,202,136,none,white,yellow,41.9BBY,male,Tatooine,2014-12-20
Leia Organa,150,49,brown,light,brown,19BBY,female,Alderaan,2014-12-20
Owen Lars,178,120,"brown, grey",light,blue,52BBY,male,Tatooine,2014-12-20
Beru Whitesun lars,165,75,brown,light,blue,47BBY,female,Tatooine,2014-12-20
R5-D4,97,32,n/a,"white, red",red,unknown,n/a,Tatooine,2014-12-20
Biggs Darklighter,183,84,black,light,brown,24BBY,male,Tatooine,2014-12-20
"""

people_response = {
    "count": 82,
    "next": None,
    "previous": None,
    "results": [
        {
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male",
            "homeworld": "http://swapi.dev/api/planets/1/",
            "films": [
                "http://swapi.dev/api/films/1/",
                "http://swapi.dev/api/films/2/",
                "http://swapi.dev/api/films/3/",
                "http://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "http://swapi.dev/api/vehicles/14/",
                "http://swapi.dev/api/vehicles/30/"
            ],
            "starships": [
                "http://swapi.dev/api/starships/12/",
                "http://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-09T13:50:51.644000Z",
            "edited": "2014-12-20T21:17:56.891000Z",
            "url": "http://swapi.dev/api/people/1/"
        },
        {
            "name": "C-3PO",
            "height": "167",
            "mass": "75",
            "hair_color": "n/a",
            "skin_color": "gold",
            "eye_color": "yellow",
            "birth_year": "112BBY",
            "gender": "n/a",
            "homeworld": "http://swapi.dev/api/planets/1/",
            "films": [
                "http://swapi.dev/api/films/1/",
                "http://swapi.dev/api/films/2/",
                "http://swapi.dev/api/films/3/",
                "http://swapi.dev/api/films/4/",
                "http://swapi.dev/api/films/5/",
                "http://swapi.dev/api/films/6/"
            ],
            "species": [
                "http://swapi.dev/api/species/2/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:10:51.357000Z",
            "edited": "2014-12-20T21:17:50.309000Z",
            "url": "http://swapi.dev/api/people/2/"
        },
    ]
}


planets_response = {
    "count": 60,
    "next": None,
    "previous": None,
    "results": [
        {
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000",
            "residents": [
                "http://swapi.dev/api/people/1/",
                "http://swapi.dev/api/people/2/",
                "http://swapi.dev/api/people/4/",
                "http://swapi.dev/api/people/6/",
                "http://swapi.dev/api/people/7/",
                "http://swapi.dev/api/people/8/",
                "http://swapi.dev/api/people/9/",
                "http://swapi.dev/api/people/11/",
                "http://swapi.dev/api/people/43/",
                "http://swapi.dev/api/people/62/"
            ],
            "films": [
                "http://swapi.dev/api/films/1/",
                "http://swapi.dev/api/films/3/",
                "http://swapi.dev/api/films/4/",
                "http://swapi.dev/api/films/5/",
                "http://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-09T13:50:49.641000Z",
            "edited": "2014-12-20T20:58:18.411000Z",
            "url": "http://swapi.dev/api/planets/1/"
        },
        {
            "name": "Alderaan",
            "rotation_period": "24",
            "orbital_period": "364",
            "diameter": "12500",
            "climate": "temperate",
            "gravity": "1 standard",
            "terrain": "grasslands, mountains",
            "surface_water": "40",
            "population": "2000000000",
            "residents": [
                "http://swapi.dev/api/people/5/",
                "http://swapi.dev/api/people/68/",
                "http://swapi.dev/api/people/81/"
            ],
            "films": [
                "http://swapi.dev/api/films/1/",
                "http://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-10T11:35:48.479000Z",
            "edited": "2014-12-20T20:58:18.420000Z",
            "url": "http://swapi.dev/api/planets/2/"
        },
    ],
}
