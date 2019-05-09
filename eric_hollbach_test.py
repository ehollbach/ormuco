from pymemcache.client.base import Client

class Line:
	def __init__(self, x1, x2):
		self.x1 = x1
		self.x2 = x2

def do_intersect( line1, line2 ):
	"""
	Returns True if the two line segments intersect and False otherwise.
	"""
	return min(line1.x2, line2.x2) > max(line1.x1, line2.x1)

def compare_versions( version1, version2 ):
	"""
	Compares the two version strings passed as input
	"""
	version1 = version1.rstrip(".")
	version2 = version2.rstrip(".")

	if version1 == version2:
		return 0
	elif version1 < version2:
		return -1
	else:
		return 1

def main():
	line1 = Line(1, 5)
	line2 = Line(2, 6)
	line3 = Line(6, 8)
	line4 = Line(7, 9)
	
	assert do_intersect(line1, line2) == True
	assert do_intersect(line1, line3) == False
	
	assert do_intersect(line2, line1) == True
	assert do_intersect(line3, line1) == False
	
	assert do_intersect(line3, line4) == True
	
	assert compare_versions("1.1", "1.2") == -1
	assert compare_versions("1.2.1", "1.2") == 1
	assert compare_versions("1.2.1", "1.2.1a") == -1
	assert compare_versions("1.2.1b", "1.2.1a") == 1
	assert compare_versions("1.2.1", "1.21") == -1
	assert compare_versions("2.1.1", "1.2.1") == 1
	assert compare_versions("1.2.1", "1.2.1") == 0
	assert compare_versions("1.", "1") == 0
	assert compare_versions("a1", "1a") == 1
	
	client = Client('127.0.0.1', 11211)
	client.set('some_key', 'some_value', expire = 30)
	assert client.get('some_key') == 'some_value'
	
	print("OK")
	
if __name__ == "__main__":
	main()
