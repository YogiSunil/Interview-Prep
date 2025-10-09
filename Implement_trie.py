# . Implement Trie (Prefix Tree)
# Medium
# Topics
# premium lock icon
# Companies
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.



class TrieNode(object):
    def __init__(self):
        # Each node stores:
        # - children: mapping char -> next TrieNode
        # - is_end : True if some word ends at this node
        self.children = {}
        self.is_end = False


class Trie(object):
    def __init__(self):
        """
        Initialize the Trie with an empty root node.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts `word` into the trie.

        :type word: str
        :rtype: None
        Time:  O(L) where L = len(word)
        Space: O(L) in the worst case (all new nodes)
        """
        node = self.root                 # start from root
        for ch in word:                  # walk each character
            if ch not in node.children:  # if edge doesn't exist, create it
                node.children[ch] = TrieNode()
            node = node.children[ch]     # move to the child
        node.is_end = True               # mark the end of a full word

    def search(self, word):
        """
        Returns True iff `word` was inserted before (exact match).

        :type word: str
        :rtype: bool
        Time:  O(L)
        Space: O(1) extra
        """
        node = self.root
        for ch in word:                  # traverse down by characters
            if ch not in node.children:  # missing edge => word not present
                return False
            node = node.children[ch]
        return node.is_end               # only True if a word ends exactly here

    def startsWith(self, prefix):
        """
        Returns True if any inserted word starts with `prefix`.

        :type prefix: str
        :rtype: bool
        Time:  O(L)
        Space: O(1) extra
        """
        node = self.root
        for ch in prefix:                # traverse down by characters
            if ch not in node.children:  # if path breaks, no such prefix
                return False
            node = node.children[ch]
        return True                      # all prefix chars were found


#optional

class TrieNode26(object):
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

def idx(c): return ord(c) - ord('a')
