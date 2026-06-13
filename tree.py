# Один человек, слева отец, справа мать
class Node:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.father = None
        self.mother = None


# Рекурсивно строит дерево предков для человека по имени
def build_tree(name, people):
    if name == "" or name not in people:
        return None
    person = people[name]
    node = Node(person["name"], person["birth"])
    node.father = build_tree(person["father"], people)
    node.mother = build_tree(person["mother"], people)
    return node


# Прямой обход, сначала человек, потом отец, потом мать
def preorder(node, result):
    if node is None:
        return
    result.append(node)
    preorder(node.father, result)
    preorder(node.mother, result)


# Обратный обход, сначала предки, потом сам человек
def postorder(node, result):
    if node is None:
        return
    postorder(node.father, result)
    postorder(node.mother, result)
    result.append(node)


# Симметричный обход, отец, человек, мать
def inorder(node, result):
    if node is None:
        return
    inorder(node.father, result)
    result.append(node)
    inorder(node.mother, result)


# Рекурсивно ищет узел по имени и возвращает его
def find_node(node, name):
    if node is None:
        return None
    if node.name == name:
        return node
    found = find_node(node.father, name)
    if found is not None:
        return found
    return find_node(node.mother, name)


# Находит человека и собирает всех его предков
def find_ancestors(root, name):
    person = find_node(root, name)
    if person is None:
        return []
    result = []
    preorder(person.father, result)
    preorder(person.mother, result)
    return result


# Обход в глубину через стек без рекурсии
def dfs_with_stack(root):
    result = []
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            continue
        result.append(node)
        stack.append(node.mother)
        stack.append(node.father)
    return result


# Сортировка выбором по дате рождения
def sort_by_birth(members):
    result = list(members)
    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j].birth < result[smallest].birth:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result


# Собирает всех людей из файла, включая родню по браку
def all_people(people):
    result = []
    for name in people:
        person = people[name]
        result.append(Node(person["name"], person["birth"]))
    return result
