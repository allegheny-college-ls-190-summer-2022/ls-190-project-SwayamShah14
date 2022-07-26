import json
import tweepy

def load_keys():
    """Load keys file"""
    # Find the file and open it
    file = open("../.secrets/keys.json")
    # Parse JSON
    keys = json.load(file)
    # Return results
    return keys

def tweet(message):
    """Handles authentication and tweeting."""
    # Get keys from file
    keys = load_keys()
    # "Log in"
    auth = tweepy.OAuthHandler(keys["API"], keys["API_SECRET"])
    auth.set_access_token(keys["ACCESS"], keys["ACCESS_SECRET"])
    api = tweepy.API(auth)
    # Post message
    api.update_status(message)

def main():
    """Entry point"""
    pass # Delete this line when adding your own code

if __name__ == "__main__":
    main()
