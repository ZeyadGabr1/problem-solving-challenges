from datetime import datetime


def timeConversion(time: str):
    
    time_object = datetime.strptime(time, "%I:%M:%S%p")
    return time_object.strftime("%H:%M:%S")


if __name__ == "__main__":
    time = input("")
    print(timeConversion(time))