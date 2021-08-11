#uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    result = 'Приветствуем, дорогой друг! Здесь ты можешь получить информацию о семье, друзьях, а так же о некоторых странах!'
    return(result)

@app.get('/family')
def family1():
    return('Члены семьи: Кайрат, Айгуль, Валихан')

@app.get('/family/{name}')
def family2(name):
    db1_info = {
        'kairat': {
            'name': 'Кайрат',
            'surname': 'Ильясов',
            'age': 34,
            'work': 'учитель',
            'hobby': 'слушать музыку',
            'residency': 'Астана'
        },
        'aigul': {
            'name': 'Айгуль',
            'surname': 'Алиева',
            'age': 44,
            'work': 'бухгалтер',
            'hobby': 'чтение книг',
            'residency': 'Алматы'
        },
        'valikhan': {
            'name': 'Валихан',
            'surname': 'Искаков',
            'age': 20,
            'work': 'финансист',
            'hobby': 'просмотр фильмов',
            'residency': 'Семипалатинск'
        }
    }
    result = '%s %s. Возраст: %s. Должность: %s. Хобби: %s. Город проживания: %s' % (db1_info[name]['name'], db1_info[name]['surname'],
    db1_info[name]['age'], db1_info[name]['work'], db1_info[name]['hobby'], db1_info[name]['residency'])

    return result

@app.get('/friends')
def friends1():
    return('Друзья: Абылай, Аскар и Нурбек.')

@app.get('/friends/{name}')
def friends2(name):
    db1_info = {
        'abylai': {
            'name': 'Абылай',
            'surname': 'Жунусов',
            'age': 29,
            'work': 'инженер',
            'hobby': 'фотосъёмка',
            'residency': 'Актау'
        },
        'askar': {
            'name': 'Аскар',
            'surname': 'Жакупов',
            'age': 20,
            'work': 'финансист',
            'hobby': 'просмотр фильмов',
            'residency': 'Семипалатинск'
        },
        'nurbek': {
            'name': 'Нурбек',
            'surname': 'Сыздыков',
            'age': 31,
            'work': 'юрист',
            'hobby': 'видеосъёмка',
            'residency': 'Шымкент'
        },
    }
    result = '%s %s. Возраст: %s. Должность: %s. Хобби: %s. Город проживания: %s' % (db1_info[name]['name'], db1_info[name]['surname'],
    db1_info[name]['age'], db1_info[name]['work'], db1_info[name]['hobby'], db1_info[name]['residency'])

    return result

@app.get('/countries')
def countries1():
    return('Любимые страны: Турция, Грузия, Япония.')

@app.get('/countries/{name}')
def countries2(name):
    db1_info = {
        'turkey': {
            'name': 'турция',
            'population': '82 000 000 чел',
            'area': '783 562 км2',
            'year of foundation': 1923,
            'time zone': 'GMT+3',
            'capital': 'Анкара',
            'president': 'Реджеп Тайип Эрдоган'
        },
        'georgia': {
            'name': 'грузия',
            'population': '3 720 000 чел',
            'area': '69 700 км2',
            'year of foundation': 1991,
            'time zone': 'GMT+4',
            'capital': 'Тбилиси',
            'president': 'Саломе Левановна Зурабишвили'
        },
        'japan': {
            'name': 'япония',
            'population': '126 300 000 чел',
            'area': '377 975 км2',
            'year of foundation': -660,
            'time zone': 'GMT+9',
            'capital': 'Токио',
            'president': 'Нарухито'
        }
    }
    result = '%s. Население: %s. Площадь территории: %s. Год основания: %s. Часовой пояс: %s. Столица: %s. Президент: %s.' \
             % (db1_info[name]['name'].capitalize(), db1_info[name]['population'], db1_info[name]['area'], db1_info[name]['year of foundation'],
                db1_info[name]['time zone'], db1_info[name]['capital'], db1_info[name]['president'])

    return result

