from weather import WeatherResponse

test_key = {
            '/start':"Hello!\n\nI'm a simple bot for weather forecast in Yaroslavl. "
                     "Type me any date (within 15 days) in the format `DD/MM`. Also"
                     " you can use `today` and `tomorrow`.\n\n"
                     "I'll be happy to help you 😇"
            }

class MessageResponse:

    response = 'Wrong data format. Type in DD/MM format please.'

    def __init__(self, message):
        self.text = message.text
        self.author = message.from_user.id

    def AddResponse(self):
        check = self.text.lower().split('/')
        if len(check) == 2 and check[0].isdigit() and check[1].isdigit():
            self.Weather(int(check[0]), int(check[1]))

        elif check == ['today']:
            self.Weather(today=1)

        elif check == ['tomorrow']:
            self.Weather(tmrw=1)

        elif self.text in test_key.keys():
            self.response = test_key[self.text]

    def Weather(self, day=1, month=1, today=0, tmrw=0):
        r = WeatherResponse()
        if today: r.setToday()
        elif tmrw: r.setTmrw()
        else: r.setDate(day, month)

        if r.choice:
            self.response = f'Weather forecast for {r.getDate()} in Yaroslavl\n\n' \
                            f'Temperature: {r.choice["temp"]} °C\n' \
                            f'Relative Humidity: {r.choice["rh"]} %\n' \
                            f'Pressure: {r.choice["pres"]} mmHg\n' \
                            f'Probability of precipitation: {r.choice["pop"]} %'
        else:
            self.response = 'Wrong data. Please enter any date within 15 days from today.'