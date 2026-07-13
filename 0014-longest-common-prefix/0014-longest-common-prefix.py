class Solution:
    def longestCommonPrefix(self, strs):
        
        # If the list is empty
        if not strs:
            return ""
        
        prefix = ""
        first = strs[0]  # Take the first word
        
        # Check each character of the first word
        for i in range(len(first)):
            
            ch = first[i]
            
            # Compare with all other words
            for word in strs[1:]:
                
                # If the word is shorter
                # or the character doesn't match
                if i >= len(word) or word[i] != ch:
                    return prefix
            
            # If all words have the same character
            prefix += ch
        
        return prefix
        