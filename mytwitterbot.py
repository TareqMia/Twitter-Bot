# mytwitterbot.py
# IAE 101, Fall 2019
# Project 02 - Building a Twitterbot
# Name: Tareq Mia      
# netid: TMIA   


import sys
import simple_twit
import requests



def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    api = simple_twit.create_api()
    # YOUR CODE BEGINS HERE
    
    name = "tmia_IAE101"
    
    user = simple_twit.get_user(api, name)
    
    time_line = simple_twit.get_user_timeline(api,name, count = 5)
    home_time_line = simple_twit.get_home_timeline(api, count = 5)


    #weather bot
    key = "440cb9d576a4f8df23fb00a4e3a2dde2"
    latitude = "40.916168"
    longitude = "-73.118309"
    url = f"https://api.darksky.net/forecast/{key}/{latitude},{longitude}"
    data = requests.get(url).json()
    
    currently = data['currently']["summary"]
    current_temp = data['currently']['temperature']
    try:
        precipitation = data["currently"]["precipType"]
    except KeyError:
        pass
    precipitation_probability = str(
        data["currently"]["precipProbability"] * 100)
    
    if float(precipitation_probability) in [100, 100.0]:
        try:
            message = f"Currently in Stony Brook: {currently} with a temperature of {current_temp}°F\nPrecipitation probability: {precipitation_probability}%\nAnd now a word from Ollie: "
        except KeyError:
            pass
        tweet = simple_twit.send_media_tweet(api, message, "ollie_raining_sideways.jpg")
        thanks = simple_twit.send_tweet(api, "Thanks Ollie.")
    
    elif float(precipitation_probability) in range(50,100):
        try:
            message = f"Curreently: {currently} with a temperature of {current_temp}°F\nPrecipitation probability: {precipitation_probability}%"
        except KeyError:
            pass
        tweet = simple_twit.send_media_tweet(api, message, "ollie.jpg")
        
        thanks = simple_twit.send_tweet(api, "Thanks Ollie.")
    
    else:
        message = f"Currently in Stony Brook: {currently} with a temperature of {current_temp}°F\nPrecipitation probability: {precipitation_probability}%"
        tweet = simple_twit.send_tweet(api, message)
    
    
        
    
    
    

    
    simple_twit.version()
    

if __name__ == "__main__":
       main()
