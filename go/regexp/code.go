package regexp

func isMatch(s string, p string) bool {
	m, n := len(s), len(p)
	d := make([][]bool, m+1)
	for i := 0; i < len(d); i++ {
		d[i] = make([]bool, n+1)
	}

	d[0][0] = true

	// check for empty pattern
	for j := 2; j <= n; j++ {
		if p[j-1] == '*' {
			d[0][j] = d[0][j-2]
		}
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if p[j-1] == '*' {
				d[i][j] = d[i][j-2] || (d[i-1][j] && (s[i-1] == p[j-2] || p[j-2] == '.'))
			} else {
				d[i][j] = d[i-1][j-1] && (s[i-1] == p[j-1] || p[j-1] == '.')
			}
		}
	}

	return d[m][n]
}
