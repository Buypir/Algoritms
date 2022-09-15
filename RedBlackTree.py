class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # новий вузол - червоний


class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fixInsert(node)

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def fixInsert(self, kid):
        while kid.parent.color == 1:
            if kid.parent == kid.parent.parent.right:
                uncle = kid.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    kid.parent.color = 0
                    kid.parent.parent.color = 1
                    kid = kid.parent.parent
                else:
                    if kid == kid.parent.left:
                        kid = kid.parent
                        self.rightRotate(kid)
                    kid.parent.color = 0
                    kid.parent.parent.color = 1
                    self.leftRotate(kid.parent.parent)
            else:
                uncle = kid.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    kid.parent.color = 0
                    kid.parent.parent.color = 1
                    kid = kid.parent.parent
                else:
                    if kid == kid.parent.right:
                        kid = kid.parent
                        self.leftRotate(kid)
                    kid.parent.color = 0
                    kid.parent.parent.color = 1
                    self.rightRotate(kid.parent.parent)
            if kid == self.root:
                break
        self.root.color = 0

    def swap(self, x, y):
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def deleteNodeHelper(self, node, key):
        l = self.NULL
        while node != self.NULL:
            if node.val == key:
                l = node
            if node.val <= key:
                node = node.right
            else:
                node = node.left
        if l == self.NULL:
            print("invalid value")
            return
        y = l
        y_original_color = y.color              
        if l.left == self.NULL:                 
            x = l.right                         
            self.swap(l, l.right)
        elif l.right == self.NULL:
            x = l.left
            self.swap(l, l.left)
        else:
            y = self.minimum(l.right)
            y_original_color = y.color
            x = y.right
            if y.parent == l:
                x.parent = y
            else:
                self.swap(y, y.right)
                y.right = l.right
                y.right.parent = y
            self.swap(y, y.right)
            y.left = l.left
            y.left.parent = y
            y.color = l.color
        if y_original_color == 0:
            self.fixDelete(x)

    def fixDelete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                brother = x.parent.right
                if brother.color == 1:
                    brother.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    brother = x.parent.right
                if brother.left.color == 0 and brother.right.color == 0:
                    brother.color = 1
                    x = x.parent
                else:
                    if brother.right.color == 0:
                        brother.left.color = 0
                        brother.color = 1
                        self.rightRotate(brother)
                        brother = x.parent.right
                    brother.color = x.parent.color
                    x.parent.color = 0
                    brother.right.color = 0
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                brother = x.parent.left
                if brother.color == 1:
                    brother.color = 0
                    x.parent.color = 1
                    self.rightRotate(x.parent)
                    brother = x.parent.left
                if brother.right.color == 0 and brother.left.color == 0:
                    brother.color = 1
                    x = x.parent
                else:
                    if brother.left.color == 0:
                        brother.right.color = 0
                        brother.color = 1
                        self.leftRotate(brother)
                        brother = x.parent.left

                    brother.color = x.parent.color
                    x.parent.color = 0
                    brother.left.color = 0
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 0

    def delete_node(self, key):
        self.deleteNodeHelper(self.root, key)

    def __printCall(self, node, indent, last):
        if node != self.NULL:
            print(indent, end=" ")
            if last:
                print("R----", end=" ")
                indent += "     "
            else:
                print("L----", end=" ")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.val) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    def print_tree(self):
        self.__printCall(self.root, "", True)


if __name__ == "__main__":
    rbt = RedBlackTree()

    rbt.insertNode(20)
    rbt.insertNode(40)
    rbt.insertNode(45)
    rbt.insertNode(50)
    rbt.insertNode(30)
    rbt.insertNode(25)
    rbt.insertNode(32)
    rbt.insertNode(34)
    rbt.insertNode(5)
    rbt.insertNode(4)
    rbt.insertNode(6)
    rbt.insertNode(2)
    rbt.insertNode(5)
    rbt.insertNode(10)
    rbt.print_tree()
    print("--------------------------------")
    rbt.delete_node(45)
    rbt.print_tree()
