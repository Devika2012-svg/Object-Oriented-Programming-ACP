class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter your message: ")

    def print_message(self):
        print("Uppercase message:", self.message.upper())

class HelperSession:
    def __init__(self):
        print("Helper session created!")

    def __del__(self):
        print("Helper session ended!")

def create_session():
    print("Making helper session..")
    session = HelperSession()
    print("Session is ready!")
    return session

class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}
        for index, number in enumerate(numbers):
            needed_number = target - number
            if needed_number in lookup:
                return (lookup[needed_number], index)
            lookup[number] = index

        return None
    
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()

session = create_session()

numbers = [10, 20, 30, 40, 50, 60, 70]

target_value = int(input("Enter target sum to search: "))
result = PairFinder().find_pair(numbers, target_value)

if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No pair found!")
del session
