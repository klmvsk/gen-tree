from loader import load_people
from tree import build_tree, preorder, postorder, inorder, find_ancestors, dfs_with_stack, sort_by_birth


ROOT_NAME = "Анна"
WIDTH = 44


def show_header():
    print("=" * WIDTH)
    print("ГЕНЕАЛОГИЧЕСКОЕ ДЕРЕВО".center(WIDTH))
    print("=" * WIDTH)


def show_menu():
    print()
    print("  1. Родословная, прямой обход")
    print("  2. Родословная, обратный обход")
    print("  3. Родословная, симметричный обход")
    print("  4. Найти предков человека")
    print("  5. Члены семьи по дате рождения")
    print("  6. Обход в глубину через стек")
    print("  0. Выход")
    print()


def show_list(title, people):
    print()
    print(title)
    print("-" * WIDTH)
    if len(people) == 0:
        print("  ничего не найдено")
    else:
        number = 1
        for person in people:
            print("  " + str(number) + ". " + person.name + ", " + person.birth)
            number = number + 1
    print("-" * WIDTH)


def main():
    people = load_people("family.json")
    root = build_tree(ROOT_NAME, people)
    show_header()

    while True:
        show_menu()
        choice = input("Ваш выбор: ")

        if choice == "1":
            result = []
            preorder(root, result)
            show_list("Родословная, прямой обход", result)
        elif choice == "2":
            result = []
            postorder(root, result)
            show_list("Родословная, обратный обход", result)
        elif choice == "3":
            result = []
            inorder(root, result)
            show_list("Родословная, симметричный обход", result)
        elif choice == "4":
            name = input("Имя человека: ")
            show_list('Предки человека "' + name + '"', find_ancestors(root, name))
        elif choice == "5":
            members = []
            preorder(root, members)
            members = sort_by_birth(members)
            show_list("Члены семьи по дате рождения", members)
        elif choice == "6":
            show_list("Обход в глубину через стек", dfs_with_stack(root))
        elif choice == "0":
            print()
            print("До свидания")
            break
        else:
            print()
            print("Нет такого пункта, попробуйте снова")


main()
