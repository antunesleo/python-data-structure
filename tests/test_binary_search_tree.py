import unittest
from src.binary_search_tree import Node


class TestNodeCreateRoot(unittest.TestCase):

    def test_should_create_root_node_instance(self):
        node = Node.create_root(5)
        self.assertIsInstance(node, Node)

    def test_should_not_create_root_node_if_value_is_not_a_int_number(self):
        with self.assertRaises(ValueError):
            Node.create_root('asdf')

    def test_should_have_value(self):
        node = Node.create_root(5)
        self.assertEqual(5, node.value)


class TestNodeAdd(unittest.TestCase):

    def setUp(self):
        self.node = Node.create_root(5)

    def test_should_add_to_left_child_if_value_is_smaller_than_node_value_and_left_child_is_empty(self):
        self.node.add(4)
        self.assertIsInstance(self.node.left_child, Node)
        self.assertEqual(self.node.left_child.value, 4)

    def test_should_add_to_right_child_if_value_is_bigger_than_node_value_and_right_child_is_empty(self):
        self.node.add(8)
        self.assertIsInstance(self.node.right_child, Node)
        self.assertEqual(self.node.right_child.value, 8)

    def test_should_recursively_find_a_spot_if_value_is_smaller_than_node_and_left_child_is_not_empty(self):
        self.node.add(4)
        self.node.add(2)
        self.node.add(1)
        self.assertIsInstance(self.node.left_child, Node)
        self.assertEqual(self.node.left_child.value, 4)
        self.assertIsInstance(self.node.left_child.left_child, Node)
        self.assertEqual(self.node.left_child.left_child.value, 2)
        self.assertIsInstance(self.node.left_child.left_child.left_child, Node)
        self.assertEqual(self.node.left_child.left_child.left_child.value, 1)

    def test_should_recursively_find_a_spot_if_value_is_grather_than_node_and_right_child_is_not_empty(self):
        self.node.add(8)
        self.node.add(10)
        self.node.add(12)
        self.assertIsInstance(self.node.right_child, Node)
        self.assertEqual(self.node.right_child.value, 8)
        self.assertIsInstance(self.node.right_child.right_child, Node)
        self.assertEqual(self.node.right_child.right_child.value, 10)
        self.assertIsInstance(self.node.right_child.right_child.right_child, Node)
        self.assertEqual(self.node.right_child.right_child.right_child.value, 12)

    def test_should_recursively_find_a_spot_if_first_value_is_grather_second_is_grather_but_third_is_smaller(self):
        self.node.add(8)
        self.node.add(10)
        self.node.add(2)
        self.assertIsInstance(self.node.right_child, Node)
        self.assertEqual(self.node.right_child.value, 8)
        self.assertIsInstance(self.node.right_child.right_child, Node)
        self.assertEqual(self.node.right_child.right_child.value, 10)
        self.assertIsInstance(self.node.left_child, Node)
        self.assertEqual(self.node.left_child.value, 2)

    def test_should_return_error_if_value_equals_to_root_node_value(self):
        with self.assertRaises(ValueError):
            self.node.add(5)

    def test_should_return_error_if_value_equals_to_any_node_value(self):
        self.node.add(8)
        self.node.add(10)
        self.node.add(2)
        with self.assertRaises(ValueError):
            self.node.add(10)


class TestNodeSearch(unittest.TestCase):

    def test_should_return_node_if_root_node_value_is_equals_to_value(self):
        node = Node.create_root(5)
        found_node = node.search(5)
        self.assertEqual(node, found_node)

    def test_should_return_node_recursively(self):
        node = Node.create_root(5)
        node.add(3)
        node.add(2)
        node.add(6)
        node.add(4)
        found_node = node.search(2)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 2)

    def test_should_return_none_if_value_not_found(self):
        node = Node.create_root(5)
        node.add(3)
        node.add(2)
        node.add(6)
        node.add(4)
        found_node = node.search(12)
        self.assertIsNone(found_node)
