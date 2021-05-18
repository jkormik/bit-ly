# Bitly url shorterer

It is a console programm for fast shortening of long knotty urls based on a Bitly API, which also can give you an information about a sum of clicks on your bitlinks.

### How to install

You will need to sign in bitly.com (free account is ehough) and get a Generic Access Token.

Generic Access Token is generated in a dashboard of your account.

1. Click on a profile name in an upper right corner
2. Choose a PROFILE SETTINGS option in a menu
3. Choose a Generic Access Token option inside profile settings
4. Choose an API group and enter correct password

You will recieve a Generic Access Token wich will look something like that "123456789009876543212345678909875zxdt876".

Put this token inside quotation marks in a file .env:
```
BITLY_OAUTHACCESSTOKEN="6e2a0ee7011166b05356f944dd82dfc2725bf50a"
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).