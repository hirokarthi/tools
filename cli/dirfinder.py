#!/usr/bin/env python3


BANNER = """


 ____  _        _____ _           _           
|  _ \(_)_ __  |  ___(_)_ __   __| | ___ _ __ 
| | | | | '__| | |_  | | '_ \ / _` |/ _ \ '__|
| |_| | | |    |  _| | | | | | (_| |  __/ |   
|____/|_|_|    |_|   |_|_| |_|\__,_|\___|_|   

Coded by Mr.Karthikeyan!


"""

import requests
import argparse

def check_url(base_url, wordlist):
    for word in wordlist:
        # Construct the full URL by appending the word to the base URL
        full_url = f"{base_url}/{word}"

        try:
            # Send a GET request to the constructed URL
            response = requests.get(full_url)

            # Check if the response status code is 200 (OK)
            if response.status_code == 200:
                print(f"Success: The URL '{full_url}' is available on the server.")
            else:
                print(f"Failed: The URL '{full_url}' is not available.")
        except requests.RequestException as e:
            # Handle any exceptions that occur during the request
            print(f"Failed: Could not reach the URL '{full_url}'. Error: {e}")

def main():

    print(BANNER)
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Check if specific URLs are available on a server.')
    parser.add_argument('url', help='The base URL to check (e.g., https://example.com)')
    parser.add_argument('wordlist', nargs='+', help='A list of words to append to the base URL')

    # Parse the arguments
    args = parser.parse_args()

    # Run the URL check
    check_url(args.url, args.wordlist)

if __name__ == '__main__':
    main()
