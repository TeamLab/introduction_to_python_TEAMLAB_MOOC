def swap_value (x, y):
	temp = x
	x = y
	y = temp

def swap_offset(offset_x, offset_y):
	temp = a[offset_x]
	a[offset_x] = a[offset_y]
	a[offset_y] = temp

def swap_reference (list_ex, offset_x, offset_y):
	temp = list_ex[offset_x]
	list_ex[offset_x] = list_ex[offset_y]
	list_ex[offset_y] = temp
