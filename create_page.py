import json
import subprocess
from jinja2 import Template, Environment, FileSystemLoader
import pdfkit
import os



project_path = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(project_path, 'fonts/static/Karla-Regular.ttf')

# Chargez les données à partir du fichier JSON
with open("data_book.json") as f:
    data = json.load(f)


# Créez un environnement Jinja qui chargera les templates à partir du répertoire courant
result_filename = "book.html"
env = Environment(loader=FileSystemLoader("templates/"))

# Créez un nouveau template Jinja avec le contenu souhaité
template = env.get_template("basic_page.html")


data = {
    "sentences": ["une pomme", "un pirate", "une chaise", "une maison", "un avion"]
}
# Remplissez le template avec les données chargées à partir du fichier JSON
result = template.render(data=data, font_path=font_path)

# Affichez le résultat
with open(f"book/{result_filename}", "w") as file:
    file.write(result)
    print(f"...wrote finish!")


def run_cmd(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except UnicodeDecodeError as e:
        print(f"fatal error: {e}")
        return f"fatal error: {e}"

    if result.returncode != 0:
        # print(f"Error executing command: '{command}'")
        return result.stderr
    # print(f"The command '{command}' was executed successfully!")
    return result.stdout


run_cmd(f"firefox book/{result_filename}")
options = {
    'enable-local-file-access': ''
}

pdfkit.from_string(''.join([result]), 'output.pdf', options=options)