# studydrive-api
A Python Wrapper for the (unofficial) Studydrive API

**Project is currently not working as Studydrive has moved some nessesary keys and logic into a shared library that I can't read because it's compiled C code.**

## Install
Run
```
pip3 install studydrive
```
in your terminal.

---

## Usage
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

For development reasons I've implemented a third possiblity to "login": If you have a valid token you can directly use it
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI(token = myToken)
```

---

## Documentation

### login
Parameters:
 - Email
 - Password

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
print(api.login("email", "password"))
```
Output:
```json
{
   "token_type":"Bearer",
   "new_user":"None",
   "expires_in":5184000,
   "access_token":"***",
   "refresh_token":"***"
}
```

### getUniversityCourses
Gets all courses for a given university.

Parameters:
 - universityID

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.login("email", "password")
print(api.getUniversityCourses(800)[0:5]) # the [0:5] is just to reduce the output
```
Output:
```json
[
   {
      "number":"BSMB-1101",
      "name":"Höhere Mathematik I (für Maschinenbauer)",
      "qlearningid":"None",
      "originator":"None",
      "active":1,
      "copyright_warning":0,
      "users_count":6844,
      "has_joined":false,
      "share_link":"https://www.studydrive.net/de/course/hoehere-mathematik-i-fuer-maschinenbauer-/53417?ref=1657548",
      "email_body":"",
      "email_subject":"Melde dich auch bei Studydrive an",
      "university_id":800,
      "course_id":53417
   },
   {
      "number":"BSETITTI-211/09",
      "name":"Höhere Mathematik 2",
      "qlearningid":"None",
      "originator":"None",
      "active":1,
      "copyright_warning":0,
      "users_count":6181,
      "has_joined":false,
      "share_link":"https://www.studydrive.net/de/course/hoehere-mathematik-2/51944?ref=1657548",
      "email_body":"",
      "email_subject":"Melde dich auch bei Studydrive an",
      "university_id":800,
      "course_id":51944
   },
   {
      "number":"BSMB-1002",
      "name":"Mechanik I für Maschinenbauer",
      "qlearningid":"None",
      "originator":"None",
      "active":1,
      "copyright_warning":0,
      "users_count":6071,
      "has_joined":false,
      "share_link":"https://www.studydrive.net/de/course/mechanik-i-fuer-maschinenbauer/53415?ref=1657548",
      "email_body":"",
      "email_subject":"Melde dich auch bei Studydrive an",
      "university_id":800,
      "course_id":53415
   },
   {
      "number":"BSMB-1003",
      "name":"Maschinengestaltung I (für Maschinenbauer 1. Sem.)",
      "qlearningid":"None",
      "originator":"None",
      "active":1,
      "copyright_warning":0,
      "users_count":5748,
      "has_joined":false,
      "share_link":"https://www.studydrive.net/de/course/maschinengestaltung-i-fuer-maschinenbauer-1-sem-/53416?ref=1657548",
      "email_body":"",
      "email_subject":"Melde dich auch bei Studydrive an",
      "university_id":800,
      "course_id":53416
   },
   {
      "number":"BSMB-1102",
      "name":"Grundzüge der Chemie",
      "qlearningid":"None",
      "originator":"None",
      "active":1,
      "copyright_warning":0,
      "users_count":5514,
      "has_joined":false,
      "share_link":"https://www.studydrive.net/de/course/grundzuege-der-chemie/53418?ref=1657548",
      "email_body":"",
      "email_subject":"Melde dich auch bei Studydrive an",
      "university_id":800,
      "course_id":53418
   }
]
```

### register
Parameters:
 - Email
 - Password

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
print(api.register("email", "password"))
```
Output:
```json
{
   "access_token":"***",
   "refresh_token":"***",
   "token_type":"Bearer",
   "expires_in":5184000
}
```

### setNickname
Sets your nickname

Parameters:
 - Nickname

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.login("email", "password")
print(api.setNickname("your Nickname"))
```
Output:
```json
{
   "nickname":"your Nickname"
}
```

### setProgram
Sets your university, programm and starting semester. Useful after registering. You can get these IDs from the following functions: getUniversities, getAllMajors, getSemester

Parameters:
 - universityID
 - programID
 - semesterID

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.login("email", "password")
print(api.setProgram(universityID = 800, programID = 619, semesterID = 45))
```
Output: no output

