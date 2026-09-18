def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	# Your code here
	if z<0:
		return (alpha*z)
	else:
		return (z)
