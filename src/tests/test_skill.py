import json
from pathlib import Path

import pytest

from skill_museum_guide.skill import skill

base_req_file_name = Path(__file__).parent / 'base_request.json'


@pytest.mark.parametrize('phrase_text, new_session, answer_text', [
    ('космос', True, """Добро пожаловать в аудиотур по московскому Музею космонавтики! Путеводитель расскажет про начало покорения космоса, создание орбитальных станций, достижения отечественной, зарубежной космонавтики и многое-многое другое. Обещаю, понравится не только юным мечтателям-космонавтам, но и взрослым!

С какого зала начнём экскурсию? 
- Утро космической эры
- Творцы космической эры
- Космический дом на орбите
- Исследования планет Солнечной системы
- Международное сотрудничество
- Международный космический парк
"""),
])
def test_skill(phrase_text, new_session, answer_text):
    req = {}
    resp = {}
    with open(base_req_file_name) as f:
        req = json.load(f)

    req['request']['original_utterance'] = phrase_text
    req['request']['command'] = phrase_text
    req['session']['new'] = new_session

    skill.handle_dialog(req, resp)

    assert answer_text in resp['response']['text']
