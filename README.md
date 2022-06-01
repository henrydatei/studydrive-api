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
# I recommend setting a nickname, university, program and semester
api.setNickname("my Nickname")
api.setProgram(universityID = 800, programID = 619, semesterID = 45)
# You can get these IDs from the following functions: api.getUniversities(), api.getAllMajors(), api.getSemester()
```
Don't forget to verify your email - otherwise some features will not work!