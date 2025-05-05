class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []

    def learn_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        return self.commands

class HomeAnimal(Animal): pass
class Dog(HomeAnimal): pass
class Cat(HomeAnimal): pass
class Hamster(HomeAnimal): pass

class PackAnimal(Animal): pass
class Horse(PackAnimal): pass
class Donkey(PackAnimal): pass

class Counter:
    def __init__(self):
        self.count = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise Exception("Resource already closed")
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.closed = True

def main():
    animals = []
    while True:
        print("\n1. Завести новое животное")
        print("2. Посмотреть команды животного")
        print("3. Обучить команде")
        print("4. Выйти")
        choice = input("Выбор: ")

        if choice == "1":
            with Counter() as counter:
                kind = input("Вид (dog/cat/horse): ").lower()
                name = input("Имя: ")
                birth = input("Дата рождения (YYYY-MM-DD): ")
                if kind == "dog":
                    animal = Dog(name, birth)
                elif kind == "cat":
                    animal = Cat(name, birth)
                elif kind == "horse":
                    animal = Horse(name, birth)
                else:
                    print("Неизвестный вид.")
                    continue
                animals.append(animal)
                counter.add()

        elif choice == "2":
            for a in animals:
                print(f"{a.name}: {a.show_commands()}")

        elif choice == "3":
            name = input("Введите имя животного: ")
            command = input("Введите команду: ")
            for a in animals:
                if a.name == name:
                    a.learn_command(command)
                    print("Обучено.")
                    break
            else:
                print("Животное не найдено.")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
