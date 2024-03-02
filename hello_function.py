def hello(name):
    # делаем первую букву имени большой
    out = name.title()
    # формируем приветствие
    out = 'Привет, ' + out + '.'
    # возвращаем его как результат работы функции
    return out

def start(delta):
    delta = delta * 100
    return delta