# 127. Word Ladder
# Hard
# Topics
# premium lock icon
# Companies
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        LeetCode 127 — Word Ladder (Bidirectional BFS)

        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        Goal:
          Return the number of words in the shortest transformation sequence
          from beginWord to endWord (inclusive). Return 0 if impossible.

        Idea (Bidirectional BFS):
          - BFS from both ends (beginWord and endWord) at the same time.
          - Always expand the *smaller* frontier to keep the branching factor low.
          - Generate neighbors by changing one character at each position (L positions, 26 letters).
          - Use a dictionary set for O(1) membership and a visited set to avoid repeats.
          - When the two frontiers meet, we've found the shortest path.

        Why bidirectional?
          - Plain BFS explores up to O(26^L) patterns per depth; two-way BFS
            drastically reduces the explored space by meeting in the middle.

        Complexity:
          Let N be the dictionary size and L the word length.
          Each expansion changes L positions × 26 letters; membership checks are O(1) via set.
          Time  : O(N · L · 26) in practice (often much faster than one-sided BFS).
          Space : O(N) for sets/queues.
        """

        # Convert the word list to a set for O(1) lookups
        dict_set = set(wordList)          # all allowed intermediate/end words

        # If endWord is not in dictionary, there's no valid sequence
        if endWord not in dict_set:
            return 0

        # If beginWord equals endWord (problem states they differ, but just in case)
        if beginWord == endWord:
            return 1

        # Two BFS frontiers: one from the start, one from the end
        front = {beginWord}               # current frontier from the beginning
        back  = {endWord}                 # current frontier from the end

        # Visited words so we don't revisit them (avoid cycles/duplicates)
        visited = set([beginWord, endWord])

        # Current length of path so far; starting word counts as 1
        length = 1

        # While there are nodes to expand from both sides
        while front and back:
            # Always expand the smaller frontier to reduce branching
            if len(front) > len(back):
                front, back = back, front  # swap

            # We'll build the next frontier here
            next_front = set()

            # Increment path length because we're moving one level deeper
            length += 1

            # For every word in the current smaller frontier
            for word in front:
                word_list = list(word)     # work with a list for character replacement

                # Try changing each position (0..L-1)
                for i in range(len(word_list)):
                    original_char = word_list[i]   # remember original char

                    # Try all 26 letters at this position
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original_char:
                            continue               # skip same letter; no change

                        word_list[i] = c          # mutate one character
                        nei = "".join(word_list)  # neighbor candidate

                        # If neighbor is in the opposite frontier, paths meet → found shortest
                        if nei in back:
                            return length         # meeting level yields total shortest length

                        # If neighbor is a valid word and not visited, add to next frontier
                        if nei in dict_set and nei not in visited:
                            visited.add(nei)
                            next_front.add(nei)

                    # Restore original character before moving to next position
                    word_list[i] = original_char

            # Move to next layer from the side we expanded
            front = next_front

        # If we exhausted both sides without meeting, no path exists
        return 0
