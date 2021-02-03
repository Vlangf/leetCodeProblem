# Trim a Binary Search Tree


def trimBST(root: TreeNode, low: int, high: int) -> TreeNode:
    def trim(node):
        if not node:
            return
        if node.val < low:
            return trim(node.right)
        elif node.val > high:
            return trim(node.left)
        else:
            node.left, node.right = trim(node.left), trim(node.right)
            return node

    return trim(root)
