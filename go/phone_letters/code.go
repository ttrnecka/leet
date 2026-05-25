package phone_letters

import "fmt"

func letterCombinations(digits string) []string {
	digitMap := map[byte]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}
	results := []string{}

	for i := range digits {
		if i == 0 {
			results = append(results, "")
		}
		new_results := []string{}
		for _, r := range results {
			for _, letter := range digitMap[digits[i]] {
				new_results = append(new_results, fmt.Sprintf("%s%s", r, string(letter)))
			}
		}
		results = new_results
	}
	return results
}
