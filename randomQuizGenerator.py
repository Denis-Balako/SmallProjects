#! python3
# randomQuizGenerator - создаёт билеты с вопросами и ответами,
# расположенными в случайном порядке, вместе с ключами ответов

import random
# Данные билетов: ключи - названия штатов, а значения - столицы
capitals = {'Айдахо': 'Бойсе', 'Айова': 'Де-Мойн', 'Алабама': 'Монтгомери',
            'Аляска': 'Джуно', 'Аризона': 'Финикс', 'Арканзас': 'Литл-Рок',
            'Вайоминг': 'Шайенн', 'Вашингтон': 'Олимпия', 'Вермонт': 'Монтпилиер',
            'Виргиния': 'Ричмонд', 'Висонсин': 'Мадисон', 'Гавайи': 'Гонолулу',
            'Делавэр': 'Довер', 'Джорджия': 'Атланта', 'Западная Виргиния': 'Чарлстон',
            'Иллинойс': 'Спрингфилд', 'Индиана': 'Индианаполис', 'Калифорния': 'Сакраменто',
            'Канзас': 'Топика', 'Кентукки': 'Франкфорт', 'Колорадо': 'Денвер', 'Коннектикут': 'Хартфорд',
            'Луизиана': 'Батон-Руж', 'Массачусетс': 'Бостон', 'Миннесота': 'Сент-Пол', 'Миссисипи': 'Джэксон',
            'Миссури': 'Джефферсон-Сити', 'Мичиган': 'Лансинг', 'Монтана': 'Хелена', 'Мэн': 'Огаста',
            'Мэриленд': 'Аннаполис', 'Небраска': 'Линкольн', 'Невада': 'Карсон-Сити', 'Нью-Джерси': 'Трентон',
            }
