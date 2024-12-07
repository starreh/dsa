# Graph Traversal

class Graph:
    """
    Implementation of Graph traversal techniques
    """

    def depth_first_search(self, graph, root, visited):
        """
        Depth-First Search

        :param graph: Graph
        :param root: Node
        :param visited: set
        :return: None
        """

        if not root:
            return None

        if not visited:
            visited = set()

        visited.add(root)
        print(root.data)

        for neighbour in graph.get(root):
            if neighbour not in visited:
                self.depth_first_search(graph, neighbour, visited)

    def breadth_first_search(self, graph, root):
        """
        Breadth-First Search

        :param graph: Graph
        :param root: Node
        :return: None
        """

        if not root:
            return None

        visited = set()
        q = [root]

        while q:
            node = q.pop(0)

            if node not in visited:
                visited.add(node)
                print(node.data)

            for neighbour in graph.get(node):
                if neighbour not in visited:
                    q.append(neighbour)
