d = {"app":False,'app2':False,'app3':True}
d.pop('app')
#print(len(d.keys()))
#print(d)

class AppStore:
    DICT_APP = {}
    
    def add_application(self, app):
        self.DICT_APP.update({app.name:app.blocked })
       
    def remove_application(self, app):
        self.DICT_APP.pop(app.name)

    def block_application(self, app):
        self.DICT_APP[app.name]=True
    def total_apps(self) :
        return len(self.DICT_APP.keys())


class Application:
    def __init__(self,name,blocked=False) -> None:
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")
print(app_youtube.blocked)
#assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"

store.add_application(app_youtube)
store.block_application(app_youtube)
print(app_youtube.name)
#assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"

app_stepik = Application("Stepik")
store.add_application(app_stepik)
print(store.total_apps())
#assert store.total_apps() == 2, "неверное число приложений в магазине"

store.remove_application(app_youtube)
#assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"
print(store.total_apps())