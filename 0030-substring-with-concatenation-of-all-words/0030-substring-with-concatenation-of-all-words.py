
class Solution:
    def findSubstring(self, s):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        freq = Counter(words)

        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0
            while j < word_count:
                word_start = i + j * word_len
                word = s[word_start: word_start + word_len]

                if word not in freq:
                    break

                seen[word] = seen.get(word, 0) + 1
                if seen[word] > freq[word]:
                    break

                j += 1
            
            if j == word_count:
                result.append(i)

        return result
