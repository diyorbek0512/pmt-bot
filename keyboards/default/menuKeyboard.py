from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu1 = ReplyKeyboardMarkup(
    keyboard= [
        [
         KeyboardButton(text="🏫Prezident Maktabi"),
         KeyboardButton(text="🗂Tayyorgarlik uchun darslar"),
        ],
        [
            KeyboardButton(text="🏫Ixtisoslashtirilgan Maktablar")
        ],
        [
         KeyboardButton(text="📣Telegram Kanalga ulanish"),
         KeyboardButton(text="▶YouTube kanalga ulanish")
        ],
        [
         KeyboardButton(text="💻Reklama xizmati")
        ]

    ],
    resize_keyboard=True
)
menu2 = ReplyKeyboardMarkup(
    keyboard= [
        [
         KeyboardButton(text="❇Prezident Maktabi Hayoti❇"),
         KeyboardButton(text="🔍MAXSUS TO'PLAM"),
        ],
        [
            KeyboardButton(text="❔❓Namunaviy savollar"),
            KeyboardButton(text="Go back.")
        ]
    ],
    resize_keyboard=True
)


menu3 = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="📖 Ingliz tili"),
            KeyboardButton(text="📗 Tanqidiy Fikrlash"),
        ],
        [
            KeyboardButton(text="📐Matematika"),
            KeyboardButton(text="Go Back.")
        ],
    ],
    resize_keyboard=True
)
# menu4 =  ReplyKeyboardMarkup(
#     keyboard= [
#         [
#             KeyboardButton(text="📖Tanqidiy Fikrlash"),
#             KeyboardButton(text="📖Ingliz tili")
#         ],
#         [
#             KeyboardButton(text="🧮Matematika"),
#             KeyboardButton(text="📙Muammoli Masalalar"),
#         ],
#         [
#          KeyboardButton(text="Go Back.")
#         ],
#     ],
#     resize_keyboard=True
# )

menu5 = ReplyKeyboardMarkup(
    keyboard= [
        [
         KeyboardButton(text="📈 Tanqidiy fikrlash"),
         KeyboardButton(text="📖 Matematika")
        ],
        [
         KeyboardButton(text="Go Back.")
        ],
    ],
    resize_keyboard=True
)

menu6 = ReplyKeyboardMarkup(
    keyboard= [
        [
         KeyboardButton(text="Matematikadan video darslar")
        ],
        [
         KeyboardButton(text="Ingliz Tili"),
         KeyboardButton(text="Matematika"),
        ],
        [
         KeyboardButton(text="Fizika"),
        ],
        [
         KeyboardButton(text="Biologiya"),
         KeyboardButton(text="Kimyo"),
        ],
        [
         KeyboardButton(text="Go BacK")
        ],
    ],
    resize_keyboard=True
)