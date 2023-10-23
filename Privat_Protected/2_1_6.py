'''
идео-разбор подвига (решение смотреть только после своей попытки):

 https://youtu.be/w0SAD6zNLlw

Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов
 класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author
 объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price объектов 
класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title
 объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author
 объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price
 объектов класса Book;

Объекты класса Book предполагается создавать командой:

book = Book(автор, название, цена)

При этом, в каждом объекте должны создаваться приватные локальные свойства:

__author - строка с именем автора;
__title - строка с названием книги;
__price - целое число с ценой книги.

P.S. В программе требуется объявить только класс. Ничего на экран выводить
 не нужно.
'''

class Book():
    def __init__(self,author,title,price) -> None:
        self.__author = author
        self.__title = title
        self.__price = price
    @classmethod
    def __check_str(cls,param):
        return  isinstance(param,str)
        
    @classmethod
    def __check_int(cls,param):
        return isinstance(param,int)
    
    def set_title(self, title):
        if self.__check_str(title):
            self.__title = title
    def  set_author(self, author):
        if self.__check_str(author):
            self.__author = author
    def set_price(self, price):
        if self.__check_int(price):
            self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def  get_price(self):
        return self.__price


book = Book('50 Cent', 'Aboba', 999)
book.set_title('Amogus')
book.set_author('NLE Choppa')
book.set_price(123)
book.get_title()
book.get_author()
book.get_price()