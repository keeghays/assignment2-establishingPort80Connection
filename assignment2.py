import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        birth_year = currentYear - self.year
        print(f'Your age is {birth_year}')

    def listAnniversaries(self):
        current_year = 2022
        anniversaries = []
        for i in range(1, 11):
            anniversary = current_year - self.year + (i * 10)
            anniversaries.append(anniversary)
        return anniversaries

    def modifyYear(self, n):
        year_str = str(self.year)
        result = year_str[:2] * n + year_str[-2:] * n
        return result

    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower():
            return False
        digits = 0
        for char in string:
            if char.isdigit():
                digits += 1
        if digits != 1:
            return False
        return True

    @staticmethod
    def connectTcp(host, port):
        try:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except Exception as e:
            return False

# Example usage:
a = Assignment2(2000)
a.tellAge(2023)

ret = a.listAnniversaries()
print(ret)

modified_year = a.modifyYear(5)
print(modified_year)

print(Assignment2.checkGoodString("f1obar0more"))
print(Assignment2.checkGoodString("foobar0more"))

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")

