

class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
        if self.right == None:
            self.right = val[-1:int(len(val)/2)]
        if self.left == None:
            self.left = val[:int(len(val)/2)]
        



class Arvore:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
    
        def invert(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            invert(root.left)
            invert(root.right)

        invert(root)
        return root

class Vector:
    def __init__(self, lista):
        self.lista = lista
    def random_invert(self) -> list:
        
        return lista
v = Vector([0,1,2])
print(v.lista)
