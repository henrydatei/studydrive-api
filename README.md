# studydrive-api
A Python Wrapper for the (unofficial) Studydrive API

### Install
Run
```
pip3 install studydrive
```
in your terminal.

### Usage
As most querys have to be authenticated you should login first
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.login("email", "password")
```
Alternatively you can register a new account
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.register("email", "password")
```
Don't forget to verify your email - otherwise some features will not work!