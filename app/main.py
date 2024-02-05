from models.pageGenerator import PageGenerator
from tools.enumerators import GrammaticalCategory, IllustratedPageCategory


book = {
    "articles indefinis": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.INDEFINITE_ARTICLES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "articles partitifs": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.PARTITIVE_ARTICLES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "articles definis": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.DEFINITE_ARTICLES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "adjectifs demonstratifs": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.DESMONSTRATIVE_ADJECTIVES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "adjectifs possessifs premiere personne": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.FIRST_PERSON_POSSESSIVE_ADJECTIVES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "adjectifs possessifs deuxieme personne": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.SECOND_PERSON_POSSESSIVE_ADJECTIVES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "adjectifs possessifs troisieme personne": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.THIRD_PERSON_POSSESSIVE_ADJECTIVES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "adjectifs possessifs pluriel": {
        "page": 1,
        "header": 1,
        "category": GrammaticalCategory.PLURAL_POSSESSIVE_ADJECTIVES,
        "sentences_by_page": 20,
        "sentences_by_header": 10,
    },
    "small-illustrated-page": {
        "page": 4,
        "header": 0,
        "category": IllustratedPageCategory.SMALL_ILLUSTRATED_PAGE,
        "sentences_by_page": 2,
        "sentences_by_header": 0,
    },
    "medium-illustrated-page": {
        "page": 4,
        "header": 0,
        "category": IllustratedPageCategory.MEDIUM_ILLUSTRATED_PAGE,
        "sentences_by_page": 2,
        "sentences_by_header": 0,
    },
    "big-illustrated-page": {
        "page": 4,
        "header": 0,
        "category": IllustratedPageCategory.BIG_ILLUSTRATED_PAGE,
        "sentences_by_page": 2,
        "sentences_by_header": 0,
    },
}


book = [
    {
        "id": "1_3",
        "left": {
            "template": "header",
            "category": "articles indefinis",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 9,
        }
    },
        {
        "id": "2_4",
        "left": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 9,
        },
        "right": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 9,
        }
    }
]

pg = PageGenerator(book_name="book1")
pg.create_book(book)