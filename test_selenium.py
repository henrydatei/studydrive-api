from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import re
import math
from dataclasses import dataclass
import chromedriver_autoinstaller

@dataclass
class StudydriveSelenium:

    def __post_init__(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        self.driver.get('https://www.studydrive.net/')
        time.sleep(2)
        self.driver.execute_script(r'return document.querySelector("#usercentrics-root").shadowRoot.querySelectorAll("div div div div div")[29].querySelectorAll("button")[1]').click() # privacy policy

    def __getRegististrationLink__(self, username):
        allUrls = []
        params = {"username": username}
        response = requests.get("https://trashmailgenerator.de/backend.php", params = params)
        response.raise_for_status()
        for mail in response.json()["mails"]:
            html = mail["textHtml"]
            urls = re.findall(r'href=[\'"]?([^\'" >]+)', html)
            allUrls.extend(urls)
        for url in list(set(allUrls)):
            if "verify" in url:
                return url

    def login(self, username, password):
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[1]/div/div/nav/div/button[1]').click()
        self.driver.find_element("xpath", '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/input[1]').send_keys(username)
        self.driver.find_element("xpath", '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/input[2]').send_keys(password)
        self.driver.find_element("xpath", '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/div[3]/label').click()
        self.driver.find_element("xpath", '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/button[3]').click()
        time.sleep(1)
        self.cookies = self.driver.get_cookies()

    def register(self, username, password, gender = "m"):
        email = username + "@trashmailgenerator.de"
        
        # Email and Password
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[1]/div/div/nav/div/button[2]').click()
        self.driver.find_element("xpath", '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/input[1]').send_keys(email)
        self.driver.find_element("xpath", '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/input[2]').send_keys(password)
        self.driver.find_element("xpath", '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/button[3]').click()
        time.sleep(1)

        # Username and Gender
        self.driver.find_element("xpath", '//*[@id="username"]').send_keys(username)
        self.driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div').click()
        if gender == "m":
            self.driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/ul/div/div[1]').click() # männlich
        elif gender == "f":
            self.driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/ul/div/div[2]').click() # weiblich
        else:
            self.driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/ul/div/div[3]').click() # divers
        self.driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/button').click()
        time.sleep(1)
        
        # University and Couse
        self.driver.find_element("xpath", '//*[@id="vs1__combobox"]/div[1]/input').send_keys("RWTH Aachen")
        time.sleep(3)
        self.driver.find_element("xpath", '//*[@id="vs1__combobox"]/div[1]/input').send_keys(Keys.RETURN)
        self.driver.find_element("xpath", '//*[@id="vs2__combobox"]/div[1]/input').send_keys("Betriebswirtschaftslehre")
        time.sleep(2)
        self.driver.find_element("xpath", '//*[@id="vs2__combobox"]/div[1]/input').send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN) # BWL Doktor
        self.driver.find_element("xpath", '//*[@id="vs3__combobox"]/div[1]/input').click()
        time.sleep(2)
        self.driver.find_element("xpath", '//*[@id="vs3__combobox"]/div[1]/input').send_keys(Keys.DOWN, Keys.RETURN)
        self.driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/button').click()
        
        # Verify Email
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.__getRegististrationLink__(username))
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def getCorrectPath(driver: webdriver.Chrome, type: str, id: int):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(f"https://www.studydrive.net/de/{type}/test/{id}")
        correctPath = driver.current_url
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return correctPath

    def getCorrectPathQuestion(driver: webdriver.Chrome, id: int):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(f"https://www.studydrive.net/de/course/test/post/{id}/test")
        correctPath = driver.current_url
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return correctPath

    def downloadDocument(self, documentID):
        correctPath = self.getCorrectPath(self.driver, "doc", documentID)
        self.driver.get(correctPath)
        time.sleep(2)
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[1]/div/div/div[1]/div[2]/div[3]').click()

    # if called on a already liked document, the document will be unliked
    def likeDocument(self, documentID):
        correctPath = self.getCorrectPath(self.driver, "doc", documentID)
        self.driver.get(correctPath)
        time.sleep(2)
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[1]/div/div/div[1]/div[2]/div[1]').click()

    # if called on a already liked question, the question will be unliked
    def likeQuestion(self, questionID):
        correctPath = self.getCorrectPathQuestion(self.driver, questionID)
        self.driver.get(correctPath)
        time.sleep(2)
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[3]/div').click()

    # if called on a already liked answer, the answer will be unliked
    # answerPosition is the position of the answer in the list of answers (1 for the first answer, 2 for the second answer, etc.)
    # to get the position of the answer, use getInformationAboutQuestion()
    def likeAnswer(self, questionID, answerPosition):
        correctPath = self.getCorrectPathQuestion(self.driver, questionID)
        self.driver.get(correctPath)
        time.sleep(2)
        self.driver.find_element("xpath", f'//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[4]/div[{answerPosition}]/div[2]/div[2]/div/div').click()

    # type: "group" or "course"
    def createQuestion(self, text, type, id, anonymous = False):
        correctPath = self.getCorrectPath(self.driver, type, id)
        self.driver.get(correctPath)
        time.sleep(2)
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[3]/div/div/div[3]/section/div/div/div/div/form/div/div[2]/div[2]').click()
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[3]/div/div/div[3]/section/div/div/div/div[1]/form/div[1]/div[2]/div[2]/textarea').send_keys(text)
        if anonymous:
            self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[3]/div/div/div[3]/section/div/div/div/div[1]/form/div[1]/div[3]/button[1]').click() # anonym
        self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[3]/div/div/div[3]/section/div/div/div/div[1]/form/div[1]/div[3]/button[4]').click()

    # if you have previouisly answered the question (or created the question), you can't change the anonimity (well, technically you can, but I don't support that)
    def createAnswer(self, text, questionID, anonymous = False):
        correctPath = self.getCorrectPathQuestion(self.driver, questionID)
        self.driver.get(correctPath)
        time.sleep(2)
        # is nessesary because the text field is on another position when the question is unanswered
        try:
            self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[4]/div/form/textarea').send_keys(text)
            if anonymous:
                self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[4]/div/form/div/button[1]').click() # anonym
            self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[4]/div/form/div/button[3]').click()
        except:
            self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[5]/div/form/textarea').send_keys(text)
            if anonymous:
                self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[5]/div/form/div/button[1]').click() # anonym
            self.driver.find_element("xpath", '//*[@id="main-container"]/div[3]/div[2]/div/div/div[2]/div[5]/div/form/div/button[3]').click()

    def getInformationAboutQuestion(self, questionID):
        correctPath = self.getCorrectPathQuestion(self.driver, questionID)
        self.driver.get(correctPath)
        time.sleep(2)
        data = self.driver.execute_script(r'return sdWindow')
        return data

    def getCourseList(self):
        data = self.driver.execute_script(r'return sdWindow')
        return data["courses"]["data"]

    def getUsersDocuments(self, userID):
        documents = []
        # first page
        params = {"page": 1, "followed": False}
        header = {"X-Requested-With": "XMLHttpRequest"}
        r = requests.get("https://www.studydrive.net/profile/{}/documents".format(userID), params = params, headers = header)
        r.raise_for_status()
        meta = r.json()["meta"]
        documents.extend(r.json()["data"])
        numberOfPages = math.ceil(meta["total"]/meta["per_page"])
        # other pages
        for i in range(2, numberOfPages + 1):
            params = {"page": i, "followed": False}
            r = requests.get("https://www.studydrive.net/profile/{}/documents".format(userID), params = params, headers = header)
            r.raise_for_status()
            documents.extend(r.json()["data"])

        return documents

    # type 60 = Klausuren
    # type 30 = Übungen & Tutorien
    # type 80 = Zusammenfassungen
    # type 10 = Andere
    # type 20 = Vorlesungen
    def getCourseDocuments(self, courseID, filterDocumentType = None):
        documents = []
        # first page
        params = {"course_id": courseID, "content": "documents", "p": 1}
        if filterDocumentType != None:
            params["document_type[]"] = filterDocumentType
        header = {"X-Requested-With": "XMLHttpRequest"}
        r = requests.get("https://www.studydrive.net/get-search-results", params = params, headers = header)
        r.raise_for_status()
        documents.extend(r.json()["data"]["results"]["data"])
        numberOfPages = r.json()["data"]["results"]["last_page"]
        # other pages
        for i in range(2, numberOfPages + 1):
            params = {"course_id": courseID, "content": "documents", "p": i}
            if filterDocumentType != None:
                params["document_type[]"] = filterDocumentType
            r = requests.get("https://www.studydrive.net/get-search-results", params = params, headers = header)
            r.raise_for_status()
            documents.extend(r.json()["data"]["results"]["data"])

        return documents