class Node:
    """Один человек в дереве, есть отец и мать."""

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.father = None
        self.mother = None


def build_tree(name, people):
    """
    Рекурсивно строит дерево предков для человека по его имени.
    Слева отец, справа мать, пустое имя завершает ветку.
    """
    if name == "" or name not in people:
        return None
    person = people[name]
    node = Node(person["name"], person["birth"])
    # сначала строим ветку отца, потом ветку матери
    node.father = build_tree(person["father"], people)
    node.mother = build_tree(person["mother"], people)
    return node


def preorder(node, result):
    """Прямой обход, сначала сам человек, затем отец и мать."""
    if node is None:
        return
    result.append(node)
    preorder(node.father, result)
    preorder(node.mother, result)


def postorder(node, result):
    """Обратный обход, сначала предки, потом сам человек."""
    if node is None:
        return
    postorder(node.father, result)
    postorder(node.mother, result)
    result.append(node)


def inorder(node, result):
    """Симметричный обход, отец -> человек -> мать."""
    if node is None:
        return
    inorder(node.father, result)
    result.append(node)
    inorder(node.mother, result)


def find_node(node, name):
    """Рекурсивно ищет человека по имени и возвращает его узел."""
    if node is None:
        return None
    if node.name == name:
        return node
    # ищем сначала в ветке отца, потом в ветке матери
    found = find_node(node.father, name)
    if found is not None:
        return found
    return find_node(node.mother, name)


def find_ancestors(root, name):
    """
    Находит человека в дереве и собирает всех его предков.
    Возвращает пустой список, если человека нет в дереве.
    """
    person = find_node(root, name)
    if person is None:
        return []
    result = []
    # предки это все люди из веток отца и матери
    preorder(person.father, result)
    preorder(person.mother, result)
    return result


def dfs_with_stack(root):
    """Обход дерева в глубину."""
    result = []
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            continue
        result.append(node)
        # кладем мать раньше отца, чтобы отец обработался первым
        stack.append(node.mother)
        stack.append(node.father)
    return result


def sort_by_birth(members):
    """Сортировка выбором, упорядочивает людей по дате рождения."""
    result = list(members)
    for i in range(len(result)):
        # ищем самого раннего среди оставшихся и ставим его на место i
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j].birth < result[smallest].birth:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result


def all_people(people):
    """Собирает всех людей из файлау."""
    result = []
    for name in people:
        person = people[name]
        result.append(Node(person["name"], person["birth"]))
    return result
