package largestaltitude

func largestAltitude(gain []int) int {
	max := 0
	alt := 0
	for _, g := range gain {
		alt += g
		if alt > max {
			max = alt
		}
	}
	return max
}
