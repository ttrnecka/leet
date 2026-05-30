package substring_with_concatenation_of_all_words

func findSubstring(s string, words []string) []int {
	if len(s) == 0 || len(words) == 0 {
		return []int{}
	}

	word_freq := make(map[string]int)

	for _, word := range words {
		word_freq[word]++
	}

	word_len := len(words[0])
	window_len := word_len * len(words)
	result := []int{}

	for i := range len(s) - window_len + 1 {
		j := i
		tmp_freq := make(map[string]int)

		for j < i+window_len {
			tmp_word := s[j : j+word_len]
			_, ok := word_freq[tmp_word]
			if !ok {
				break
			}

			tmp_freq[tmp_word]++

			if word_freq[tmp_word] < tmp_freq[tmp_word] {
				break
			}
			j += word_len
		}
		if j == i+window_len {
			result = append(result, i)
		}
	}

	return result
}

func findSubstring2(s string, words []string) []int {
	ans := make([]int, 0)
	cnt := make(map[string]int)
	for _, curString := range words {
		cnt[curString]++
	}
	dif := len(cnt) // use len(cnt) to get the dif

	sz, totSz := len(words[0]), len(words[0])*len(words)
	for st := 0; st < sz; st++ {
		clear(cnt) // use clear to reset the map
		for _, curString := range words {
			cnt[curString]++
		}

		cntOk := 0
		for i := st; i+sz-1 < len(s); i += sz {
			if i >= totSz {
				cur := s[i-totSz : i-totSz+sz]
				if _, ok := cnt[cur]; ok {
					cnt[cur]++
					if cnt[cur] == 1 {
						cntOk--
					}
				}
			}
			cur := s[i : i+sz]
			if _, ok := cnt[cur]; ok {
				cnt[cur]--
				if cnt[cur] == 0 {
					cntOk++
				}
			}
			if cntOk == dif {
				ans = append(ans, i-totSz+sz)
			}
		}
	}
	return ans
}
