from enum import Enum

**
    

class Color(Enum):
    A = "pink"
    E = "blue"
    E_AIGU = "purple"
    O = "yellow"
    U = "orange"
    OU = "red"
    I = "green"
    

class WordType(Enum):
    ADJ = "ADJ"
    ADP = "ADP"
    ADV = "ADV"
    AUX = "AUX"
    CONJ = "CONJ"
    CCONJ = "CCONJ"
    DET = "DET"
    INTJ = "INTJ"
    NOUN = "NOUN"
    NUM = "NUM"
    PART = "PART"
    PRON = "PRON"
    PROPN = "PROPN"
    PUNCT = "PUNCT"
    SCONJ = "SCONJ"
    SYM = "SYM"
    VERB = "VERB"
    X = "X"
    SPACE = "SPACE"
    

class ModelType(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_INSTRUCT = "gpt-3.5-turbo-instruct"
    GPT_4 = "gpt-4"
    
    
class IllustratedPageCategory(Enum):
    SMALL_ILLUSTRATED_PAGE = "small-illustrated-page"
    MEDIUM_ILLUSTRATED_PAGE = "medium-illustrated-page"
    BIG_ILLUSTRATED_PAGE = "big-illustrated-page"
    
class GrammaticalCategory(Enum):
    INDEFINITE_ARTICLES = (["un", "une"], "ARTICLES INDEFINIS")
    PARTITIVE_ARTICLES = (["de", "du", "des"], "ARTICLES PARTITIFS")
    DEFINITE_ARTICLES = (["le", "la", "les", "l'"], "ARTICLES DEFINIS")
    DESMONSTRATIVE_ADJECTIVES = (["ce", "cet", "cette", "ces"], "ADJECTIFS DEMONSTRATIFS")
    FIRST_PERSON_POSSESSIVE_ADJECTIVES = (["mes", "mon", "ma"], "ADJECTIFS POSSESSIFS PREMIERE PERSONNE")
    SECOND_PERSON_POSSESSIVE_ADJECTIVES = (["ton", "ta", "tes"], "ADJECTIFS POSSESSIFS DEUXIEME PERSONNE")
    THIRD_PERSON_POSSESSIVE_ADJECTIVES = (["son", "sa", "ses"], "ADJECTIFS POSSESSIFS TROISIEME PERSONNE")
    PLURAL_POSSESSIVE_ADJECTIVES = (["notre", "votre", "leur"], "ADJECTIFS POSSESSIFS PLURIEL")
    
    # CONJUNCTIONS = ["et", "ou", "mais"]
    # PREPOSITIONS = ["dans", "par", "pour", "avec"]
    # SINGULAR_SUBJECT_PRONOUNS = ["je", "tu", "il"]
    # PLURAL_SUBJECT_PRONOUNS = ["nous", "vous", "ils"]
    
    def __init__(self, words, fr):
        self.words = words
        self.fr = fr

if __name__ == "__main__":
    test = GrammaticalCategory
    print(test.INDEFINITE_ARTICLES.name)
    print(test.INDEFINITE_ARTICLES.words)
    print(test.INDEFINITE_ARTICLES.value)