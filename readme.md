POUR GPT4:
Je suis en train de créer un livre pour enfant de 4 ans qui permet d'apprendre a lire en découpant les mots en syllabes et associant une couleur par type de syllabe. Les types sont définis de la manière suivante: si une syllabe contient le son "a" c'est une catégorie. Je fais la même opération pour les voyelles suivante: "e", "i", "é", "o", "u", "ou". Maintenant je vais écrire des petites phrases comme par exemple "Le chien a un os", et j'aimerai que tu créer une ilustration au format A5 car je vais mettre l'image sur un fichier HTML qui fera la moitié d'une feuille A4 en mode paysage. Génère moi une image pour la phrase suivante: "Le prince à une épée dorée"


CREER UN PDF:
pdftk *.pdf cat output fichier_final.pdf
GARDER QUE LES PAGE:
pdftk fichier_original.pdf cat 2 4 6 8 10 output BOOK.pdf



SOUS-TEMPLATE POSSIBLE:
- HEADER
- NORMAL
- HOMOPHONE
- COVER
- ILLUSTRATED
- FIRST
- EMPTY

pour séparer en deux parties les feuilles à imprimer:
pdftk *.pdf cat output result.pdf

Il faut séparer maintenant le fichier result.pdf en deux resultat, le premier pour imprimer le recto et
le deuxième pour le recto
pdftk 1_3.pdf 5_7.pdf 9_11.pdf 13_15.pdf 17_19.pdf 21_23.pdf 25_27.pdf 29_31.pdf 33_35.pdf 37_39.pdf 41_43.pdf 45_47.pdf 49_51.pdf 53_55.pdf 57_59.pdf cat output recto.pdf

pdftk 2_4.pdf 6_8.pdf 10_12.pdf 14_16.pdf 18_20.pdf 22_24.pdf 26_28.pdf 30_32.pdf 34_36.pdf 38_40.pdf 42_44.pdf 46_48.pdf 50_52.pdf 54_56.pdf 58_60.pdf cat output verso.pdf

    ADJ: adjective, e.g. big, old, green, incomprehensible, first
    ADP: adposition, e.g. in, to, during
    ADV: adverb, e.g. very, tomorrow, down, where, there
    AUX: auxiliary, e.g. is, has (done), will (do), should (do)
    CONJ: conjunction, e.g. and, or, but
    CCONJ: coordinating conjunction, e.g. and, or, but
    DET: determiner, e.g. a, an, the
    INTJ: interjection, e.g. psst, ouch, bravo, hello
    NOUN: noun, e.g. girl, cat, tree, air, beauty
    NUM: numeral, e.g. 1, 2017, one, seventy-seven, IV, MMXIV
    PART: particle, e.g. ’s, not,
    PRON: pronoun, e.g I, you, he, she, myself, themselves, somebody
    PROPN: proper noun, e.g. Mary, John, London, NATO, HBO
    PUNCT: punctuation, e.g. ., (, ), ?
    SCONJ: subordinating conjunction, e.g. if, while, that
    SYM: symbol, e.g. $, %, §, ©, +, −, ×, ÷, =, :), 😝
    VERB: verb, e.g. run, runs, running, eat, ate, eating
    X: other, e.g. sfpksdpsxmsa
    SPACE: space, e.g.
