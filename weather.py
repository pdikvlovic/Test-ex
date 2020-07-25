import requests, time
from datetime import date, datetime
from cn import getWeather

months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

class WeatherResponse:

    def __unixToStandart(self, timestamp):
        value = datetime.fromtimestamp(timestamp)
        date = [value.year, value.month, value.day]
        return date

    def __init__(self):
        unix = time.mktime(datetime.now().timetuple())
        dd = self.__unixToStandart(unix)

        self.__today = int(datetime(dd[0], dd[1], dd[2], 0, 1, 0).timestamp())
        self.__weather = getWeather()
        self.__limit = 1296000

        self.choice = None

    def __incYear(self, ch):
        dd = self.__unixToStandart(ch)
        dd[0] += 1
        return int(datetime(dd[0], dd[1], dd[2], 0, 1, 0).timestamp())

    def setDate(self, day, month):
        year = self.__unixToStandart(self.__today)[0]
        choice = int(datetime(year, month, day, 0, 1, 0).timestamp())

        if choice < self.__today:
            choice = self.__incYear(choice)

        if (choice - self.__today) > self.__limit:
            return
        else:
            self.choice = self.__weather[choice]

    def getDate(self):
        now = self.__unixToStandart(self.choice['ts'])
        day = now[-1]
        month = months[now[-2]]
        year = now[-3]
        return f'{day} {month} {year}'

    def setToday(self):
        self.choice = self.__weather[self.__today]

    def setTmrw(self):
        tmrw = self.__today + 86400
        self.choice = self.__weather[tmrw]