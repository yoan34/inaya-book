import requests
from bs4 import BeautifulSoup


def get_syllabes(word):
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
        
        
def get_occitan(sentence):
    api_key = ""
    url = "https://api.revirada.eu/translate_string"
    body = {
        "api_key": api_key,
        "engine": "apertium",
        "content_type": "txt",
        "text": sentence,
        "source_language": "fra",
        "target_language": "oci_gascon",
    }
    try:
        response = requests.post(url, data=body)
        print(response)
    except requests.RequestException as e:
        print(f"Erreur lors de la requête")
    except Exception as e:
        print(f"Erreur lors du traitement: {e}")
        
        
if __name__ == "__main__":
    get_occitan("hhh")