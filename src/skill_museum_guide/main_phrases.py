welcome_text = {
    "text": """Добро пожаловать в аудиотур по московскому Музею космонавтики! Путеводитель расскажет про начало покорения космоса, создание орбитальных станций, достижения отечественной, зарубежной космонавтики и многое-многое другое. Обещаю, понравится не только юным мечтателям-космонавтам, но и взрослым!

С какого зала начнём экскурсию? Утро космической эры, Творцы космической эры, Космический дом на орбите,  Исследования планет солнечной системы, международное сотрудничество и международный космический парк
""",
    "tts": """Добро пожаловать в аудиотур по московскому Музею космонавтики! Путеводитель расскажет про нач`ало покорения космоса, создание орбитальных станций, достижения отечественной, зарубежной космонавтики и многое-многое другое. Обещаю, понравится не только юным мечтателям-космонавтам, ^но^ и взрослым!

С какого зала начнём экскурсию? Утро космической эры, Творцы космической эры, Космический дом на орбите,  Исследования планет солнечной системы, международное сотрудничество и международный космический парк
""",
    "suggests": [
        "Утро космической эры",
        "Творцы космической эры",
        "Космический дом на орбите",
        "Исследования планет солнечной системы",
        "международное сотрудничество",
        "международный космический парк"
    ]
}

rules = {
    "text": """Прежде чем приступить к экскурсии по Музею космонавтики, пожалуйста, прослушайте краткие правила по управлению аудиогидом.

Чтобы перейти к следующему экспонату, скажите: «Дальше» или «Далее».

Чтобы ещё раз прослушать отрывок, скажите: «Ещё раз».
Чтобы выйти из аудиогида, скажите: «Стоп» или «Хватит».""",
    "tts": """Прежде чем приступить к экскурсии по Музею космонавтики, пожалуйста, прослушайте краткие правила по управлению аудиогидом.

Чтобы перейти к следующему экспонату, скажите: «Дальше» или «Далее».

Чтобы ещё раз прослушать отрывок, скажите: «Ещё раз».
Чтобы выйти из аудиогида, скажите: «Стоп» или «Хватит».
""",
    "suggests": [
        "Дальше",
        "Ещё раз"
    ]
}

exit_card = {
    'url': 'https://kosmo-museum.ru',
    'title': 'Московский музей Космонавтики',
    'text': 'Узнайте о других экспонатах музея и ближайших активностях на сайте.',
    'image_url': 'https://newyearskill.viktortolstov.ru.com/slava/logo_RGB-03_2.jpg'
}

suggests_between_exhibits = [
    'Дальше',
    'Ещё раз',
    'Назад'
]

question_between_exhibits = [
    {
        "text": 'Скажите: «Далее», чтобы перейти к следующему отрывку аудиогида',
        "tts": 'Скажите: «Далее», чтобы перейти к следующему отрывку аудиогида',
        "suggests": suggests_between_exhibits
    },
    {
        "text": 'Скажите: «Далее», чтобы переключить аудиогид и «Ещё раз», чтобы прослушать отрывок ещё раз',
        "tts": 'Скажите: «Далее», чтобы переключить аудиогид и «Ещё раз», чтобы прослушать отрывок ещё раз',
        "suggests": suggests_between_exhibits
    },
    {
        "text": 'Пройдёмте к следующему экспонату. Скажите: «Далее», чтобы переключить отрывок',
        "tts": 'Пройдёмте к следующему экспонату. Скажите: «Далее», чтобы переключить отрывок',
        "suggests": suggests_between_exhibits
    },
    {
        "text": 'Скажите: «Далее», чтобы перейти к следующей части аудиогида',
        "tts": 'Скажите: «Далее», чтобы перейти к следующей части аудиогида',
        "suggests": suggests_between_exhibits
    }
]

unclear = [
    'Пожалуйста, повторите. Засмотрелась на звёзды и не поняла вас',
    'Не расслышала вас. Повторите, пожалуйста'
]

exit = [
    'До скорой встречи! И спасибо вам за путешествие',
    'Возвращайтесь скорее'
]

hall_is_over = [
    {
        "text": 'Экскурсия по залу «{0}» завершилась. В какой зал пройдем дальше?',
        "tts": 'Экскурсия по залу {0} ^завершилась^. В какой зал пройдем дальше?',
    },
    {
        "text": 'Как интересно! Мы прослушали всё про «{0}». Про что будем слушать дальше?',
        "tts": 'Как интересно! Мы прослушали всё про {0}. Про что будем слушать дальше?',
    },
    {
        "text": 'Думаю, теперь вы знаете всё про «{0}». Про что будем слушать дальше?',
        "tts": 'Думаю, теперь вы знаете всё про {0}. Про что будем слушать дальше?',
    }
]

