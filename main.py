from pysentimiento import create_analyzer
from os import system
import json

leng = input('Select language(en/es): ')

sentiment_analyzer = create_analyzer(task="sentiment", lang=leng)

url = input('Video URL: ')
system(f'youtube-comment-downloader --url {url} --output comments.txt')

data = open('comments.txt','r')
sentimental_list = []

for line in data:
    text = json.loads(line)['text']
    sentimental_list.append(sentiment_analyzer.predict(text).output)

print(f'''
        Positivo: {round(sentimental_list.count('POS')/len(sentimental_list)*100, 2)}
        Neutral: {round(sentimental_list.count('NEU')/len(sentimental_list)*100, 2)}
        Negativo: {round(sentimental_list.count('NEG')/len(sentimental_list)*100, 2)}
    ''')
