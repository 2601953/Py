class user:
    # Constructor
    def __init__(self, name, age, uni, course, hobby):
        self._name = Standardise(name)
        self._age = age
        self._uni = uni.upper()
        self._course = course.upper()
        self._hobby = hobby

    def DisplayInfo(self):
        print(f"Name: {self._name}\nAge: {self._age}\nUniversity: {self._uni}\nCourse: {self._course}\nHobby: {self._hobby}")

# Standardise a given string
def Standardise(content):
    return content.lower().capitalize()

# New user object
user1 = user("sam", 19, "CHI", "CS", "programming")

user1.DisplayInfo()

# This comment changed my file