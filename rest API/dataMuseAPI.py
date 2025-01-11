import requests
import json


#The Datamuse API is a word-finding query engine for developers.
#You can use it in your apps to find words that match a given set of constraints and that are likely in a given context.
#You can specify a wide variety of constraints on meaning, spelling, sound, and vocabulary in your queries, in any combination.
#https://www.datamuse.com/api/

# This block will only execute if this file is run directly, not if it's imported
if __name__ == "__main__":
    def get_rhymes(word):
        # Base URL for the Datamuse API
        baseurl = "https://api.datamuse.com/words"

        # Dictionary to store query parameters
        param_dict = {}

        # Add the word to find rhymes for to the parameters
        param_dict['rel_rhy'] = word

        # Set the maximum number of results to 3
        param_dict['max'] = 3

        # Send a GET request to the Datamuse API with the specified parameters
        resp = requests.get(baseurl, params=param_dict)

        # Parse the JSON response into a Python object (a list of dictionaries)
        word_ds = resp.json()

        # Extract the 'word' value from each dictionary in the list and return the list of words
        return [d['word'] for d in word_ds]
        # Alternatively, just return the JSON response (commented out)
        # return resp.json()


    # Print the list of rhymes for the word "funny"
    print(get_rhymes("funny"))
