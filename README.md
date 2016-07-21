States & Cities.
===================

This is a simple API that provides a list of local government areas in Nigeria with their GPS coordinates. It's written in Python with Flask Framework and uses MongoDB as DataStore.


## Local Government Areas (LGAs)



All LGAs have the following properties:

Field | Description
------|------------
stateCode | State Code of the State the LGA belongs
state | State the LGA belongs to
lga | Name of the Local Government Area
latitude | Latitude of the Local Government Area
longitude | Longitude of the Local Government Area

For example, Zurmi Local Goverment in Zamfara: 

```json
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Zurmi",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  }

```

## How to setup ?
1. clone this repo
2. Create a Virtual Environment for the application 
```shell
virtualenv env
```
3. Activate your virtual environment 
```shell
source env/bin/activate
```
4. Install all the project's requirements

```python
pip install -r requirements.txt
```




RUN:
===
The Application runs on port 8080

To run, enter command :

python run.py

Anc check the endpoints in your favourite REST Client

For any questions or problems feel free to shoot me an email @ mykelokuboyejo@gmail.com
