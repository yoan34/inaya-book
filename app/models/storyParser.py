import spacy
import json
import os
from collections import defaultdict

from app.tools.enumerators import WordType


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
                print(f"{token.text}: {token.morph}")
                if token.lemma_ not in self.dataset:
                    self.dataset[token.lemma_] = { 
                        "type": token.pos_,
                        "total_count": 1,
                        "img": "",
                        "variants": {token.text: {"count": 1}}
                    }
                else:
                    self.dataset[token.lemma_]["total_count"] += 1
                    if token.text not in self.dataset[token.lemma_]["variants"]:
                        self.dataset[token.lemma_]["variants"][token.text] = {"count": 1}
                    else:
                        self.dataset[token.lemma_]["variants"][token.text]["count"] += 1


            self.total_words += story_words
        
        self._save_stories()
        self._save_dataset()
          
    def _load_dataset(self):
        try:
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
         
    def parse_nouns_with_image(self):
        path = os.path.dirname(os.path.dirname(__file__))
        nouns = os.listdir(f"{path}/src/img/nouns")
        nouns = [noun.split('.')[0] for noun in nouns]
        print(nouns)

    # REPORT METHODS
    # - créer rapport pour avoir tous les noms
    
    def create_report_of_word_type(self, word_type: WordType):
        words = self.get_word_in_dataset(word_type=word_type, only_lemma=False)
        file_path = self._build_path(folder='reports', filename=f"total_{word_type.value}.txt")

        with open(file_path, "w") as f:
            words = list(sorted(words, key=lambda x: x[1], reverse=True))
            print(file_path)
            for word, count in words:
                f.write(f"{word}={count}\n")
                
    def create_syllabes_report(self):
        syllabes = []
        for lemma, values in self.dataset.items():
            if "syllabes" in values:
                syllabes.append(values["syllabes"])
            for variant, v in values["variants"].items():
                if "syllabes" in v:
                    syllabes.append(v["syllabes"])
        syllabes = [syllabes for c in syllabes for syllabes in c.split('-')]
        result = defaultdict(int)
        for syllabe in syllabes:
            result[syllabe] += 1
        result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        file_path = self._build_path(folder='reports', filename=f"syllabes.txt")
        with open(file_path, "w") as f:
            for syllabe, count in result:
                f.write(f"{syllabe}={count}\n")
                
    def create_word_by_syllabes_report(self):
        syllabes = []
        for lemma, values in self.dataset.items():
            if "syllabes" in values:
                syllabes.append(values["syllabes"])
            for variant, v in values["variants"].items():
                if "syllabes" in v:
                    syllabes.append(v["syllabes"])
        syllabes.sort()

        file_path = self._build_path(folder='reports', filename=f"syllabes.txt")
        with open(file_path, "w") as f:
            current = syllabes[0].split('-')[0]
            for syllabe in syllabes:
                if current == syllabe.split('-')[0]: 
                    f.write(f"{syllabe}\n")

                
                
    def _build_path(self, folder: str, filename: str):
        current_script_path = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_script_path)
        new_path =  os.path.join(parent_directory, folder)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        return os.path.join(new_path, filename)
        
    def get_word_in_dataset(self, word_type: WordType, only_lemma=True):
        words = []
        for lemma, values in self.dataset.items():
            if values['type'] == word_type.value:
                if only_lemma:
                    words.append((lemma, values['total_count']))
                else:
                    for variant, item in values['variants'].items():
                        words.append((variant, item['count']))
        return words
            
if __name__ == "__main__":
    story_parser = StoryParser("all_stories", "dataset_stories")
    story_parser.create_word_by_syllabes_report()
    

    
    