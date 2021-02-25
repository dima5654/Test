#3 завдання
class Море_океан:
    pass

class Остров_Буян(Море_океан):
    pass
class Дуб(Остров_Буян):
    pass
class Сундук(Дуб):
    pass
class Заяц(Сундук):
    pass
class Утка(Заяц):
    pass
class Яйцо(Утка):
    pass
class Игла(Яйцо):
    pass
class Смерть_Кощея(Игла):
    def end(self):
        print("Казочці кінець")
петро = Смерть_Кощея()
петро.end()
