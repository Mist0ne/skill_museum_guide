# flake8: noqa: E501
import random
from typing import Dict, List, Any
from . import first_museum, main_phrases


class Skill:
    def __init__(self) -> None:
        self._sessionStorage: Dict = dict()  # Хранилище данных о сессиях.

    # Функция для непосредственной обработки диалога.
    def handle_dialog(self, req, res) -> None:
        res['version'] = req['version']
        res['session'] = req['session']
        res['response'] = {
            'end_session': False
        }

        user_id = req['session']['user_id']
        original_utterance = req['request']['original_utterance'].lower()

        # Обрабатываем вход в скилл
        if req['session']['new']:
            self._sessionStorage[user_id] = {
                'suggests': main_phrases.welcome_text['suggests']
            }

            res['response']['text'] = main_phrases.welcome_text['text']
            res['response']['tts'] = main_phrases.welcome_text['tts']
            res['response']['buttons'] = self.get_suggests(user_id)
            res['session_state'] = {'museum': 1, 'second_step': 'rules'}
            return

        elif req['state']['session']['second_step'] == 'rules' \
                and req['state']['session']['museum'] == 1 and \
                (original_utterance in first_museum.first_hall_synonims
                 or original_utterance in first_museum.second_hall_synonims
                 or original_utterance in first_museum.third_hall_synonims
                 or original_utterance in first_museum.fourth_hall_synonims
                 or original_utterance in first_museum.fifth_hall_synonims
                 or original_utterance in first_museum.sixth_hall_synonims):
            res['response']['text'] = main_phrases.rules['text']
            res['response']['tts'] = main_phrases.rules['tts']
            self._sessionStorage[user_id] = {
                'suggests': main_phrases.rules['suggests']
            }
            res['response']['buttons'] = self.get_suggests(user_id)
            res['session_state'] = {'museum': 1, 'second_step': 'read_card', 'rules': True, 'exhibit': 1}
            if original_utterance in first_museum.first_hall_synonims:
                res['session_state']['hall'] = 1
            elif original_utterance in first_museum.second_hall_synonims:
                res['session_state']['hall'] = 2
            elif original_utterance in first_museum.third_hall_synonims:
                res['session_state']['hall'] = 3
            elif original_utterance in first_museum.fourth_hall_synonims:
                res['session_state']['hall'] = 4
            elif original_utterance in first_museum.fifth_hall_synonims:
                res['session_state']['hall'] = 5
            elif original_utterance in first_museum.sixth_hall_synonims:
                res['session_state']['hall'] = 6
            return

        elif req['state']['session']['second_step'] == 'read_card' \
                and req['state']['session']['museum'] == 1 \
                and original_utterance in main_phrases.next_exhibit_synonims:
            current_hall = req['state']['session']['hall']
            current_exhibit = req['state']['session']['exhibit']
            random_suggest_index = random.randint(0, len(main_phrases.question_between_exhibits)-1)
            random_suggest: Any = main_phrases.question_between_exhibits[random_suggest_index].copy()
            if current_exhibit in first_museum.data[current_hall]:
                current_data = first_museum.data[current_hall][current_exhibit]
                res['response']['audio_player'] = {
                    'playlist': [
                        {
                            'stream': {
                                'track_id': '1',
                                'source_type': 'url',
                                'source': current_data['audio']
                            },
                            'meta': {
                                'title': first_museum.audio_descriptions[current_hall][current_exhibit],
                                'sub_title': first_museum.audio_descriptions[current_hall]['subtitle']
                            }
                        },
                        {
                            'stream': {
                                'track_id': '2',
                                'source_type': 'url',
                                'source': main_phrases.question_between_exhibits_audio[random_suggest_index]['audio']
                            },
                        }
                    ]
                }
                res['response']['card'] = {
                    'type': 'BigImage',
                    'image_url': current_data['picture']
                }
                if current_exhibit == 1:
                    random_suggest['suggests'] = [random_suggest['suggests'][0], random_suggest['suggests'][1]]
                self._sessionStorage[user_id] = {
                    'suggests': random_suggest['suggests']
                }
                res['response']['text'] = random_suggest['text']
                res['response']['tts'] = ''
                res['session_state'] = {'museum': 1, 'second_step': 'read_card', 'hall': current_hall,
                                        'exhibit': current_exhibit + 1}
            else:
                random_suggest = random.choice(list(main_phrases.hall_is_over))
                suggests = []
                for i in range(len(first_museum.halls_names)):
                    if i + 1 != current_hall:
                        suggests.append(first_museum.halls_names[i])
                self._sessionStorage[user_id] = {
                    'suggests': suggests
                }
                res['response']['text'] = str(random_suggest['text']).format(first_museum.halls_names[current_hall - 1]) + \
                                          '\n\n' + ', '.join(suggests)
                res['session_state'] = {'museum': 1, 'second_step': 'new_hall_choose', 'hall': current_hall}

            res['response']['buttons'] = self.get_suggests(user_id)
            return

        elif req['state']['session']['second_step'] == 'new_hall_choose' \
                and req['state']['session']['museum'] == 1 and \
                (original_utterance in first_museum.first_hall_synonims
                 or original_utterance in first_museum.second_hall_synonims
                 or original_utterance in first_museum.third_hall_synonims
                 or original_utterance in first_museum.fourth_hall_synonims
                 or original_utterance in first_museum.fifth_hall_synonims
                 or original_utterance in first_museum.sixth_hall_synonims):
            hall_number = 1
            if original_utterance in first_museum.first_hall_synonims:
                hall_number = 1
            elif original_utterance in first_museum.second_hall_synonims:
                hall_number = 2
            elif original_utterance in first_museum.third_hall_synonims:
                hall_number = 3
            elif original_utterance in first_museum.fourth_hall_synonims:
                hall_number = 4
            elif original_utterance in first_museum.fifth_hall_synonims:
                hall_number = 5
            elif original_utterance in first_museum.sixth_hall_synonims:
                hall_number = 6
            current_data = first_museum.data[hall_number][1]
            random_suggest_index = random.randint(0, len(main_phrases.question_between_exhibits)-1)
            random_suggests = main_phrases.question_between_exhibits[random_suggest_index].copy()
            res['response']['audio_player'] = {
                'playlist': [
                    {
                        'stream': {
                            'track_id': '1',
                            'source_type': 'url',
                            'source': current_data['audio']
                        },
                        'meta': {
                            'title': first_museum.audio_descriptions[hall_number][1],
                            'sub_title': first_museum.audio_descriptions[hall_number]['subtitle']
                        }
                    },
                    {
                        'stream': {
                            'track_id': '2',
                            'source_type': 'url',
                            'source': main_phrases.question_between_exhibits_audio[random_suggest_index]['audio']
                        },
                    }
                ]
            }
            res['response']['card'] = {
                'type': 'BigImage',
                'image_url': current_data['picture']
            }
            res['response']['text'] = random_suggests['text']
            res['response']['tts'] = ''
            self._sessionStorage[user_id] = {
                'suggests': [random_suggests['suggests'][0], random_suggests['suggests'][1]]
            }
            res['response']['buttons'] = self.get_suggests(user_id)
            res['session_state'] = {'museum': 1, 'second_step': 'read_card', 'hall': hall_number, 'exhibit': 2}
            return

        elif original_utterance in main_phrases.repeat_synonims \
                and req['state']['session']['museum'] == 1:
            if 'rules' not in req['state']['session'] and 'exhibit' in req['state']['session'] and 'hall' in \
                    req['state']['session']:
                current_hall = req['state']['session']['hall']
                current_exhibit = req['state']['session']['exhibit'] - 1
                current_data = first_museum.data[current_hall][current_exhibit]
                random_suggest_index = random.randint(0, len(main_phrases.question_between_exhibits)-1)
                random_suggest = main_phrases.question_between_exhibits[random_suggest_index].copy()
                res['response']['audio_player'] = {
                    'playlist': [
                        {
                            'stream': {
                                'track_id': '1',
                                'source_type': 'url',
                                'source': current_data['audio']
                            },
                            'meta': {
                                'title': first_museum.audio_descriptions[current_hall][current_exhibit],
                                'sub_title': first_museum.audio_descriptions[current_hall]['subtitle']
                            }
                        },
                        {
                            'stream': {
                                'track_id': '2',
                                'source_type': 'url',
                                'source': main_phrases.question_between_exhibits_audio[random_suggest_index]['audio']
                            },
                        }
                    ]
                }
                res['response']['card'] = {
                    'type': 'BigImage',
                    'image_url': current_data['picture']
                }
                if current_exhibit == 1:
                    random_suggest['suggests'] = [random_suggest['suggests'][0], random_suggest['suggests'][1]]
                self._sessionStorage[user_id] = {
                    'suggests': random_suggest['suggests']
                }
                res['response']['text'] = random_suggest['text']
                res['response']['tts'] = ''
                res['session_state'] = {'museum': 1, 'second_step': 'read_card', 'hall': current_hall,
                                        'exhibit': current_exhibit + 1}

                res['response']['buttons'] = self.get_suggests(user_id)
            else:
                res['response']['text'] = main_phrases.rules['text']
                res['response']['tts'] = main_phrases.rules['tts']
                self._sessionStorage[user_id] = {
                    'suggests': main_phrases.rules['suggests']
                }
                res['response']['buttons'] = self.get_suggests(user_id)
                res['session_state'] = {'museum': 1, 'second_step': 'read_card', 'rules': True,
                                        'hall': req['state']['session']['hall'], 'exhibit': 1}
            return

        elif original_utterance in main_phrases.go_back_synonims and 'exhibit' in req['state']['session'] and \
                req['state']['session']['museum'] == 1 and req['state']['session']['exhibit'] > 2:
            current_hall = req['state']['session']['hall']
            current_exhibit = req['state']['session']['exhibit'] - 2
            current_data = first_museum.data[current_hall][current_exhibit]
            random_suggest_index = random.randint(0, len(main_phrases.question_between_exhibits)-1)
            random_suggest = main_phrases.question_between_exhibits[random_suggest_index].copy()
            res['response']['audio_player'] = {
                'playlist': [
                    {
                        'stream': {
                            'track_id': '1',
                            'source_type': 'url',
                            'source': current_data['audio']
                        },
                        'meta': {
                            'title': first_museum.audio_descriptions[current_hall][current_exhibit],
                            'sub_title': first_museum.audio_descriptions[current_hall]['subtitle']
                        }
                    },
                    {
                        'stream': {
                            'track_id': '2',
                            'source_type': 'url',
                            'source': main_phrases.question_between_exhibits_audio[random_suggest_index]['audio']
                        },
                    }
                ]
            }
            res['response']['card'] = {
                'type': 'BigImage',
                'image_url': current_data['picture']
            }
            if current_exhibit == 1:
                random_suggest['suggests'] = [random_suggest['suggests'][0], random_suggest['suggests'][1]]
            self._sessionStorage[user_id] = {
                'suggests': random_suggest['suggests']
            }
            res['response']['text'] = random_suggest['text']
            res['response']['tts'] = ''
            res['session_state'] = {'museum': 1, 'second_step': 'read_card', 'hall': current_hall,
                                    'exhibit': current_exhibit + 1}
            res['response']['buttons'] = self.get_suggests(user_id)
            return

        elif original_utterance in main_phrases.stop_synonims:
            random_phrase = random.choice(main_phrases.exit)
            res['response']['text'] = random_phrase
            res['response']['tts'] = random_phrase
            res['response']['card'] = {
                'type': 'Link',
                'url': main_phrases.exit_card['url'],
                'title': main_phrases.exit_card['title'],
                'text': main_phrases.exit_card['text'],
                'image_url': main_phrases.exit_card['image_url'],
            }
            res['response']['end_session'] = True
            return

        else:
            random_phrase = random.choice(main_phrases.unclear)
            if req['state']['session']['second_step'] == 'rules':
                res['response']['text'] = random_phrase + '\n\n' + str(main_phrases.welcome_text['text']).split('\n')[2]
                res['response']['tts'] = random_phrase + '\n' + str(main_phrases.welcome_text['tts']).split('\n')[2]
                self._sessionStorage[user_id] = {
                    'suggests': main_phrases.welcome_text['suggests']
                }
                res['response']['buttons'] = self.get_suggests(user_id)
            elif req['state']['session']['second_step'] == 'new_hall_choose':
                random_suggest = random.choice(list(main_phrases.hall_is_over))
                current_hall = req['state']['session']['hall']
                new_halls = []
                for hall_id in range(len(first_museum.halls_names)):
                    if hall_id+1 != req['state']['session']['hall']:
                        new_halls.append(first_museum.halls_names[hall_id])
                res['response']['text'] = random_phrase + '\n\n' + \
                                          str(random_suggest['text']).format(first_museum.halls_names[current_hall - 1]) \
                                          + '\n\n' + ', '.join(new_halls)
                res['response']['tts'] = random_phrase + '\n' + ', '.join(new_halls)
                self._sessionStorage[user_id] = {
                    'suggests': new_halls
                }
                res['response']['buttons'] = self.get_suggests(user_id)
            else:
                res['response']['text'] = random_phrase
                res['response']['tts'] = random_phrase
            res['session_state'] = {}
            for key in req['state']['session'].keys():
                res['session_state'][key] = req['state']['session'][key]
            return

    # Функция возвращает подсказки для ответа.
    def get_suggests(self, user_id: str) -> List:
        session = self._sessionStorage.get(user_id) or {'suggests': []}

        suggests: List = [
            {'title': suggest, 'hide': True}
            for suggest in session['suggests']
        ]

        return suggests


skill: Skill = Skill()
