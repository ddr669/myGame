class TreeNode:
    def __init__(self, root: list):
        self.root = root
        if self.is_odd(len(root)):
            half = int(len(root) / 2)
            self.left = root[:half]
            self.right = root[half:]
            
        else:
            print("impar")
    def is_odd(self, n)-> bool :
        x = 1 if n%2==0 else 0
        return x 
    

a = TreeNode([1,2,3,4])
