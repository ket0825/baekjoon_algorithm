class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self, node):
        result = []
        if node:
            result = self.inorder_traversal(node.left)
            result.append(node.value)
            result += self.inorder_traversal(node.right)
        return result

# 일반 트리
    
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        
        # 현재 노드 출력
        print("  " * level + "├─", node.value)
        
        # 자식 노드 재귀적으로 출력
        for child in node.children:
            self.print_tree(child, level + 1)

def create_tree():
    return {}

def add_node(tree, parent, value):
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(value)

my_tree = create_tree()
add_node(my_tree, 'root', 'A')
add_node(my_tree, 'A', 'B')
add_node(my_tree, 'A', 'C')
add_node(my_tree, 'B', 'D')
print(my_tree)

# 이진 트리 생성 및 사용 예시
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

# 작은 순임.
print(tree.inorder_traversal(tree.root))  # [3, 5, 7, 10, 15]

# 일반 트리 생성 및 사용 예시
family_tree = Tree("할아버지")
father = TreeNode("아버지")
uncle = TreeNode("삼촌")
family_tree.root.add_child(father)
family_tree.root.add_child(uncle)
son = TreeNode("아들")
daughter = TreeNode("딸")
father.add_child(son)
father.add_child(daughter)

family_tree.print_tree()