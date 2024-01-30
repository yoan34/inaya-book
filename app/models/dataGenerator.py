import os
import json
import requests
import time
import ast
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from app.models.storyParser import StoryParser
from app.models.chatGPT import ChatGPT
from app.tools.constants import QUESTION_GENERATE_SENTENCES, CONTEXT_GENERATE_SENTENCES, CONTEXT_GENERATE_IMG
from app.tools.enumerators import WordType, GrammaticalCategory, Color, IllustratedPageCategory

load_dotenv()


class DataGenerator:

    NOUNS_WITH_IMG = [
        "prince",
        "pirate",
        "papa",
        "nuit",
        "sorcière",
        "princesse",
        "tête",
        "sirène",
        "maman",
        "dent",
        "maison",
        "fille",
        "ours",
        "oeil",
        "porte",
        "homme",
        "trésor",
        "main",
        "château",
        "bébé",
        "femme",
        "lit",
        "bateau",
        "roi",
        "enfant",
        "fée",
        "eau",
        "loup",
        "chevalier",
        "perroquet",
        "sac",
        "monstre",
        "baguette",
        "cheveu",
        "garçon",
        "fantôme",
        "souris",
        "pied",
        "pièce",
        "vague",
        "arbre",
        "fleur",
        "grotte",
        "forêt",
        "docteur",
        "oiseau",
        "bras",
        "fenêtre",
        "jardin",
        "jambe",
        "poisson",
        "cadeau",
        "table",
        "épaule",
        "soleil",
        "ogre",
        "reine",
        "troll",
        "ciel",
        "gâteau",
        "bol",
        "cuisine",
        "bois",
        "robe",
        "nuage",
        "salade",
        "collier",
        "lait",
        "vache",
        "coeur",
        "carrosse",
        "larme",
        "ourse",
        "pont",
        "île",
        "pomme",
        "rivière",
        "fromage",
        "pain",
        "coquillage",
        "cheval",
        "train",
        "dragon",
        "épée",
        "robot",
        "camion",
        "musique",
        "livre",
        "bouche",
        "soupe",
        "chocolat",
        "papillon",
        "ourson",
        "ventre",
        "feu",
        "citrouille",
        "poupée",
        "blaireau",
        "poule",
        "chaton",
        "feuille",
        "herbe",
        "chasseur",
        "oeuf",
        "sapin",
        "pistolet",
        "étoile",
        "glace",
        "ballon",
        "oreille",
        "noix",
        "cuiller",
        "escalier",
        "corde",
        "lèvre",
        "échelle",
        "cochon",
    ]
    
    def __init__(self, stories_name = "fake_stories", dataset_name = "fake_dataset"):
        self.sp = StoryParser(stories_name=stories_name, dataset_name=dataset_name)
        self.chat_gpt = ChatGPT()
        self.oci_api_key = os.environ.get("REVIRADA_API_KEY")
        
    def get_nouns(self, top=100):
        nouns = self.sp.get_word_in_dataset(word_type=WordType.NOUN)
        nouns = list(sorted(nouns, key=lambda x: x[1], reverse=True))[:top]
        return nouns
        
    def generate_all_sentences(self, category: GrammaticalCategory):
        nouns = DataGenerator.NOUNS_WITH_IMG
        result = {"sentences": []}
        file_path = self.sp._build_path('sentences', filename=f"{category.fr.lower()}.json")
        for i in range(0, len(nouns), 10):
            some_nouns = nouns[i:i+10]
            context=CONTEXT_GENERATE_SENTENCES.format(
                    category.fr.lower(),
                    category.fr.lower(),
                    category.fr.lower(),
                    category.words,
                    some_nouns
                )
            print(f"CONTEXT: {context}")
            print(f"QUESTION: {QUESTION_GENERATE_SENTENCES}")
            text, tokens = self.chat_gpt.answer(question=QUESTION_GENERATE_SENTENCES, context=context)
            print(f"TEXT: {text}")
            print(text.split('\n'))
            list_sentences = [sentence for sentence in text.split('\n') if sentence != ""]
            print(f"RESULT: {list_sentences}")

            try:
                print(f"before ast: {list_sentences}")
                result["sentences"] += list_sentences
            except (ValueError, SyntaxError):
                print(f"Error during ast.literal_eval of text from GPT.")
            print(list_sentences)
            print(f"token: {tokens}")
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print("END GENERATE SENTENCES")
      
    def generate_multi_word_sentences(self, category):
        with open(f"app/sentences/{category}.json", 'r') as f:
            sentences = json.load(f)["sentences"]
        print(sentences)
        for sentence in sentences:
            question = CONTEXT_GENERATE_IMG.format(sentence)
            print(f"QUESTION: {question}")
            self.chat_gpt.generate_img(question)
                 
    def _get_color(self, syllabe):
        for homophone in ['aient', 'ait', 'ais', 'ai', 'est', 'et', 'é', 'és', 'ée', 'ées', 'eai', 'er']:
            if homophone in syllabe:
                return Color.E_AIGU.value
        if 'es' == syllabe:
            return Color.E_AIGU.value
        if 'ou' in syllabe:
            return Color.OU.value
        for homophone in ['oh', 'ho', 'eau', 'au', 'o', 'ô']:
            if homophone in syllabe:
                return Color.O.value
        for homophone in ['as', 'ah', 'ha', 'a', 'à', 'â']:
            if homophone in syllabe:
                return Color.A.value
        for homophone in ['ie', 'y', 'is', 'it', 'i', 'î']:
            if homophone in syllabe:
                return Color.I.value
        for homophone in ['ent', 'es', 'e', 'è', 'ê']:
            if homophone in syllabe:
                return Color.E.value
        if 'u' in syllabe:
            return Color.U.value
        
    def _is_an_homophone_or_not(self, syllabe, n):
        for homophone in ['aient', 'ait', 'ais', 'ai', 'est', 'et', 'é', 'és', 'ée', 'ées', 'eai', 'er']:
            if homophone == syllabe:
                return True
        if "es" == syllabe:
            if n == 1:
                return True
            return False
        for homophone in ['oh', 'ho', 'eau', 'au', 'o', 'ô']:
            if homophone == syllabe:
                return True
        for homophone in ['as', 'ah', 'ha', 'a', 'à', 'â']:
            if homophone == syllabe:
                return True
        for homophone in ['ie', 'y', 'is', 'it', 'i', 'î']:
            if homophone == syllabe:
                return True
        for homophone in ['ent', 'es', 'e', 'è', 'ê']:
            if homophone == syllabe:
                return True
        if 'ou' == syllabe:
            return True
        if 'u' == syllabe:
            return True
        return False
        
    def format_sentence_for_template(self, category: GrammaticalCategory):
        result = {"header_words": [], "sentences": []}
        sentences, grammatical_words = self._get_sentences_and_words(category.fr)
        self.create_and_fill_data_template(data=result, sentences=grammatical_words, category="header_words")
        self.create_and_fill_data_template(data=result, sentences=sentences, category="sentences")
        with open(f"app/sentences/template_{category.fr.lower()}.json", "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return result
    
    def format_sentence_for_illustrated_page_template(self, category):
        result = {"header_words": [], "sentences": []}
        sentences, _ = self._get_sentences_and_words(category.value)
        if sentences:
            self.create_and_fill_data_template(data=result, sentences=sentences, category="sentences", folder_img=category.value)
            with open(f"app/sentences/template_{category.value}.json", "w") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
                print(f"file app/sentences/template_{category.value}.json create successfully!")
    
    def create_and_fill_data_template(self, data, sentences, category, folder_img = ""):
        for ind, sentence in enumerate(sentences):
            t1 = time.time()
            item = {"fr": sentence, "oci": self._translate_in_oci(sentence), "data": []}
            if folder_img:
                abs_path = os.path.dirname(os.path.dirname(__file__))
                item["img"] = f"{abs_path}/src/img/{folder_img}/{sentence}.png"
            words = sentence.split(' ')
            for i, word in enumerate(words):
                syllabes = self._get_syllabes(word)
                for syllabe in self._split_syllabes(syllabes):
                    color = self._get_color(syllabe)
                    is_border = self._is_an_homophone_or_not(syllabe, n=len(syllabes))
                    item["data"].append({"text": syllabe, "classname": "syllabe", "color": color, "is_border": is_border})
                if i + 1 != len(words):
                    item["data"].append({"text": "", "classname": "space", "color": "white", "is_border": False})
            data[category].append(item)
            t2 = time.time()
            print(f"{category}: {sentence:<24}   {ind+1}/{len(sentences)} done in {(t2-t1):.2f}s")
    
    def _split_syllabes(self, syllabes):
        result = []
        syllabes = syllabes.split('-')
        for syllabe in syllabes:
            if syllabe.endswith("ier"):
                first_syl = syllabe.split('er')[0]
                result += [first_syl, "er"]
                continue
            if syllabe.endswith("ion"):
                first_syl = syllabe.split('on')[0]
                result += [first_syl, "on"]
                continue
            result.append(syllabe)
        return result
    
    def _get_sentences_and_words(self, category: str):
        try:
            with open(f"app/sentences/{category.lower()}.json", "r") as f:
                data = json.load(f)
                return data['sentences'], data['words']
        except FileNotFoundError as e:
            print(f"File app/sentences/{category.lower()}.json doesn't exist: {e}")
            return False, False
    
    def _translate_in_oci(self, sentence):
        try:
            body = {
                "api_key": self.oci_api_key,
                "engine": "apertium",
                "content_type": "txt",
                "text": sentence,
                "source_language": "fra",
                "target_language": "oci"
            }
            response = requests.post("https://api.revirada.eu/translate_string", data=body)
            if response.status_code == 500:
                print("ERROR SERVER")
                return ""
            response = response.json()
            print(f"traduit en {response['translation_time']}s")
            return response["translated_text"]
        except Exception as e:
            print(f"ERROR ON TRANSLATE OCI: {e}")
            
    def _get_syllabes(self, word):
        url = f"https://www.silabas.net/index-fr.php?lang=/index-fr.php&p={word}&button=Séparées"
        try:
            response = requests.get(url)
            response.raise_for_status()  # génère une exception si la requête a échoué
            soup = BeautifulSoup(response.content, 'html.parser')

            syllables_div = soup.find('div', style="padding-left:1em;background-color:#f5f5ff;border-style:dashed;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;border: 0px dashed #dde0fc;")
            
            if syllables_div:
                syllables = syllables_div.find('font').text
                return syllables
            else:
                print(f"Erreur lors de la récupération des syllabes pour le mot '{word}'")
        except requests.RequestException as e:
            print(f"Erreur lors de la requête pour le mot '{word}': {e}")
        except Exception as e:
            print(f"Erreur lors du traitement du mot '{word}': {e}")
    
        


if __name__ == "__main__":
    data_generator = DataGenerator(stories_name="fake_stories", dataset_name="dataset_stories")
    # quand je lance ce fichier "python3 -m app.models.dataGenerator"
    # je récupère les fichiers templates qui existe déjà et je vais créer tous les templates
    # restant pour avoir les données à jours de toutes les phrases.
    CHOICE_DATA_TO_GENERATE = "illustrated_page"
    
    filenames = os.listdir("app/sentences")
    filenames = [filename for filename in filenames if filename.startswith("template")]
    filenames = [filename.split('.')[0].split('_')[1] for filename in filenames]
    print(f"FILENAMES: {filenames}")
    
    if CHOICE_DATA_TO_GENERATE == "illustrated_page":
        for illustrated_page in IllustratedPageCategory:
            if illustrated_page.value not in filenames:
                data_generator.format_sentence_for_illustrated_page_template(illustrated_page)
            else:
                print(f"template {illustrated_page.value} already create...")
    
    if CHOICE_DATA_TO_GENERATE == "grammatical":
        for value in GrammaticalCategory:
            if value.fr.lower() not in filenames:
                data_generator.format_sentence_for_template(value)
            else:
                print(f"template {value.fr.lower()} already create...")
    
    