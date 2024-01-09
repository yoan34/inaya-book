import json

from tools.helpers import get_syllabes, get_occitan
from tools.enumerators import Color


# ACHETER BITCOIN LEDGE
# https://shop.ledger.com/fr

# trouver une structure de sentene comme
a = {
  "un_une": {
    "sentences": ["une pomme"]
  },
  "ton_ta_tes": {
    "sentences": ["une pomme"]
  }
}

def get_color(syllabe):
  for homophone in ['aient', 'ait', 'ais', 'ai', 'est', 'et', 'é', 'és', 'ée', 'ées', 'eai']:
    if homophone in syllabe:
      return Color.E_AIGU.value
  if 'es' == syllabe:
    return Color.E_AIGU.value
  for homophone in ['as', 'ah', 'ha', 'a']:
    if homophone in syllabe:
      return Color.A.value
  for homophone in ['ie', 'y', 'is', 'it', 'i']:
    if homophone in syllabe:
      return Color.I.value
  for homophone in ['ent', 'es', 'e']:
    if homophone in syllabe:
      return Color.E.value
  for homophone in ['oh', 'ho', 'eau', 'au', 'o']:
    if homophone in syllabe:
      return Color.O.value
  if 'ou' in syllabe:
    return Color.OU.value
  if 'u' in syllabe:
    return Color.U.value


def create_data_json(data):
  r = {}
  for page in data:
    sentences = data[page]["sentences"]
    r[page] = {"sentences": []}
    for sentence in sentences:
      item = {"fr": sentence, "oci": "blablablablabl", "data": []}
      words = sentence.split(' ')
      for word in words:
        syllabes = get_syllabes(word)
        for syllabe in syllabes.split('-'):
          color = get_color(syllabe)
          item["data"].append({"text": syllabe, "classname": "syllabe", "color": color})
        item["data"].append({"text": "", "classname": "space", "color": "white"})
      r[page]["sentences"].append(item)
  return r

      

with open('data_sentences.json', "w", encoding='utf-8') as f:
  json.dump(create_data_json(a), f, ensure_ascii=False, indent=4)
