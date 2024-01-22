import requests
import spacy
import time
import json


from bs4 import BeautifulSoup

with open('all_stories.json', 'r', encoding='utf-8') as f:
    all_stories = json.load(f)
    

nlp = spacy.load("fr_core_news_md")
all_words = {}
total_words = []
total_words_count = 0
total_words_spacy = {}
for story in all_stories:
    print(f"-----{story['title']}-----")
    print(f"   {story['age']}")
    words = story["words"].split(' ')
    total_words_count += len(words)
    print(f"   words = {len(words)}")
    print(f"   {'Already analyse' if story['analyse'] else 'to be analyse'}")

    if not story["analyse"]:


        for word in words:
            if '-' in word:
                splitted_word = word.split('-')
                for w in splitted_word:
                    total_words.append(w)
            elif "'" in word:
                splitted_word = word.split("'")
                total_words.append(splitted_word[1])
            else:
                total_words.append(word)
        story["analyse"] = True
            
print(f"total words count with occurence: {total_words_count}")



total_words = ' '.join(total_words)
doc = nlp(total_words)
for token in doc:
    print(token)
    if token.lemma_ not in all_words:
        all_words[token.lemma_] = {"type": token.pos_, "count": 1, "possibilities": {token.text: {"count": 1}}}
    else:
        all_words[token.lemma_]["count"] += 1
        if token.text not in all_words[token.lemma_]["possibilities"]:
            all_words[token.lemma_]["possibilities"][token.text] = {"count": 1}
        else:
            all_words[token.lemma_]["possibilities"][token.text]["count"] += 1



all_words = dict(sorted(all_words.items(), key=lambda item: item[1]['count']))

# écrire le nouveau json avec l'attribut "analyse" qui change
with open('all_stories.json', 'w', encoding='utf-8') as f:
    json.dump(all_stories, f, ensure_ascii=False, indent=4)
    

total_word_analyse = 0
for lemma in all_words:
    total_word_analyse += len(all_words[lemma]['possibilities'])
for ind, lemma in enumerate(all_words):
    for word in all_words[lemma]["possibilities"]:
        url = f"https://www.silabas.net/index-fr.php?lang=/index-fr.php&p={word}&button=Séparées"
        try:
            response = requests.get(url)
            response.raise_for_status()  # génère une exception si la requête a échoué
            soup = BeautifulSoup(response.content, 'html.parser')

            syllables_div = soup.find('div', style="padding-left:1em;background-color:#f5f5ff;border-style:dashed;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;border: 0px dashed #dde0fc;")
            
            if syllables_div:
                syllables = syllables_div.find('font').text
                print(f"{syllables:<40} ({ind+1}/{len(all_words)})")
                all_words[lemma]["possibilities"][word]["syllables"] = syllables
            else:
                print(f"Erreur lors de la récupération des syllabes pour le mot '{word}'")
        except requests.RequestException as e:
            print(f"Erreur lors de la requête pour le mot '{word}': {e}")
        except Exception as e:
            print(f"Erreur lors du traitement du mot '{word}': {e}")
            
with open('dataset_stories.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_words, json_file, ensure_ascii=False, indent=4)
