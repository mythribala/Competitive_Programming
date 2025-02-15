'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Jist -> Given the Preorder and Inorder Traversal of a BinaryTree, we have to construct the BinaryTree

Important Observation : It is only possible to construct a unique BinaryTree when its Inorder traversal is given. i.e, Using only the 
Preorder and Postorder traversals, we cannot construct a unique BinaryTree
'''

#Topics invloved : Recursion, Hashing, Observation

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def construcTree(preStart, inStart, inEnd) :

            if (inStart > inEnd) :
                return None
            
            newNode = TreeNode(preorder[preStart])
            curInd = hash_map[preorder[preStart]]
            numLeftElem = curInd - inStart
            newNode.left = construcTree(preStart + 1, inStart, curInd - 1)
            newNode.right = construcTree(preStart + numLeftElem + 1, curInd + 1, inEnd)
            
            return newNode

        n = len(preorder)
        hash_map = {val : idx for idx, val in enumerate(inorder)}
        return construcTree(0, 0, n - 1)

#Problem Link : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#Submission Link : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1535695015/