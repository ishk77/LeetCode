# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left, right):
            if left > right:
                return None
            
            middle = (lefts + right) // 2

            node = TreeNode(nums[middle])
            
            node.left = buildBST(left, middle - 1)
            
            node.right = buildBST(middle + 1, right)
            
            return node
        
        return buildBST(0, len(nums) - 1)