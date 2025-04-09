from doublelink import DoublyLinkedList
from builtin import BuiltinList 

choice = ''
while choice not in ['1', '2']:
    print("\nОберіть реалізацію списку для демонстрації:")
    print("1: DoublyLinkedList")
    print("2: BuiltinList")
    choice = input("Ваш вибір (введіть 1 або 2): ")
    if choice not in ['1', '2']:
        print("Введіть 1 або 2.")

if choice == '1':
    ListImplementation = DoublyLinkedList
    impl_name = "DoublyLinkedList"
else: 
    ListImplementation = BuiltinList
    impl_name = "BuiltinList"


print(f"\n--- Демонстрація {impl_name} ---") 

# Створення та append
my_list = ListImplementation()
print(f"\nСтворено список: {my_list}")
print("Додаємо 'a', 'b', 'c' за допомогою append...")
my_list.append('a')
my_list.append('b')
my_list.append('c')
print(f"Список: {my_list}, Довжина: {my_list.length()}")

# insert
print("\nВставляємо 'x' на позицію 1 (insert)...")
my_list.insert('x', 1)
print(f"Список: {my_list}")

# get
print(f"\nЕлемент на позиції 2 (get): '{my_list.get(2)}'")

# delete
print("\nВидаляємо елемент з індексом 0 (delete)...")
deleted = my_list.delete(0)
print(f"Видалено '{deleted}'. Список: {my_list}")

# findFirst / findLast
print(f"\nfindFirst('c'): {my_list.findFirst('c')}")
print(f"findLast('x'): {my_list.findLast('x')}")
print(f"findFirst('z'): {my_list.findFirst('z')}")

# deleteAll
print("\nДодаємо 'c' ще раз: список має стати схожим на [x, b, c, c]")
my_list.append('c')
print(f"Список перед deleteAll('c'): {my_list}")
my_list.deleteAll('c')
print(f"Список після deleteAll('c'): {my_list}") 

# reverse
print(f"\nСписок перед reverse: {my_list}")
my_list.reverse()
print(f"Список після reverse: {my_list}") 

# clone
print("\nКлонуємо поточний список...")
cloned_list = my_list.clone()
print(f"Оригінал: {my_list}")
print(f"Клон:     {cloned_list}")
print("Додаємо '!' до оригіналу...")
my_list.append('!') 
print(f"Оригінал після зміни: {my_list}")
print(f"Клон (має бути без '!'): {cloned_list}") 

# extend
print("\nРозширюємо клон списком ['1', '2'] (extend)...")
list_to_extend = ListImplementation()
list_to_extend.append('1')
list_to_extend.append('2')
cloned_list.extend(list_to_extend) 
print(f"Розширений клон: {cloned_list}")
print(f"Список, яким розширювали (має бути незмінним): {list_to_extend}")

# clear
print(f"\nОчищуємо клон (clear)...")
cloned_list.clear()
print(f"Клон після clear: {cloned_list}")
print(f"Довжина клона: {cloned_list.length()}")


print(f"\n--- Демонстрація {impl_name} завершена ---")
