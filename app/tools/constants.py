
QUESTION_GENERATE_SENTENCES = ""
CONTEXT_GENERATE_SENTENCES = """Je créer un livre pour apprendre a des enfants de 4ans à lire. Je vais te données une liste de {} et de noms.\
Pour chaque {} je veux que tu l'associe avec chaque nom fournis. Génère moi une matrice sous forme de liste en sautant de ligne a chaque nouvelle génération. \
N'écris aucun commentaire, juste la liste. par exemple:\nun pirate\nune pomme\nune poire\nune tante\n \
Prend en considération le 'genre' et le 'nombre'. N'écris jamais de crochet, sinon ça va casser mon programme. Retourne juste la liste. Voici la liste de {}: {}.\n Pour chaque mots, essaye de le couplé avec chacun des noms suivants quand c'est correcte:  {}"""