import requests
import spacy
import time
import json
from bs4 import BeautifulSoup


"""
1 - Je dois arriver a récupérer les stories, recalculer que sur les nouvelles histoires
"""
class StoryParser:
    
    def __init__(self, stories_name, dataset_name):
        self.stories_name = stories_name
        self.stories = self._load_stories()
        self.dataset_name = dataset_name
        self.dataset = self._load_dataset()
        self.total_words = []
        self.total_words_count = 0
        
    # USEFULL FOR ANALYSE STORIES
    def parse_new_stories(self):
        nlp = spacy.load("fr_core_news_md")
        print(f"chargement spacy")
        for story in self.stories:
            if story["analyse"]:
                print(f"{story['title']} already analyze.")
                continue
            print(f"{story['title']} Parsing...")
            story_words = []
            words = story["words"].split(' ')
            self.total_words_count += len(words)
            for word in words:
                if '-' in word:
                    splitted_word = word.split('-')
                    for w in splitted_word:
                        story_words.append(w)
                elif "'" in word:
                    splitted_word = word.split("'")
                    story_words.append(splitted_word[1])
                else:
                    story_words.append(word)
            story["analyse"] = True
            story["words_count"] = len(words)
        
            doc = nlp(' '.join(story_words))
            for token in doc:
                if token.lemma_ not in self.dataset:
                    self.dataset[token.lemma_] = {
                        "type": token.pos_,
                        "total_count": 1,
                        "possibilities": {token.text: {"count": 1}}
                    }
                else:
                    self.dataset[token.lemma_]["total_count"] += 1
                    if token.text not in self.dataset[token.lemma_]["possibilities"]:
                        self.dataset[token.lemma_]["possibilities"][token.text] = {"count": 1}
                    else:
                        self.dataset[token.lemma_]["possibilities"][token.text]["count"] += 1


            self.total_words += story_words
        
        self._save_stories()
        self._save_dataset()
 
    def _get_known_words(self):
        known_words = {}
        for lemma, values in self.dataset.items():
            for word in values["possibilities"]:
                known_words[word] = lemma
        return known_words
    
    def _increase_count(self, lemma, word, nlp):
        doc = nlp(word)
        for token in doc:
            item = self.dataset[lemma]
            item["total_count"] += 1
            item["possibilities"][token.text]["count"] += 1
            
    def _add_words(self, words, nlp):
        doc = nlp(' '.join(words))
        for token in doc:
            if token.lemma_ not in self.dataset:
                self.dataset[token.lemma_] = {
                    "type": token.pos_,
                    "total_count": 1,
                    "possibilities": {token.text: {"count": 1}}
                }
            else:
                self.dataset[token.lemma_]["total_count"] += 1
                if token.text not in self.dataset[token.lemma_]["possibilities"]:
                    self.dataset[token.lemma_]["possibilities"][token.text] = {"count": 1}
                else:
                    self.dataset[token.lemma_]["possibilities"][token.text]["count"] += 1
                       
    def _load_dataset(self):
        try:
            print(f"UPDATE: {self.dataset_name}")
            with open(f"data/{self.dataset_name}.json", "r", encoding="utf-8") as f:
                print("dataset load successfully.")
                return json.load(f)
        except FileNotFoundError as e:
            return {}
    
    def _save_dataset(self):
        with open(f"data/{self.dataset_name}.json", "w", encoding='utf-8') as f:
            json.dump(self.dataset, f, ensure_ascii=False, indent=2)
            
    def _load_stories(self):
        try:
            with open(f"data/{self.stories_name}.json", "r", encoding="utf-8") as f:
                print("stories load successfully.")
                return json.load(f)
        except Exception as e:
            print(f"ERROR during loading the stories: {e}")
    
    def _save_stories(self):
        with open(f"data/{self.stories_name}.json", "w", encoding='utf-8') as f:
            json.dump(self.stories, f, ensure_ascii=False, indent=2)
            
    # REPORT METHODS
    # - créer rapport pour avoir tous les noms
    def create_report(self):
        pass
            
if __name__ == "__main__":
    story_parser = StoryParser("fake_stories", "fake_dataset")
    story_parser.parse_new_stories()