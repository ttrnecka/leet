package longestcommonprefix

import "strings"

func longestCommonPrefix(strs []string) string {
	var prefix strings.Builder
	i := 0
	for {
		var char byte
		if i < len(strs[0]) {
			char = strs[0][i]
		} else {
			return prefix.String()
		}
		for j := 1; j < len(strs); j++ {
			if i >= len(strs[j]) || strs[j][i] != char {
				return prefix.String()
			}
		}
		prefix.WriteByte(char)
		i++
	}
}
