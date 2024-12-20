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
        "special_template": "cover_homophone_a",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "2_4",
        "special_template": "homophone_e_é",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "5_7",
        "special_template": "homophone_i_o",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "6_8",
        "special_template": "homophone_u_ou",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "9_11",
        "left": {
            "template": "empty",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 10,
        }
    },
    {
        "id": "10_12",
        "left": {
            "template": "header",
            "category": "articles indefinis",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 10,
        }
    },
    {
        "id": "13_15",
        "left": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "articles definis",
            "sentence_number": 10,
        }
    },
    {
        "id": "14_16",
        "left": {
            "template": "header",
            "category": "articles definis",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "articles definis",
            "sentence_number": 10,
        }
    },
    {
        "id": "17_19",
        "left": {
            "template": "normal",
            "category": "articles definis",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "18_20",
        "left": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "21_23",
        "left": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "normal",
            "category": "articles partitifs",
            "sentence_number": 10,
        }
    },
    {
        "id": "22_24",
        "left": {
            "template": "header",
            "category": "articles partitifs",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "articles partitifs",
            "sentence_number": 10,
        }
    },
    {
        "id": "25_27",
        "left": {
            "template": "normal",
            "category": "articles partitifs",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs demonstratifs",
            "sentence_number": 10,
        }
    },
    {
        "id": "26_28",
        "left": {
            "template": "header",
            "category": "adjectifs demonstratifs",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs demonstratifs",
            "sentence_number": 10,
        }
    },
    {
        "id": "29_31",
        "left": {
            "template": "normal",
            "category": "adjectifs demonstratifs",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "30_32",
        "left": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "33_35",
        "left": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "34_36",
        "left": {
            "template": "header",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "37_39",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "38_40",
        "left": {
            "template": "header",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "41_43",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "42_44",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "45_47",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "46_48",
        "left": {
            "template": "header",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "49_51",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 10,
        }
    },
    {
        "id": "50_52",
        "left": {
            "template": "header",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 10,
        }
    },
    # JE DOIS AJOUTER DES big-illustrated-page ()
    {
        "id": "53_55",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "54_56",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "57_59",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "empty",
            "category": "",
            "sentence_number": 0,

        }
    },
    {
        "id": "58_60",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "empty",
            "category": "",
            "sentence_number": 0,

        }
    },
]

book = [
    {
        "id": "1_3",
        "special_template": "cover_homophone_a",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "2_4",
        "special_template": "homophone_e_é",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "5_7",
        "special_template": "homophone_i_o",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "6_8",
        "special_template": "homophone_u_ou",
        "left": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "",
            "category": "",
            "sentence_number": 0,
        }
    },
    {
        "id": "9_11",
        "left": {
            "template": "empty",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 10,
        }
    },
    {
        "id": "10_12",
        "left": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "articles indefinis",
            "sentence_number": 0,
        }
    },
    {
        "id": "13_15",
        "left": {
            "template": "normal",
            "category": "articles indefinis",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "articles definis",
            "sentence_number": 10,
        }
    },
    {
        "id": "14_16",
        "left": {
            "template": "normal",
            "category": "articles definis",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "articles definis",
            "sentence_number": 0,
        }
    },
    {
        "id": "17_19",
        "left": {
            "template": "normal",
            "category": "articles definis",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "18_20",
        "left": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "21_23",
        "left": {
            "template": "illustrated",
            "category": "small-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "normal",
            "category": "articles partitifs",
            "sentence_number": 10,
        }
    },
    {
        "id": "22_24",
        "left": {
            "template": "normal",
            "category": "articles partitifs",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "articles partitifs",
            "sentence_number": 0,
        }
    },
    {
        "id": "25_27",
        "left": {
            "template": "normal",
            "category": "articles partitifs",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs demonstratifs",
            "sentence_number": 10,
        }
    },
    {
        "id": "26_28",
        "left": {
            "template": "normal",
            "category": "adjectifs demonstratifs",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "adjectifs demonstratifs",
            "sentence_number": 0,
        }
    },
    {
        "id": "29_31",
        "left": {
            "template": "normal",
            "category": "adjectifs demonstratifs",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "30_32",
        "left": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "33_35",
        "left": {
            "template": "illustrated",
            "category": "medium-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "34_36",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 0,
        }
    },
    {
        "id": "37_39",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs premiere personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "38_40",
        "left": {

            "template": "normal",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 0,
        }
    },
    {
        "id": "41_43",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs deuxieme personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "42_44",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "45_47",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 10,
        }
    },
    {
        "id": "46_48",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 0,
        }
    },
    {
        "id": "49_51",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs troisieme personne",
            "sentence_number": 10,
        },
        "right": {
            "template": "normal",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 10,
        }
    },
    {
        "id": "50_52",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 10,
        },
        "right": {
            "template": "header",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 0,
        }
    },
    # JE DOIS AJOUTER DES big-illustrated-page ()
    {
        "id": "53_55",
        "left": {
            "template": "normal",
            "category": "adjectifs possessifs pluriel",
            "sentence_number": 10,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "54_56",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
    {
        "id": "57_59",
        "left": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        },
        "right": {
            "template": "empty",
            "category": "",
            "sentence_number": 0,

        }
    },
    {
        "id": "58_60",
        "left": {
            "template": "empty",
            "category": "",
            "sentence_number": 0,
        },
        "right": {
            "template": "illustrated",
            "category": "big-illustrated-page",
            "sentence_number": 2,
            "with_img": True,
        }
    },
]

pg = PageGenerator(book_name="book2")
pg.create_book(book)