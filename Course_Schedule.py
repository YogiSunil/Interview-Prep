# 207. Course Schedule
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.



from collections import deque, defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        LeetCode 207 — Course Schedule

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Idea (Kahn's Algorithm / BFS Topological Sort):
          - Model courses as nodes in a directed graph.
          - Edge: bi -> ai (to take ai you must first take bi).
          - Compute indegree[i] = number of prerequisites for course i.
          - Start with all nodes with indegree 0 (no prereqs) in a queue.
          - Repeatedly pop from queue, "take" the course, and reduce indegree of its neighbors.
          - Count how many courses we successfully take.
          - If we can take all courses → no cycle → return True; else False.

          Why this detects cycles:
            - Nodes involved in a cycle never drop to indegree 0, so the
              queue won't include them; the processed count will be < numCourses.

        Complexity:
          Time  : O(V + E)  (build graph + process each edge once)
          Space : O(V + E)  (adjacency list + indegree + queue)
        """

        # Build graph: adjacency list 'graph[u]' holds courses that depend on u
        graph = defaultdict(list)          # maps course -> list of next courses
        indegree = [0] * numCourses        # indegree[i] = number of prerequisites for course i

        # Fill graph and indegrees from prerequisites
        for a, b in prerequisites:         # for each constraint "take b before a"
            graph[b].append(a)             # add edge b -> a (a depends on b)
            indegree[a] += 1               # a has one more prerequisite

        # Initialize queue with all courses having no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        taken = 0                          # number of courses we can take in order
        while q:                           # process courses with no remaining prereqs
            u = q.popleft()                # "take" course u
            taken += 1

            # For each course v that depends on u, we can remove dependency on u
            for v in graph[u]:
                indegree[v] -= 1           # we've satisfied one prerequisite of v
                if indegree[v] == 0:       # if v now has no remaining prerequisites
                    q.append(v)            # it's ready to be taken next

        # If we've taken all courses, schedule is possible (no cycles)
        return taken == numCourses



#optional


from collections import defaultdict

class SolutionDFS(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = unvisited, 1 = visiting (in recursion stack), 2 = visited (done)
        state = [0] * numCourses

        def dfs(u):
            if state[u] == 1:    # back-edge → cycle
                return False
            if state[u] == 2:    # already checked
                return True

            state[u] = 1         # mark as visiting
            for v in graph[u]:
                if not dfs(v):
                    return False
            state[u] = 2         # mark as done
            return True

        for i in range(numCourses):
            if state[i] == 0 and not dfs(i):
                return False
        return True
