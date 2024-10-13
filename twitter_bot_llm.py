import tweepy
import google.generativeai as genai
import os

# Replace with your Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authenticate to Twitter   
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Connect to Gemini
genai.configure(api_key="")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Define the bot's function (e.g., tweeting a message)
def tweet_message():
    # api.update_status(message
    
    response = model.generate_content("Status of Mumbai-Ahmedabad high speed rail project in 140 characters.")
    print(response.text)
    
    client.create_tweet(text=response.text[:140])

tweet_message()
