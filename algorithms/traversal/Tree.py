# Tree Traversal

class Tree:
    """
    Implementation of Tree traversal techniques
    """

    # Depth First Search

    def pre_order(self, root):
        """
        Pre-Order Traversal

        :param root: Node
        :return: None
        """
        if root:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        """
        In-Order Traversal

        :param root: Node
        :return: None
        """
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)
    
    def post_order(self, root):
        """
        Post-Order Traversal

        :param root: Node
        :return: None
        """
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)
    
    # Breadth First Search

    def bfs(self, root):
        """
        Breadth First Search

        :param root: Node
        :return: None
        """
        if root:
            q = [root]
            
            while q:
                curr = q.pop(0)
                print(curr.data)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)