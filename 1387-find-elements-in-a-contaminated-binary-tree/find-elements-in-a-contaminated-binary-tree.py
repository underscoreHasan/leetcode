# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        root.val = 0
        self.nodes.append(root)
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr and curr.left:
                curr.left.val = 2 * curr.val + 1
                self.nodes.append(curr.left)
                stack.append(curr.left)
            if curr and curr.right:
                curr.right.val = 2 * curr.val + 2
                self.nodes.append(curr.right)
                stack.append(curr.right)

    def find(self, target: int) -> bool:
        for i in self.nodes:
            if i.val == target:
                return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)