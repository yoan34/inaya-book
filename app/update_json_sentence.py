import json
import os


filenames = [
    'articles indefinis.json',
    'articles definis.json',
    'adjectifs demonstratifs.json',
    'adjectifs possessifs pluriel.json',
    'adjectifs possessifs troisieme personne.json',
    'adjectifs possessifs deuxieme personne.json',
    'adjectifs possessifs premiere personne.json',
    'articles partitifs.json',
    ]

nouns_to_remove = os.listdir("app/src/img/erase_nouns")
nouns_to_remove = [noun.split('.')[0] for noun in nouns_to_remove]

for filename in filenames:
    with open(f"app/sentences/{filename}", 'r') as f:
        data = json.load(f)

    new_sentences = []
    for sentence in data["sentences"]:
        keep_sentence = True
        for noun_remove in nouns_to_remove:
            if noun_remove in sentence:
                keep_sentence = False
                break
        if keep_sentence:
            new_sentences.append(sentence)
                
    print(f"{filename}  sentence to keep {len(new_sentences)}/{len(data['sentences'])}")

    with open(f"app/sentences/{filename}", 'w') as f:
        data["sentences"] = new_sentences
        json.dump(data, f, indent=4, ensure_ascii=False)