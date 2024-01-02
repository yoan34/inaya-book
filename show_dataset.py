import json


NOMBRE_SYLLABLES = 2
    
def show_most_used_word(data):
    data = dict(sorted(data.items(), key=lambda item: item[1]['count']))
    for lemma, value in data.items():
        print(f"{lemma:<12} - {value['count']}")
        
        
def show_word_syllabes(NOMBRE_SYLLABLESdata, sort = "number"):
    syllabes = {}
    for lemma, value in data.items():
        for word, d in value['possibilities'].items():
            syllabes[d['syllables']] = d['count']
    if sort == "number":
        syllabes = dict(sorted(syllabes.items(), key=lambda item: item[1]))
    if sort == "alphabet":
        syllabes = syllabes = dict(sorted(syllabes.items()))

    with open("tout_mot_syllable.txt", "w") as f:
        for syl in syllabes:
            f.write(f"{syl:<20} {syllabes[syl]}\n")
    return syllabes


def show_word_for_exercice(data, sort="number"):
    syllabes = {}
    for lemma, value in data.items():
        syl = value['syllabes']
        syllabes[syl] = value['count']
        if sort == "number":
            syllabes = dict(sorted(syllabes.items(), key=lambda item: item[1]))
        if sort == "alphabet":
            syllabes = syllabes = dict(sorted(syllabes.items()))

    with open("mots_syllables.txt", "w") as f:
        for syl in syllabes:
            f.write(f"{syl:<20} {syllabes[syl]}\n")
    return syllabes


def show_syllabes(data, sort = "number"):
    syllabes = show_word_syllabes(data)
    all_syllabes = {}
    for syllabe, count in syllabes.items():
        sub_syllabe = syllabe.split('-')
        for syl in sub_syllabe:
            if syl not in all_syllabes:
                all_syllabes[syl] = count
            else:
                all_syllabes[syl] += count
                
    if sort == "number":
        all_syllabes = dict(sorted(all_syllabes.items(), key=lambda item: item[1]))
    if sort == "alphabet":
        all_syllabes = dict(sorted(all_syllabes.items()))
    for syllabe, count in all_syllabes.items():
        print(f'{syllabe:<5} - {count}')
    print(f"total syllables: {len(all_syllabes)}")
            
       
def create_file_same_start_syllabe(data, n, hidden=False):
    syllabes = {}
    startwith = ""
    for lemma, value in data.items():
        syl = value['syllabes']
        syllabes[syl] = value['count']
        syllabes = syllabes = dict(sorted(syllabes.items()))
    result = []
    some_syl = []
    for ind, syl in enumerate(syllabes):
        all_syl = syl.split('-')
        if len(all_syl) != NOMBRE_SYLLABLES:
            continue
        if ind == 0:
            startwith = all_syl[0]
            some_syl.append(syl)
        else:
            if not startwith:
                startwith = all_syl[0]
            if all_syl[0] == startwith:
                some_syl.append(syl)
            else:
                startwith = all_syl[0]
                result.append(some_syl)
                some_syl = [syl]
    groups = 0
    for r in result:
        if len(r) == n:
            groups += 1
            if not hidden:
                for w in r:
                    print(w)
                print()
    if groups > 0:
        print(f"il y a {groups} groupe de mot qui ont {n} mots différents.")
        


def create_file_by_type(data):
    types = []
    words = {}
    all_words = []
    for key in data:
        if data[key]["type"] not in types:
            types.append(data[key]["type"])
        if data[key]["count"] > 10:
            all_words.append((key, data[key]["count"], data[key]['type']))
            # if data[key]["type"] not in words:
            #     words[data[key]]["type"] = {}
            # words[data[key["type"]]][key] = data[key]
    for word, count, t in all_words:
        print(f"{word:<18} {count:<6} {t}")
    print(types)
            
            
 
        
        
        
if __name__ == "__main__":
    # Les différentes types sont
    # ['NOUN', 'VERB', 'ADJ', 'ADV', 'PROPN', 'AUX', 'PRON', 'INTJ', 'ADP', 'X', 'NUM', 'CCONJ', 'DET', 'SYM', 'SCONJ']
    # ceux utile pour apprendre à lire sont les DET (un, une, on, mon, ton, sa, le votre..)
    # ADP (de, à)
    # PRON (il, )
    # CCONJ (et)
    with open("dataset_stories.json", "r") as file:
        data = json.load(file)
    
    create_file_by_type(data)
    
    
    
    
"""
j'aimerai que tu me génère ce genre d'image, en format A4 et en paysage. Je veux dire le meme style de dessin mais le but du jeu c'est que j'écris des mots clés et avec ces mots clés tu dois créer soit un paysage, soit une mise en scène des mots/noms/verbe pour l'ilustration. Car j'aimerai avoir des images pour ilustrer un livre que je créer pour ma fille, le but du livre est de deviner des mots, par exemple je commence par "CHA" et il faut deviner les mots qui commence par "CHA" comme "CHATON", "CHATEAU", "CHARETTE" etc.
Peux-tu créer une ilustration dans le meme style de dessin avec les mots clés suivant:
chaton, chateau, chameau, charette, chalet, chapeau, chataigne. Tu dois dans l'ilustration y mettre quelques concept lié au mot clé mais également rajouté d'autre chose qui ne sont pas dans les mots clés.
"""
"""
Bonjour, je travaille sur un projet de livre illustré pour ma fille. Le concept du livre est de deviner des mots basés sur des indices visuels. Pour chaque page, j'aimerais une illustration qui représente un groupe de mots commençant par les mêmes lettres. Par exemple, pour la lettre "CHA", les mots pourraient être "chaton", "château", "chameau", "charette", etc.

Je souhaite que les illustrations soient réalisées dans un style adapté aux enfants, coloré et imaginaire, en format A4 paysage. Chaque image doit intégrer visuellement les mots clés que je fournirai, tout en ajoutant des éléments créatifs et ludiques qui ne sont pas directement liés aux mots clés. Cela permettra d'encourager la curiosité et l'imagination des enfants tout en les aidant à apprendre de nouveaux mots.

Pourriez-vous créer une illustration suivant ces directives, en utilisant les mots clés "chaton", "château", "chameau", "charette", "chalet", "chapeau", et "châtaigne"? L'idée est de créer une scène où ces éléments sont harmonieusement intégrés, stimulant ainsi l'intérêt et la découverte pour les jeunes lecteurs.
"""