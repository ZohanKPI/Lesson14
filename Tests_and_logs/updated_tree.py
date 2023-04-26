from tree import Tree

def test_node_addition():
    tree = Tree()
    tree.node_addition(5)
    assert tree.root.value == 5

    tree.node_addition(3)
    assert tree.root.left.value == 3

    tree.node_addition(7)
    assert tree.root.right.value == 7

    tree.node_addition(1)
    assert tree.root.left.left.value == 1

    tree.node_addition(4)
    assert tree.root.left.right.value == 4

    tree.node_addition(6)
    assert tree.root.right.left.value == 6

    tree.node_addition(8)
    assert tree.root.right.right.value == 8

def test_min_max_element():
    tree = Tree()
    tree.node_addition(5)
    tree.node_addition(3)
    tree.node_addition(7)
    tree.node_addition(1)
    tree.node_addition(4)
    tree.node_addition(6)
    tree.node_addition(8)

    assert tree.min_element() == 1
    assert tree.max_element() == 8

def test_node_deletion():
    tree = Tree()
    tree.node_addition(5)
    tree.node_addition(3)
    tree.node_addition(7)
    tree.node_addition(1)
    tree.node_addition(4)
    tree.node_addition(6)
    tree.node_addition(8)

    tree.node_deletion(1)
    assert tree.root.left.left is None

    tree.node_deletion(5)
    assert tree.root.value == 6
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7
