'''
106. Construct Binary Tree from Postorder and Inorder Traversal

Jist -> Given the Postorder and Inorder Traversal of a BinaryTree, we have to construct the BinaryTree

Important Observation : It is only possible to construct a unique BinaryTree when its Inorder traversal is given. i.e, Using only the 
Preorder and Postorder traversals, we cannot construct a unique BinaryTree

It is similar to the Problem No : LC 105 (using Preorder and Inorder traversals)
'''

#Topics invloved : Recursion, Hashing, Observation

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def construcTree(postEnd, inStart, inEnd) :

            if (inStart > inEnd) :
                return None
            
            newNode = TreeNode(postorder[postEnd])
            curInd = hash_map[postorder[postEnd]]
            numRightElem = inEnd - curInd
            newNode.left = construcTree(postEnd - numRightElem - 1, inStart, curInd - 1)
            newNode.right = construcTree(postEnd - 1, curInd + 1, inEnd)
            
            return newNode

        n = len(inorder)
        hash_map = {val : idx for idx, val in enumerate(inorder)}
        return construcTree(n - 1, 0, n - 1)


#Problem Link : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#Submission Link : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/1535699642/
