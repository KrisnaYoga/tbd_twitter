from pymongo import MongoClient
from nltk.tokenize import word_tokenize

client = MongoClient('mongodb+srv://made:madeadhi@cluster0.hgmqu.mongodb.net/dbTweet?retryWrites=true&w=majority')
db = client['dbTweet']
collection = db['tbTweet']

with open('./positive.txt') as f:
    positive_words = f.read().splitlines()

with open('./negative.txt') as f:
    negative_words = f.read().splitlines()

with open('hasil.tsv', mode='w', encoding='utf-8') as f:
    f.write('tweet\tsentimen\n')

    for data in collection.find():
        tokens = [token.lower() for token in word_tokenize(data['caption']) if token.isalpha()]

        total_positive = 0
        total_negative = 0

        for token in tokens:
            if token in positive_words:
                total_positive += 1
            elif token in negative_words:
                total_negative += 1

        if total_positive - total_negative > 0:
            f.write(f'{data["caption"]}\tPositif\n')
        elif total_positive - total_negative < 0:
            f.write(f'{data["caption"]}\tNegatif\n')
        else:
            f.write(f'{data["caption"]}\tNetral\n')
