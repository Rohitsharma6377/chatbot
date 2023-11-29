from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

# using search on Google to get answers
def get_google_answer(query):
    try:
        search_url = f"https://www.bing.com/search?={query}"
        response = urlopen(search_url)
        soup = BeautifulSoup(response.read(), 'html.parser')
        answers = []
        for g in soup.find_all('div', class_='g'):
            answer = ''.join([str(text) for text in g.find_all('span', class_='st')])
            answers.append(answer)
        if answers:
            return random.choice(answers)
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == 'bye':
        return 'Bye!'
    elif re.search('(.*)?(search|find)(.*)?', user_input):
        search_query = re.sub('(.*)?(search|find)(.*)?', '', user_input)
        return get_google_answer(search_query) or 'Sorry, I couldn\'t find an answer to that.'
    else:
        return 'I\'m not sure how to help with that.'

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot_response(user_input)
    print("Chatbot: " + response)