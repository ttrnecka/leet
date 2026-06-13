package weighted_word_mapping

func mapWordWeights(words []string, weights []int) string {

	new_word := make([]byte, 0, len(words))

	for _, word := range words {
		word_weight := 0
		for i := range word {
			word_weight += weights[word[i]-'a']
		}
		word_weight = word_weight % 26

		new_word = append(new_word, byte('z'-word_weight))
	}

	return string(new_word)
}