# Синонимы основных действий
next_exhibit_synonims = [
    "пройдем к следующему экспонату",
    "пойдем к следующему экспонату",
    "следующий экспонат",
    "к следующему экспонату",
    "о следующем экспонате",
    "включи про следующий экспонат",
    "пошли к следующему экспонату",
    "включить о следующем экспонате",
    "расскажи о следующем экспонате",
    "описание следующего экспоната",
    "дальше",
    "далее",
    "переход",
    "далее",
    "нэкст",
    "следующая",
    "следующий",
    "следующего",
    "следующую",
    "включить следующий отрывок",
    "переключи на следующий отрывок",
    "включи следующий отрывок аудиогида",
    "переключи на следующий отрывок аудиогида",
    "включи следующий отрывок",
    "следующая картина",
    "следующую картину",
    "следующей картиной",
    "следующие картины",
    "следующих картин",
    "следующими картинами",
    "давай следующую",
    "следующую давай",
    "давай дальше",
    "дальше давай",
    "давай далее",
    "давай следующую картину",
    "переключи дальше",
    "переключить дальше",
    "переключи следующую картину",
    "переключить следующую картину",
    "переключи на следующую",
    "переключи на следующую картину",
    "переключить следующую картину",
    "перейти дальше",
    "перейди дальше",
    "перейти к следующей",
    "перейти к следующей картине",
    "перейди к следующей",
    "перейди к следующей картине",
    "пошли к следующей",
    "пошли к следующей картине",
    "перейти к следующей работе",
    "пошли к следующей работе",
    "перейдем",
    "перейдем дальше",
    "пойдем дальше",
    "пошли дальше",
    "пойдем к следующей картине",
    "перейдем к следующей картине",
    "перейдем далее",
    "пойдем далее",
    "продолжай",
    "продолжи",
    "проигрывай дальше",
    "проиграть дальше",
    "проиграть далее",
    "проигрывай далее",
]

stop_synonims = [
    "стоп",
    "хватит",
    "выйти",
    "остановись",
    "прекрати",
    "отстань",
    "больше не нужно",
    "не нужно",
    "не надо",
    "не включай",
    "не переключай",
    "не нужно следующую",
    "не надо следующую",
    "харэ, захлопнись",
    "замолчи",
    "молчать",
    "ни звука",
]

repeat_synonims = [
    "повтор",
    "повторить",
    "повтори",
    "расскажи снова",
    "заново",
    "снова",
    "еще раз",
    "скажи еще раз",
    "повтори еще раз",
    "повторить еще раз",
    "еще разок",
    "еще разик",
    "сначала",
    "по новой",
    "ещё раз",
]

agree_synonims = [
    "да",
    "конечно",
    "конечно же",
    "ага",
    "возможно",
    "определенно да",
    "точно",
    "так",
    "именно так",
    "без сомнений",
    "абсолютно точно",
    "верно",
    "ну да",
    "скорее всего",
    "наверное",
    "естественно",
    "а то",
    "как же иначе",
    "без вариантов",
    "только так",
    "сто процентов",
    "по-другому и быть не может",
    "вероятно",
    "хорошо",
    "так точно",
    "начнем",
    "да, давай",
    "давай",
    "запускай",
    "включай",
    "начинай",
    "давай запускай",
    "включись",
    "играй",
    "заводи шарманку",
]

disagree_synonims = [
    "Нет",
    "не нужно",
    "не хочу",
    "незачем",
    "не хотим",
    "не запускай",
    "не включай",
    "не начинай",
    "вовсе нет",
    "прекрати",
    "остановись",
    "хватит",
    "стоп",
    "харэ",
    "выйди",
    "уйди",
    "не буду",
    "больше не нужно",
    "не надо следующую",
    "не надо дальше",
    "заткнись",
]

go_back_synonims = [
    "назад",
    "предыдущий",
    "предыдущий отрывок",
    "предыдущая часть",
    "предыдущая картина",
    "предыдущий экспонат",
    "давай назад",
    "переключи назад",
    "открой предыдущий",
    "открой предыдущий отрывок",
    "переключи на предыдущий",
    "переключи на предыдущий отрывок",
    "переключи предыдущую картину",
    "переключи предыдущий экспонат",
    "включи предыдущий",
    "включи на предыдущий",
    "включи предыдущий отрывок",
    "включи предыдущую картину",
    "включи предыдущий экспонат",
    "предыдущую",
    "предшествующую",
    "предшествующий",
    "включить предыдущую ",
    "включить предыдущую картину",
    "включить предыдущий отрывок",
    "включить предыдущую часть",
    "включить предыдущий экспонат",
    "включить про предыдущий экспонат",
    "вернись назад",
    "верни назад",
    "вернись к предыдущей",
    "вернись к предыдущей части",
    "вернись к предыдущему отрывку",
    "вернись к предыдущей картине",
    "вернись к предыдущему экспонату",
    "проиграй назад",
    "проиграй предыдущий",
    "проиграй на предыдущий",
    "проиграй предыдущий отрывок",
    "проиграй предыдущую картину",
    "проиграй предыдущий экспонат",
]
