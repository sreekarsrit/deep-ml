def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	dim_a=len(a);dim_b=len(b)
	if dim_a==dim_b:
		c=[]
		for i in range(dim_a):
			c.append(b[i]+a[i])
		return c
	else:
		return -1
	pass