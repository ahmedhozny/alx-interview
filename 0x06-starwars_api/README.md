# Star Wars API

The purpose of this script is to print the names of all characters from a specified Star Wars movie. The script takes a movie ID as a command-line argument, fetches data from the Star Wars API (SWAPI), and retrieves the list of character URLs for that movie. It then makes individual requests to obtain each character's name and prints them in the same order as they appear in the API. This is achieved by using Promises to handle asynchronous HTTP requests, ensuring that all character names are collected and displayed sequentially.