### getUniversities
Gets all universities

Parameters: no parameters

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.login("email", "password")
print(api.getUniversities()[0:5]) # the [0:5] is just to reduce the output
```
Output:
```json
[
   {
      "university_id":800,
      "name":"RWTH Aachen",
      "city":"Aachen",
      "country":"Germany",
      "country_id":64,
      "image":"Uni_Aachen.jpg",
      "active":1,
      "st_active":1,
      "description":"None",
      "users_count":91598,
      "degree_program_count":282,
      "synonyms":"RWTH Aachen,RWTH,RWTH Aachen University"
   },
   {
      "university_id":380,
      "name":"Maastricht University",
      "city":"Maastricht",
      "country":"Netherlands",
      "country_id":121,
      "image":"Uni_Maastricht.jpg",
      "active":1,
      "st_active":1,
      "description":"None",
      "users_count":79351,
      "degree_program_count":366,
      "synonyms":"Universiteit Maastricht,UM,Uni Maastricht,Maastricht University,University of Maastricht,University Maastricht,Universitie Maastricht,Universiti Maastricht,University Mastricht,Universitie Mastricht,Universiteit van Maastricht,Universiteit van Mastricht,Universitie of Maastricht,Universiti of Maastricht,University of Mastricht,Universitie of Mastricht,Universiteit Mastricht,Universiteit Maastricht,Maastricht Universitie,Maastricht Universiti,Maastricht Universiteit,Mastricht Universiteit,Mastricht Universitie,Mastricht University,Mastricht Universiti"
   },
   {
      "university_id":483,
      "name":"Universität Wien",
      "city":"Wien",
      "country":"Austria",
      "country_id":10,
      "image":"Uni_Vienna.jpg",
      "active":1,
      "st_active":1,
      "description":"None",
      "users_count":56959,
      "degree_program_count":299,
      "synonyms":"Universität Wien,Uni Wien,University of Vienna"
   },
   {
      "university_id":895,
      "name":"Universität Duisburg-Essen",
      "city":"Duisburg, Essen",
      "country":"Germany",
      "country_id":64,
      "image":"Uni_Duisburg.jpg",
      "active":1,
      "st_active":1,
      "description":"None",
      "users_count":48558,
      "degree_program_count":239,
      "synonyms":"Universität Duisburg-Essen,UDE,Uni Duisburg-Essen,University of Duisburg-Essen"
   },
   {
      "university_id":1058,
      "name":"Technische Universität München",
      "city":"München",
      "country":"Germany",
      "country_id":64,
      "image":"Uni_Munich.jpg",
      "active":1,
      "st_active":1,
      "description":"None",
      "users_count":39488,
      "degree_program_count":207,
      "synonyms":"Technische Universität München,Technical University Munich,TU München,TUM"
   }
]
```

### getSemester
Gets all semesters

Parameters: no parameters

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.login("email", "password")
print(api.getSemester()[0:5]) # the [0:5] is just to reduce the output
```
Output:
```json
[
   {
      "id":1,
      "semester":0,
      "year":2000,
      "display_name":"Im Herbst 1999 (WS 99/00)",
      "display_name_short":"WS1999",
      "display_field":"Winter 1999/00",
      "display_field_since":"seit Herbst 1999 (WS 99/00)"
   },
   {
      "id":2,
      "semester":1,
      "year":2000,
      "display_name":"Im Frühjahr 2000 (SS 2000)",
      "display_name_short":"SS2000",
      "display_field":"Sommer 2000",
      "display_field_since":"seit Frühjahr 2000 (SS 2000)"
   },
   {
      "id":3,
      "semester":0,
      "year":2001,
      "display_name":"Im Herbst 2000 (WS 00/01)",
      "display_name_short":"WS2000",
      "display_field":"Winter 2000/01",
      "display_field_since":"seit Herbst 2000 (WS 00/01)"
   },
   {
      "id":4,
      "semester":1,
      "year":2001,
      "display_name":"Im Frühjahr 2001 (SS 2001)",
      "display_name_short":"SS2001",
      "display_field":"Sommer 2001",
      "display_field_since":"seit Frühjahr 2001 (SS 2001)"
   },
   {
      "id":5,
      "semester":0,
      "year":2002,
      "display_name":"Im Herbst 2001 (WS 01/02)",
      "display_name_short":"WS2001",
      "display_field":"Winter 2001/02",
      "display_field_since":"seit Herbst 2001 (WS 01/02)"
   }
]
```

