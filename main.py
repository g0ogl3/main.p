name = input('Введите свое имя:')
print('🖐Здравствуйте', name)
word = input("❓Введите непонятное слово (с большой буквы:)")
meme_dict = {
            "Кринж": "что-то очень странное или стыдное",
            "Лол": "что-то очень смешное",
            "Рофл":"шутка",
            "Щищ":"одобрение или восторг",
            "Криповый":"страшный или пугающий",
            "Агриться":"злиться",
            "Угарать":"смеяться",
            "Войсить":"записывать голосовое сообщение",
            "Байтить":"провоцировать",
            "Вайб":"атмосфера, настроение",
            "Варик":"вариант",
            "Задонатить":"пожертвовать деньги в какую либо игру либо оформить какую либо подписку",
            "Изи":"легко",
            "Краш":"предмет тайной или безответной влюблённости",
            "Овердофига":"много чего либо",
            "Имба":"что-то очень хорошее или крутое",
            }
if word in meme_dict.keys():
    print(word,'⇉',meme_dict[word])
else:
    print('Извините у нас в словаре не такого слова')
