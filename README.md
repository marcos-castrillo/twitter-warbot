# Twitter Warbot [![CircleCI](https://circleci.com/gh/marcos-castrillo/twitter-warbot.svg?style=shield)](https://circleci.com/gh/marcos-castrillo/twitter-warbot)
## Simulate your own custom war!
![preview](https://user-images.githubusercontent.com/28508893/101995454-2f539800-3cca-11eb-89d1-407f18907293.png)  

Intro TODO

# Dependencies
- pip
- twitter
- pillow
- emoji

## Instructions
Install the dependencies using [Pip](https://pypi.org/project/pip/):

````pip install -r requirements.txt````

A [Twitter app](https://developer.twitter.com/en/portal/projects-and-apps) is required to first download the profile images of the users and later to publish the tweets for you.  
After creating it, copy and rename /data/secrets.bak.py to /data/secrets.py:

````cp /data/secrets.bak.py /data/secrets.py````

Fill it with your own keys and secrets.  
You're ready to start simulating wars!

````./start.py````

## Customization
TODO
