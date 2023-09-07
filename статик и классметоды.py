'''
Подвиг 8. Объявите класс CardCheck для проверки корректности информации
 на пластиковых картах. Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает 
булево значение True, если номер в верном формате и False - в противном случае.
 Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).

check_name(name) - проверяет строку name с именем пользователя карты. Возвращает 
булево значение True, если имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными 
латинскими символами и цифрами. Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в 
программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits

Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
'''
# pattern_num = r'^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'

# pattern_letter = r'^[A-Z]{1,100}\s[A-Z]{1,100}$'
import re

class CardCheck:
    PATTERN_NUM = r'^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'

    PATTERN_LETTER = r'^[A-Z]{1,100}\s[A-Z]{1,100}$'
    
    
    
    @classmethod
    def check_card_number(cls, number):
        return True if re.fullmatch(cls.PATTERN_NUM,number)else False
    @classmethod
    def check_name(cls,name):
        return True if re.fullmatch(cls.PATTERN_LETTER,name) else False

    @staticmethod
    def check_card_number(number):
        return True if re.fullmatch(CardCheck.PATTERN_NUM ,number)else False
    # Здесь лучше писать сам паттерн так как имя класса может быть изменено
    @classmethod
    def check_name(name):
        return True if re.fullmatch(CardCheck.PATTERN_LETTER, name) else False
      # Здесь лучше писать сам паттерн так как имя класса может быть изменено

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number,is_name)