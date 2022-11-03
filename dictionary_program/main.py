# create a function that connects to api of dictionary and returns the meaning of the word

import requests
import json
# make a greeting message for the opening of the program
print('='*50)
print("Welcome to the dictionary")


def getMeaning(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word
    response = requests.get(url)
    data = json.loads(response.text)
    mean = data[0]['meanings']
    return list_meanings(mean)

def list_meanings(mean):
    meanings = []
    for i in range(len(mean)):
        meanings.append(mean[i]['definitions'][0]['definition'])
    return meanings

#create a loop that asks for input and returns the meanings of the word
while True:

    word = input("Enter a word: ")
    meaning = getMeaning(word)
    # print the meaning list in a readable format
    print("Meanings of the word: ")
    for i in range(len(meaning)):
        print(f"{i+1}. {meaning[i]}")
    
    # ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice == 'n':
        break
    # add a '='*50 to make the output more readable
    print("="*50)

print("Thank you for using the dictionary")


