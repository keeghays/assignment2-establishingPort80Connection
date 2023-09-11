import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f"Your age is {age}")

    def listAnniversaries(self):
        today = 2022
        anniversaries = []
        for i in range(10, 101, 10):
            if self.year + i <= today:
                anniversaries.append(i)
        return anniversaries

    def modifyYear(self, n):
        year_str = str(self.year)
        result = year_str[:2] * n  # n times the first two characters

        # Extract and multiply the odd-positioned characters
        odd_chars = year_str[1::2]
        odd_chars_multiplied = "".join([char * n for char in odd_chars])

        result += odd_chars_multiplied

        return result

    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower() or not string[0].isalpha():
            return False
        digit_count = sum(1 for char in string if char.isdigit())
        if digit_count != 1:
            return False
        return True

    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)  # Set a timeout for the connection attempt
                s.connect((host, port))
                return True
        except (socket.timeout, ConnectionRefusedError):
            return False

# Example usage:
a = Assignment2(2000)
a.tellAge(2023)
ret = a.listAnniversaries()
print(ret)

a = Assignment2(1782)
ret = a.modifyYear(3)
print(ret)

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.connectTcp("www.google.com", 80)
if ret:
    print("Connection established correctly")
else:
    print("Some error")