### getMyself
Gets all semesters

Parameters: no parameters

Example:
```python
from studydrive import studydriveapi 

api = studydriveapi.StudydriveAPI()
api.login("email", "password")
print(api.getMyself())
```
Output:
```json
{
   "userid":1657548,
   "uuid":"445436bc-576c-11ec-9486-02ac8496f080",
   "email":"***",
   "credentials_converted":1,
   "first_name":"Lea",
   "last_name":" ",
   "username":"",
   "gender":"f",
   "local":"de",
   "facebookid":"None",
   "googleid":"None",
   "appleid":"None",
   "graduation":"None",
   "graduation_new":"None",
   "verified":1,
   "registered":"2020-03-03 10:47:02",
   "lastactive":"2022-06-03 21:49:07",
   "hasuploaded":1,
   "referal":1494802,
   "ranking":"None",
   "created_at":"2020-03-03 10:47:02",
   "updated_at":"2022-06-04 15:21:01",
   "description":"",
   "points":0,
   "karma_points":5606,
   "profile_picture_id":406454,
   "role_id":4,
   "slug":"lea",
   "has_special_position":0,
   "former_cm":0,
   "former_ke":0,
   "semester_id":41,
   "userip":"***",
   "ban_id":"None",
   "deleted_at":"None",
   "has_admin_rights":false,
   "signup_method":"email",
   "credit_points":3196,
   "can_skip_verification":true,
   "disable_consent_management_android":false,
   "disable_consent_management_ios":false,
   "disable_smartlook_android":false,
   "degree_prgrams":[
      {
         "id":25816,
         "university_id":800,
         "degree_type_id":1,
         "user_id":1056069,
         "name":"Wirtschaftswissenschaften",
         "major_fixed_ids":"1",
         "regular_duration":"None",
         "start_semester":"None",
         "ws_start":"None",
         "ws_end":"None",
         "ss_start":"None",
         "ss_end":"None",
         "active":1,
         "created_at":"2018-12-04 22:23:13",
         "updated_at":"2018-12-05 09:36:34",
         "pivot":{
            "user_id":1657548,
            "degree_program_id":25816,
            "created_at":"2022-01-03 16:12:46",
            "updated_at":"2022-01-03 16:12:46"
         }
      }
   ],
   "majors":[
      {
         "id":1,
         "category":"Business Sciences",
         "subcategory":"Business Administration (General)",
         "studycrowd_id":1,
         "category_id":0,
         "de_category":"Wirtschaftswissenschaften",
         "de_subcategory":"Betriebswirtschaftslehre (BWL) allgemein",
         "slug_major":"business-sciences",
         "slug_submajor":"business-administration-general",
         "pivot":{
            "userid":1657548,
            "majorid":1,
            "primary":1
         }
      }
   ],
   "logins":83,
   "semesters":[
      {
         "semester":0,
         "year":2020
      }
   ],
   "course_expert_status":"",
   "newsletter":1,
   "newsletter_partner":1,
   "universities":[
      {
         "university_id":800,
         "name":"RWTH Aachen",
         "city":"Aachen",
         "country":"Germany",
         "image":"Uni_Aachen.jpg",
         "active":1,
         "st_active":1,
         "description":"None",
         "country_id":64,
         "users_count":91598,
         "degree_program_count":282
      }
   ],
   "run_group_targeting":false,
   "full_name":"Lea",
   "avatar_picture":"https://www.studydrive.net/images/avatars/karma/thumb/dog.png",
   "avatar_picture_large":"https://www.studydrive.net/images/avatars/karma/big/dog.png",
   "picture":"https://cdn.studydrive.net/d/prod/uploads/img/profile_pictures/thumb/1657548.jpg",
   "picture_large":"https://cdn.studydrive.net/d/prod/uploads/img/profile_pictures/big/1657548.jpg",
   "is_ke":false,
   "role":{
      "id":4,
      "name":"user",
      "created_at":"-0001-11-30 00:00:00",
      "updated_at":"-0001-11-30 00:00:00"
   },
   "verification_popup":"None",
   "positions":[
      
   ]
}
```