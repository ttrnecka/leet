from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word,0)+1

        word_length = len(words[0])
        concat_length = word_length*len(words)

        results = []
        for i in range(len(s)-concat_length+1):
            j = i
            tmp_freq = {}
            while j < i + concat_length:
                tmp_word = s[j:j+word_length]
                if tmp_word not in word_freq:
                    break
                tmp_freq[tmp_word] = tmp_freq.get(tmp_word,0)+1

                if tmp_freq[tmp_word] > word_freq[tmp_word]:
                    break
                j+=word_length

            if j == i + concat_length:
                results.append(i)

        return results


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"])) # should print [0, 9]