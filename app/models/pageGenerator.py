import requests
import json
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
        self.nouns_to_print = {}
        self._create_book_folder()
        
    def create_page_img(self):
        template = self.env.get_template("page_img.html")
        abs_path = os.path.dirname(os.path.dirname(__file__))
        data = []
        for noun, quantity in self.nouns_to_print.items():
            data.append({
                "name": noun,
                 "path": f"{abs_path}/src/img/nouns/{noun}.png",
                 "pixel": len(noun)*18,
                 "quantity": quantity,
                })
        print(f"IMG: {abs_path}/book/pages/img/html")
        result_path = f"{abs_path}/book/pages/img/html"
        result = template.render(data=data, font_path=self.font_path)
        
        num = self._get_num(result_path)
                
        page_name = f"book/{self.book_name}/img__{self.num_page}.html"
        self.num_page += 1
        self._write_file(page_name, result)
           
    def create_page(self, category: GrammaticalCategory, sentences, header_words, is_header=False):
        template = self.env.get_template(f"{'header' if is_header else 'normal'}_page.html")
        data = {
            "page": category.name,
            "is_header": is_header,
            "headers": header_words,
            "sentences_left": sentences[10:],
            "sentences_right": sentences[:10]
        }
        result = template.render(data=data, font_path=self.font_path)
        page_name = f"book/{self.book_name}/{category.fr.lower().replace(' ', '_')}__{self.num_page}.html"
        self.num_page += 1
        self._write_file(page_name, result)
    
    def create_ilustrate_page(self, sentences, category):
        template = self.env.get_template("ilustrate_page.html")
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
    
    def count_nouns_to_print(self, sentences):
        nouns = [noun.split('.')[0] for noun in os.listdir("app/src/img/nouns")]
        nouns.sort(key=len, reverse=True)
        
        for sentence in sentences:
            for noun in nouns:
                if noun in sentence['fr']:
                    if noun not in self.nouns_to_print:
                        self.nouns_to_print[noun] = 0
                    self.nouns_to_print[noun] += 1
                    break

    def create_book(self, book):
        for key, value in book.items():
            header = value["header"]
            page = value["page"]
            category = value["category"]
            sentences_by_page = value["sentences_by_page"]
            sentences_by_header = value["sentences_by_header"]
            total_sentences = header*sentences_by_header + page * sentences_by_page
            
            if key in [value.fr.lower() for value in GrammaticalCategory]:
                sentences, header_words = self._get_sentences_and_header_word(key, n=total_sentences)
                
                for i in range(header):
                    header_sentences = sentences[(i*sentences_by_header):((i+1)*sentences_by_header)]
                    self.count_nouns_to_print(header_sentences)
                    print(f"HEADER {i+1}: {[sentence['fr'] for sentence in header_sentences]}")
                    self.create_page(category, header_sentences, header_words, is_header=True)
                sentences = sentences[(sentences_by_header*header):]
                for _ in range(page):
                    page_sentences = sentences[i*sentences_by_page:(i+1)*sentences_by_page]
                    self.count_nouns_to_print(page_sentences)
                    print(f"PAGE {i+1}: {[sentence['fr'] for sentence in page_sentences]}")
                    self.create_page(category, page_sentences, header_words)
            
            if key in [illustrated_page.value for illustrated_page in IllustratedPageCategory]:
                sentences, _ = self._get_sentences_and_header_word(key, n=total_sentences)
                for i in range(page):
                    random_sentences = random.sample(sentences, 2)
                    self.count_nouns_to_print(random_sentences)
                    print(f"ILUSTRATED PAGE {i+1}: {[sentence['fr'] for sentence in random_sentences]}")
                    [sentences.remove(random_sentence) for random_sentence in random_sentences]
                    # JE DOIS CONTINUER DE CREER LA FONCTION JUSTE EN DESSOUS
                    self.create_ilustrate_page(random_sentences, key)
        
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

