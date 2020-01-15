class Node(object):

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    @classmethod
    def create_root(cls, value):
        return cls.__create(value)

    @classmethod
    def create(cls, value):
        return cls.__create(value)

    @classmethod
    def __create(cls, value):
        if not isinstance(value, int):
            raise ValueError('value needs to be an integer')
        return cls(value)

    def add(self, value):
        if value < self.value:
            if self.left_child is None:
                self.left_child = self.__create(value)
            self.left_child.add(value)
        if value > self.value:
            if self.right_child is None:
                self.right_child = self.__create(value)
            self.right_child.add(value)
