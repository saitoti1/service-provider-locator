CREATE_COMPANY_OBJECT_SUCCESS = {
    "name": "Lazy Panda 3108",
    "email": "lazy@mozio.com",
    "phone_number": "9876543210",
    "language": "eng",
    "currency": "USD",
    "password": "Aakashi@3108"
}

CREATE_COMPANY_OBJECT_FAILURE = {
    "name": "Lazy Panda 3108",
    "email": "lazy@mozio.com",
    "phone_number": "9876543210",
    "language": "eng",
    "currency": "USD",
}

LOGIN_COMPANY_OBJECT_SUCCESS = {
    "email": "panda@mozio.com",
    "password": "Mickey@3108"
}

LOGIN_COMPANY_OBJECT_FAILURE = {
    "email": "mickey@mozio.com",
    "password": "Mickey@3108"
}

UPDATE_COMPANY_OBJECT_SUCCESS = {
    "name": "Lazy Panda 8013",
    "phone_number": "9876543210",
    "language": "hin",
}

UPDATE_COMPANY_OBJECT_FAILURE = {
    "language": "hi",
}

CREATE_SERVICE_AREA_OBJECT_SUCCESS = {
  "name": "Service Area 1",
  "price": 3108.96,
  "geo_json": {
    "type": "Feature",
    "properties": {},
    "geometry": {
      "type": "Polygon",
      "coordinates": [
        [
          [
            74.08905029296875,
            21.25354187363282
          ],
          [
            74.28680419921875,
            20.838277806058933
          ],
          [
            74.73724365234375,
            20.958874775031518
          ],
          [
            74.45709228515625,
            21.424946712203003
          ],
          [
            74.08905029296875,
            21.25354187363282
          ]
        ]
      ]
    }
  }
}

CREATE_SERVICE_AREA_OBJECT_FAILURE = {
  "name": "Service Area 1",
  "geo_json": {
    "type": "Feature",
    "properties": {},
    "geometry": {
      "type": "Polygon",
      "coordinates": [
        [
          [
            74.08905029296875,
            21.25354187363282
          ],
          [
            74.28680419921875,
            20.838277806058933
          ],
          [
            74.73724365234375,
            20.958874775031518
          ],
          [
            74.45709228515625,
            21.424946712203003
          ],
          [
            74.08905029296875,
            21.25354187363282
          ]
        ]
      ]
    }
  }
}

UPDATE_SERVICE_AREA_OBJECT_SUCCESS = {
	"name" : "Service Area 1",
	"price": 3108.96
}

UPDATE_SERVICE_AREA_OBJECT_FAILURE = {
    "geo_json": {}
}

SEARCH_SEARVICE_AREA_OBJECT_SUCCESS = {
	"longitude" : 74.37744140625,
	"latitude": 21.30216955583029
}

SEARCH_SEARVICE_AREA_OBJECT_FAILURE = {
	"longitude" : 74.37744140625,
}