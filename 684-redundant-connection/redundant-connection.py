class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        size = [1]*N
        rep = [i for i in range(N)]

        def find(node):
            if node == rep[node]:
                return node
            rep[node] = find(rep[node])
            return rep[node]

        def doUnion(node1, node2):
            node1, node2 = find(node1), find(node2)

            if node1 == node2:
                return False
            else:
                if size[node1] > size[node2]:
                    rep[node2] = rep[node1]
                    size[node1] += size[node2]
                else:
                    rep[node1] = rep[node2]
                    size[node2] += size[node1]
                return True

        for e in edges:
            node1 = e[0]-1
            node2 = e[1]-1

            if not doUnion(node1, node2):
                return e
            
        return []

        


                