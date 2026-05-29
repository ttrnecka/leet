package dividetwointegers

import "math"

func divide(dividend int, divisor int) int {
	if dividend == math.MinInt32 && divisor == -1 {
		return math.MaxInt32
	}

	negative := (dividend < 0) != (divisor < 0)
	dividend = int(math.Abs(float64(dividend)))
	divisor = int(math.Abs(float64(divisor)))

	result := 0
	for dividend >= divisor {
		power := 1
		val := divisor
		for val+val <= dividend {
			val += val
			power += power
		}
		dividend -= val
		result += power
	}

	if negative {
		result = ^result + 1 // result = -result
	}

	if result > math.MaxInt32 {
		return math.MaxInt32
	}

	if result < math.MinInt32 {
		return math.MinInt32
	}

	return result

}
