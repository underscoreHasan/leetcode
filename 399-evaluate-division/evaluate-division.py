class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)

        for (numerator, denom), quotient in zip(equations, values):
            graph[numerator].append((denom, quotient))
            graph[denom].append((numerator, 1 / quotient))

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    product = dfs(neighbor, target, visited)
                    if product != -1.0:
                        return weight*product

            return -1.0

        # 3. Process each query
        results = []
        for start, target in queries:
            # If either variable hasn't been seen before, it's invalid
            if start not in graph or target not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(start, target, set()))
                
        return results