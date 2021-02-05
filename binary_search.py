class binary_search():
	def __init__ (self, item):
		list_range = list(range(1,51))
		self.item = item
		self.list_range = list_range
		
		
	def searching(self):

		min_loc = 0
		max_loc = len(self.list_range)-1
		
		while min_loc <= max_loc:
			mid = (max_loc + min_loc)/2
			guess = self.list_range[mid]				
			if guess == self.item:
				print(mid)
				return mid			
			elif guess < self.item:
				min_loc = mid+1
				
			else:
				max_loc = mid - 1
				
		return None

test = binary_search(3)

test.searching()
