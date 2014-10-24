def calculate_volume( arr, debug = False):
	current_left_max = 0
	current_right_max = 0
	current_left_max_index = 0
	current_right_max_index = 0
	last_v = -1
	total_guaranted = 0
	total_sub = 0
	
	for i,v in enumerate(arr):
		str_ = "[{0}:{1}]".format(i,v)
		if v >= current_left_max:
			str_+=" higherThenLeftMax"
			if current_left_max is not -1:
				# add
				str_ += " adding: "+str( total_sub)
				total_guaranted += total_sub
				total_sub = 0
				current_right_max = -1
			current_left_max = v
			current_left_max_index = i
		elif( v >= current_right_max and v>last_v):
			str_+=" rising"
			current_right_max = v
			current_right_max_index = i
			total_sub += current_left_max - v
		else:
			str_+=" lower: "+str(current_left_max - v)
			total_sub += current_left_max - v
		last_v = v
		
		if(debug):
			print( str_)
		pass
	if current_right_max is not -1:
		delta_x = current_right_max_index - current_left_max_index -1
		delta_y = current_left_max - current_right_max
		total_sub -= current_left_max - current_right_max # subtract last column value
		# 
		if(debug):
			print("sub: " + str(total_sub))
			print( "minus: " + str(delta_x) + " x " + str(delta_y))
		total_guaranted += total_sub - (delta_x*delta_y )
	return total_guaranted

def debug_graph(arr):
	max_lvl = max(arr)
	for i in range(max_lvl):
		str_ = ""
		for v in arr:
			if v<=max_lvl-i-1:
				str_+="--"
			else:
				str_+="[]"
		print(str_)

def assert_( data, val, debug = False):
	vol = calculate_volume(data, debug)
	debug_graph(data)
	print( (val==vol and "OK " or "FAIL ") + str(data))
	
		
if __name__ == '__main__':
	assert_([2,5,1,3,1,2,1,7,7,6], 17)
	#assert_([2,5,1,2,3,4,7,7,6]
	assert_([2,5,1,3,1,2,1,5], 17)
	assert_([2,5,1,3,1,2,1,3], 7)
	assert_([2,5,1,3], 2)
	assert_([2,5,1,3,3], 2)
	assert_([0], 0)
	# other tests
	print ( "\nother tests:")
	assert_([ 2,5,1,2,3,4,7,7,6,3,5 ], 12)
	assert_([ 2,5,1,2,3,4,7,7,6 ], 10)
	assert_([1,0,1 ], 1)
	assert_([5,0,5], 5)
	assert_([0,1,0,1,0 ], 1)
	assert_([1,0,1,0 ], 1)
	assert_([1,0,1,2,0,2 ], 3)
	assert_([5,1,0,1 ], 1)
		
		
	print("\n###END")