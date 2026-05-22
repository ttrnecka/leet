package atoi

func myAtoi(s string) int {
	sign := 1
	var num int
	var i int
	l := len(s)

	for {
		if i < l && s[i] == ' ' {
			i++
		} else {
			break
		}
	}

	if i == l {
		return 0
	}

	if s[i] == '+' {
		i++
	} else if s[i] == '-' {
		i++
		sign = -1
	}

	for {
		if i < l && s[i] >= '0' && s[i] <= '9' {
			num = 10*num + int(s[i]-'0')
			if num > 2147483647 {
				break
			}
			i++
		} else {
			break
		}
	}
	if sign == -1 {
		num = -num
	}
	if num < -2147483648 {
		return -2147483648
	}
	if num > 2147483647 {
		return 2147483647
	}
	return num
}
