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

    def modifyYear(n, year):
        # Convert the year to its text representation
        year_str = str(year)

        # Get the first two characters of the year text representation
        first_two_chars = year_str[:2]

        # Get the odd positioned characters of the year text representation
        odd_chars = year_str[::2]

        # Multiply the first two characters and odd characters by n
        modified_first_two_chars = first_two_chars * n
        modified_odd_chars = odd_chars * n

        # Concatenate the modified parts
        result = modified_first_two_chars + modified_odd_chars

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