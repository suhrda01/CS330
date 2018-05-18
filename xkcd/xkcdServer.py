from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/processform')
def procform():
    minWord = int(request.args.get('minWord'))
    maxWord = int(request.args.get('maxWord'))
    maxTotal = int(request.args.get('maxTotal'))
    words = []
    adjectives = []
    nouns = []
    verbs = []
    adverbs = []
    password = ""
    if request.args.get('grammar') == 'True':
        file = open("adjective.txt", "r")
        for line in file:
            line = line.strip('\n')
            if len(line) >= minWord and len(line) <= maxWord:
                adjectives.append(line)
        file.close()
        file = open("noun.txt", "r")
        for line in file:
            line = line.strip('\n')
            if len(line) >= minWord and len(line) <= maxWord:
                nouns.append(line)
        file.close()
        file = open("verb.txt", "r")
        for line in file:
            line = line.strip('\n')
            if len(line) >= minWord and len(line) <= maxWord:
                verbs.append(line)
        file.close()
        file = open("adverb.txt", "r")
        for line in file:
            line = line.strip('\n')
            if len(line) >= minWord and len(line) <= maxWord:
                adverbs.append(line)
        file.close()
        while True:
            adjective = random.choice(adjectives)
            noun = random.choice(nouns)
            verb = random.choice(verbs)
            adverb = random.choice(adverbs)
            password = adjective + noun + verb + adverb
            if len(password) <= maxTotal:
                if request.args.get('intReplace') == 'True':
                    password = password.replace("a","4")
                    password = password.replace("i","1")
                    password = password.replace('o','0')
                    password = password.replace('e','3')
                    password = password.replace('t','7')
                return render_template('password.html', password=password)
            else:
                password=''

    file = open("words.txt", "r")
    for line in file:
        line = line.strip('\n')
        if len(line) >= minWord and len(line) <= maxWord:
            words.append(line)
    file.close()
    while True:
        for i in range(4):
            word = random.choice(words)
            password += word
        if len(password) <= maxTotal:
            if request.args.get('intReplace') == 'True':
                password = password.replace("a","4")
                password = password.replace("i","1")
                password = password.replace('o','0')
                password = password.replace('e','3')
                password = password.replace('t','7')
            return render_template('password.html', password=password)
        else:
            password=''


if __name__ == '__main__':
    app.run(debug=True)