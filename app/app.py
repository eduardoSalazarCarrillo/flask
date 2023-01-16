#!/usr/bin/env python3
from flask import Flask
from collections import Counter
import logging 
import json
import sys

app = Flask(__name__)

@app.route('/palindrome/<word>', methods = ['GET'])
def palindrome(word):
    logging.info("Word received: [" +  str(word)  + "]")
    jsonResponse = buildJSON(word)
    logging.info("JSON obtained: {" + jsonResponse +"}")

    return jsonResponse

# Function that checks if its is a palindrome
def isPalindrome(string2):
    return string2 == string2[::-1]

def buildJSON(word):
    # Receiving user string
    string = word
    
    # By converting all characters to lowercase
    string2 = string.lower()
    string2 = string2.replace(",", "")
    string2 = ''.join(string2.split())

    # Using the isPalindeome function
    ans = isPalindrome(string2)
    # Formatting depending on the conditional
    if ans:
            MyList = list(string2)
            my_dict =  dict(Counter(MyList))
            length = len(string)
            my_dictionary = {"name": string, "palindrome": True}
            my_dictionary["sorted"] = my_dict
            my_dictionary["length"] = length
            json_object = json.dumps(my_dictionary, indent = 4)
            return json_object
    else:
            my_dictionary = {"name": string, "palindrome": False}
            json_object = json.dumps(my_dictionary, indent = 4)
            return json_object

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='0.0.0.0', port=8080, debug=True)
# [END gae_flex_quickstart]
