# Astrologer Talks

Astrologer Talks is a python application that integrates with the chatgpt's openai to predict your horoscope based on your name and zodiac sign.
You should be either logged in as a registered user (pass your generated jwt token from login as auth header) or you should provide your name and zodiac sign in query params to view your horoscope for today
The application is hosted [here](https://astrology-talks.onrender.com/docs#)

You can try the hosted application here:
1. Register [POST] - https://astrology-talks.onrender.com/api/v1/user/register
2. Login [POST] - https://astrology-talks.onrender.com/api/v1/user/login
3. View Horoscope [GET] - https://astrology-talks.onrender.com/api/v1/horoscope/?name=John&zodiac_sign=Aries

## Running Locally
You can run and test the application locally in following ways
- using docker container
- running script manually in your terminal

### Using Docker Container

Using the following command, will run the application on port 4001
```
docker-compose build
docker-compose up -d
```

### Running Script Manually In Your Terminal
Using the following command, will run the application on port 4000
```
python main.py
```

