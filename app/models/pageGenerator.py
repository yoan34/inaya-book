import requests
import json
from collections import defaultdict
import random
import subprocess
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
import os
from dotenv import load_dotenv
from tools.enumerators import GrammaticalCategory, IllustratedPageCategory


load_dotenv()

class PageGenerator:
    def __init__(self, book_name: str):
        self.book_name = book_name
        self.num_page = 1
        self.oci_api_key = os.environ.get("REVIRADA_API_KEY")
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.font_path = os.path.join(project_path, 'src/fonts/static/Karla-Regular.ttf')
        self.env = Environment(loader=FileSystemLoader(os.path.join(project_path, "templates")))
        self.nouns_to_print = {"small": {}, "medium": {}, "big": {}}
        self._create_book_folder()
        
    def create_page_img(self):
        template = self.env.get_template("page_img.html")

        abs_path = os.path.dirname(os.path.dirname(__file__))

        for category, item in self.nouns_to_print.items():
            data = []
            for noun, quantity in item.items():
                if category == "small":
                    container_height = "65px"
                    img_height = "40px"
                    img_width = len(noun)*15
                    img_pb = "5px"
                if category == "medium":
                    container_height = "56px"
                    img_height = "36px"
                    img_width = len(noun)*14
                    img_pb = "3px"
                if category == "big":
                    container_height = "52px"
                    img_height = "34px"
                    img_width = len(noun)*13
                    img_pb = "0px"
                data.append({
                    "name": noun,
                    "path": f"{abs_path}/src/img/nouns/{noun}.png",
                    "pixel": img_width,
                    "container_height": container_height,
                    "img_height": img_height,
                    "img_pb": img_pb,
                    "quantity": quantity,
                    })
            print(f"IMG: {abs_path}/book/pages/img/html")
            result = template.render(data=data, font_path=self.font_path)
                    
            page_name = f"book/{self.book_name}/img_{category}__{self.num_page}.html"
            self.num_page += 1
            self._write_file(page_name, result)
        
        
    def get_sentences_and_update(self, left_page, right_page, sentences: dict):
        left_sentences, right_sentences = [], []
        if left_page["category"]:
            left_sentences = random.sample(sentences[left_page["category"]]["sentences"], left_page["sentence_number"])
            [sentences[left_page["category"]]["sentences"].remove(left_sentence) for left_sentence in left_sentences]
        if right_page["category"]:
            right_sentences = random.sample(sentences[right_page["category"]]["sentences"], right_page["sentence_number"])
            [sentences[right_page["category"]]["sentences"].remove(right_sentence) for right_sentence in right_sentences]
        return left_sentences, right_sentences
    

    def get_header_words(self, left_page, right_page, sentences: dict):
        left_header_words, right_header_words = [], []
        if left_page["category"]:
            left_header_words = sentences[left_page["category"]]["header_words"]
        if right_page["category"]:
            right_header_words = sentences[right_page["category"]]["header_words"]
        return left_header_words, right_header_words
           
           
    def create_page(self, pages, sentences):
        left_page = pages["left"]
        right_page = pages["right"]
        if "special_template" in pages:
            template = self.env.get_template(f"specific/{pages['special_template']}_page.html")
        else: 
            template = self.env.get_template(f"{left_page['template']}_{right_page['template']}_page.html")

        left_sentences, right_sentences = self.get_sentences_and_update(left_page, right_page, sentences)
        left_header_words, right_header_words = self.get_header_words(left_page, right_page, sentences)
        
        print(left_sentences)

        data = {
            "sentences_left": left_sentences,
            "left_header_words": left_header_words,
            "sentences_right": right_sentences,
            "right_header_words": right_header_words
        }
        img_path = f"{os.path.dirname(os.path.dirname(__file__))}/src/img"
        if "with_img" in left_page:
            data["left_page_img"] = f"{img_path}/{left_page['category']}"
            if "small" in left_page["category"]:
                data["width_img"] = "75%"
                data["font_size"] = "30px"
                data["word_margin"] = "25px"
            if "medium" in left_page["category"]:
                data["width_img"] = "65%"
                data["font_size"] = "28px"
                data["word_margin"] = "21px"
            if "big" in left_page["category"]:
                data["width_img"] = "55%"
                data["font_size"] = "26px"
                data["word_margin"] = "17px"
            
        if "with_img" in right_page:
            data["right_page_img"] = f"{img_path}/{right_page['category']}"
            if "small" in right_page["category"]:
                data["width_img"] = "75%"
                data["font_size"] = "30px"
                data["word_margin"] = "25px"
            if "medium" in right_page["category"]:
                data["width_img"] = "65%"
                data["font_size"] = "28px"
                data["word_margin"] = "21px"
            if "big" in right_page["category"]:
                data["width_img"] = "55%"
                data["font_size"] = "26px"
                data["word_margin"] = "17px"
        
        result = template.render(data=data, font_path=self.font_path)
        page_name = f"book/{self.book_name}/{pages['id']}.html"
        self._write_file(page_name, result)
    
    def create_ilustrate_page(self, sentences, category):
        template = self.env.get_template("ilustrate_page_2.html")
        data = {
            "sentence_left": sentences[0],
            "sentence_right": sentences[1],
        }
        result = template.render(data=data, font_path=self.font_path)
        page_name = f"book/{self.book_name}/{category.replace(' ', '_')}__{self.num_page}.html"
        self.num_page += 1
        self._write_file(page_name, result)
        
        abs_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        #subprocess.run(["firefox", f"{abs_path}/{page_name}"])
        
    def _create_book_folder(self):
        path = f"book/{self.book_name}"
        if not os.path.exists(path):
            os.makedirs(path)
            os.makedirs(f"book/result_{self.book_name}")
            
    def _write_file(self, page_name, data):
        with open(page_name, 'w') as f:
            f.write(data)
            print(f"Page create {page_name} successfully")
            
    def _get_num(self, path):
        if not os.path.exists(path):
            num = 1
            os.makedirs(path)
            os.makedirs(os.path.join(os.path.dirname(path), "pdf"))
        else:
            files = os.listdir(path)
            num = max(list(map(int, [file.split('_')[0] for file in files]))) + 1
        return num
            
    def _get_sentences_and_header_word(self, category, n=20):
        sentences, header_words = [], []
        with open(f"app/sentences/template_{category}.json", 'r') as f:
            data = json.load(f)
        for sentence in data["sentences"]:
            if sentence not in sentences:
                sentences.append(sentence)
        for header_word in data["header_words"]:
            header_words.append(header_word)
        return random.sample(sentences, n), header_words
    
    def count_nouns_to_print(self, sentences, key):
        print(key)
        nouns = [noun.split('.')[0] for noun in os.listdir("app/src/img/nouns")]
        nouns.sort(key=len, reverse=True)
        
        for sentence in sentences:
            for noun in nouns:
                if noun in sentence['fr']:
                    if "medium" in key:
                        if noun not in self.nouns_to_print["medium"]:
                            self.nouns_to_print["medium"][noun] = 0
                        self.nouns_to_print["medium"][noun] += 1
                        break
                    if "big" in key:
                        if noun not in self.nouns_to_print["big"]:
                            self.nouns_to_print["big"][noun] = 0
                        self.nouns_to_print["big"][noun] += 1
                        break
                    if noun not in self.nouns_to_print["small"]:
                        self.nouns_to_print["small"][noun] = 0
                    self.nouns_to_print["small"][noun] += 1
                    break

    def create_book(self, book):
        # create dictionnaire pour retrieve all sentences necessary
        all_sentences = defaultdict(int)
        for pages in book:
            left, right = pages["left"], pages["right"]
            if left["category"]:
                all_sentences[left["category"]] += left["sentence_number"]
            if right["category"]:
                all_sentences[right["category"]] += right["sentence_number"]

        for key, count in all_sentences.items():
            print(key, count)
            sentences, header_words = self._get_sentences_and_header_word(key, n=count)
            self.count_nouns_to_print(sentences, key)
            all_sentences[key] = {"sentences": sentences, "header_words": header_words}
            
        for pages in book:
            self.create_page(pages, all_sentences)
        
        self.create_page_img()


if __name__ == "__main__":
    pg = PageGenerator()
    #r = pg.create_page_img()
    # je dois stocker les datas qui sont traduit et découpé
    # créer une fonction qui récupère les données au lieu de généré + template
    
    pg.create_page_img()
    
    # for value in GrammaticalCategory:
    #     for _ in range(5):
    #         sentences, header_words = pg._get_sentences_and_header_word(value, n=30)
    #         pg.create_page(value, sentences[:20], header_words, is_header=True)
    #         pg.create_page(value, sentences[10:], header_words)

