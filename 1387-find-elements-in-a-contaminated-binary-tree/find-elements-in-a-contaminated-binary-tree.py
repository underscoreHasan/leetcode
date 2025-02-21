# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.valSet = set()

        root.val = 0
        self.nodes.append(root)
        self.valSet.add(root.val)

        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr:
                left = curr.left
                right = curr.right
                if left:
                    left.val = 2 * curr.val + 1
                    self.nodes.append(left)
                    stack.append(left)
                    self.valSet.add(left.val)
                if right:
                    right.val = 2 * curr.val + 2
                    self.nodes.append(right)
                    stack.append(right)
                    self.valSet.add(right.val)


    def find(self, target: int) -> bool:
        return target in self.valSet
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)