
import argparse
import requests
import json

# With this CLI based application, you can get the meaning of a word passed as argument


def getMeaning(word:str) -> list[str]:
    """Returns the meaning of the word passed as argument"""

    url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word
    response = requests.get(url)
    mean = json.loads(response.text)[0]['meanings']

    return [mean[i]['definitions'][0]['definition'] for i in range(len(mean))]

    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A dictionary program")
    parser.add_argument("word", help="The word to be searched")
    args = parser.parse_args()

    meaning = getMeaning(args.word)
    
    print(f'The meanings of the word "{args.word}" are:')
    [print(f"{i+1}. {meaning[i]}" ) for i in range(len(meaning))]
    

