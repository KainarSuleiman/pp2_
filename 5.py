# class Food:
#     def __init__(self, name, ex_date, manufac):
#         self.name = name
#         self.expiration_date = ex_date
#         self.manufac = manufac
#
#     def hp(self):
#         print(self.name, "from", self.manufac, "healed me by 0 hp")
#
#
# obj = Food('Burger', 'Today', 'Bahandi')
# obj.hp()
#
#
# class Soup(Food):
#     def __init__(self, name, ex_date, manufac, concentration):
#         super().__init__( name, ex_date, manufac)
#         self.concentration = concentration
#
#     def hp_soup(self):
#         print(self.name, "from", self.manufac, "thick", self.concentration, "healed me by 50 hp")
#
# obj = Soup('lentil', 'yesterday', 'restaraunt', 'thick')
# obj.hp_soup()
#
# class Salad(Food):
#     def __init__(self, name, ex_date, manufac, type):
#         super().__init__(name, ex_date, manufac)
#         self.type = type
#
#
# class Main(Food):
#     def __init__(self, name, ex_date, manufac, quaility):
#         super().__init__(name, ex_date, manufac)
#         self.quality = quaility
#
#
# class Dessert(Food):
#     def __init__(self, name, ex_date, manufac, type):
#         super().__init__(name, ex_date, manufac)
#         self.type = type



class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LCA( root = TreeNode, p= TreeNode, q= TreeNode ):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val> root.val:
            root = root.right
        else:
            return root
    return 0

root = TreeNode(5)
root.left = TreeNode(2, TreeNode(1), TreeNode(4))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

p= root.left.left
q= root.right.right

lca= LCA(root, p, q)
print(lca.val)








class TreeNode:
    def __init__(self, 