from node import Node


def build_tree(name, people):
    if name == "" or name not in people:
        return None
    person = people[name]
    node = Node(person["name"], person["birth"])
    node.father = build_tree(person["father"], people)
    node.mother = build_tree(person["mother"], people)
    return node


def preorder(node, result):
    if node is None:
        return
    result.append(node)
    preorder(node.father, result)
    preorder(node.mother, result)


def postorder(node, result):
    if node is None:
        return
    postorder(node.father, result)
    postorder(node.mother, result)
    result.append(node)


def inorder(node, result):
    if node is None:
        return
    inorder(node.father, result)
    result.append(node)
    inorder(node.mother, result)


def find_node(node, name):
    if node is None:
        return None
    if node.name == name:
        return node
    found = find_node(node.father, name)
    if found is not None:
        return found
    return find_node(node.mother, name)


def find_ancestors(root, name):
    person = find_node(root, name)
    if person is None:
        return []
    result = []
    preorder(person.father, result)
    preorder(person.mother, result)
    return result


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


def sort_by_birth(members):
    result = list(members)
    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j].birth < result[smallest].birth:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result
