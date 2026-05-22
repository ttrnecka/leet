package palindrome_number

func isPalindrome(num int) bool {
	original := num
	reverse := 0
	for {
		if num <= 0 {
			break
		}
		reverse = 10*reverse + num%10
		num = num / 10
	}
	if reverse == original {
		return true
	}
	return false
}
