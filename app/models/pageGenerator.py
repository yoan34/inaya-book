import requests
import json
import random
import subprocess
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
import pdfkit

import os
from dotenv import load_dotenv
from app.tools.enumerators import GrammaticalCategory, Color


load_dotenv()

class PageGenerator:
    def __init__(self):
        self.oci_api_key = os.environ.get("REVIRADA_API_KEY")
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.font_path = os.path.join(project_path, 'src/fonts/static/Karla-Regular.ttf')
        self.env = Environment(loader=FileSystemLoader(os.path.join(project_path, "templates")))
        
    def create_page_img(self):
        template = self.env.get_template("page_img.html")
        imgs = os.listdir("app/src/img/nouns")
        abs_path = os.path.dirname(os.path.dirname(__file__))
        data = []
        for img in imgs:
            name = img.split('.')[0]

            data.append({"name": name, "path": f"{abs_path}/src/img/nouns/{img}", "pixel": len(name)*20})
        result_path = "book/pages/img"
        print(data)
        result = template.render(data=data, font_path=self.font_path)
        
        num = self._get_num(result_path)
                
        # JUST FOR TESTING DIRECT HTML FILE
        with open(f'{result_path}/{num}.html', 'w') as f:
            f.write(result)
            subprocess.run(["firefox", f'{result_path}/{num}.html'])
        
        
    def create_page(self, category: GrammaticalCategory, is_header=False):
        template = self.env.get_template(f"{'header' if is_header else 'normal'}_page.html")
        sentences = self._get_sentences(category=category)
        print(sentences)
        data = {
            "page": category.name,
            "is_header": is_header,
            "headers": category.words,
            "sentences_left": sentences[:10],
            "sentences_right": sentences[10:]
        }
        # Remplissez le template avec les données chargées à partir du fichiesr JSON
        result = template.render(data=data, font_path=self.font_path)
        result_path = f"book/pages/{category.fr.lower()}"
        num = self._get_num(result_path)
        
        # JUST FOR TESTING DIRECT HTML FILE
        with open(f'{result_path}/{num}.html', 'w') as f:
            f.write(result)
            subprocess.run(["firefox", f'{result_path}/{num}.html'])
            
        pdfkit.from_string(''.join([result]), f'{result_path}/{num}.pdf', options={'enable-local-file-access': ''})
        
    
    def _get_num(self, path):
        if not os.path.exists(path):
            num = 1
            os.makedirs(path)
        else:
            files = os.listdir(path)
            num = max(list(map(int, [file.split('.')[0] for file in files]))) + 1
        return num
            
    def _get_sentences(self, category: GrammaticalCategory, n=20):
        sentences = []
        with open(f"app/sentences/template_{category.fr.lower()}.json", 'r') as f:
            data = json.load(f)
        for sentence in data:
            if sentence not in sentences:
                sentences.append(sentence)
        return random.sample(sentences, n)
    
   

if __name__ == "__main__":
    pg = PageGenerator()
    r = pg.create_page_img()
    # je dois stocker les datas qui sont traduit et découpé
    # créer une fonction qui récupère les données au lieu de généré + template
    
    # r = pg.create_page(GrammaticalCategory.INDEFINITE_ARTICLES, is_header=True)
    

    
    