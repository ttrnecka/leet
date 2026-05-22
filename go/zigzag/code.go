package zigzag

import (
	"strings"
)

func convert(s string, numRows int) string {

	i := 0
	n := len(s)
	columns := []string{}
	var str strings.Builder
	for i < n {
		if i+numRows < n {
			columns = append(columns, s[i:i+numRows])
		} else {
			columns = append(columns, s[i:])
		}
		moveCols := numRows - 2
		fill := numRows - 2
		shifted := 0
		for j := 0; j < moveCols && i+numRows+j < n; j++ {
			for z := 0; z < fill; z++ {
				str.WriteString(" ")
			}
			str.WriteByte(s[i+numRows+j])
			for _ = range numRows - fill - 1 {
				str.WriteString(" ")
			}
			columns = append(columns, str.String())
			fill--
			str.Reset()
			shifted++
		}
		i += numRows + shifted
	}

	for i := 0; i < numRows; i++ {
		for _, elm := range columns {
			if i < len(elm) && string(elm[i]) != " " {
				str.WriteByte(elm[i])
			}
		}
	}
	return str.String()
}
