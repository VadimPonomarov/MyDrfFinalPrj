from core.services.g4f_extras.generators import J4fContentGenerator


def generate_task(content: str):
    return J4fContentGenerator(
        init=f''' 
    У меня есть текст: "{content}". В нем, возможно, была использована ненормативная лексика. Текст может быть написан только на русском, украинском, английском языках. Другие варианты недопустимы. Иногда, для написания плохих слов злоумышленником может использоваться вариант их транслитерации, например 'HUYLO'='ХУЙЛО'. Транслитерация плохих слов считается недопустимой и подлежит очистке.
    ''',
        body=f'''
    Так как текст впоследствии может быть опубликован в интернете, его необходимо очистить от неправильной лексики.
    ''',
        task=f'''
    Очистку текста необходимо осуществить путем замены плохих слов на *.
    ''',
        extras=f'''
    Текст нужно вернуть в виде объекта в формате json (key=res и value=текст).
    '''
    )
