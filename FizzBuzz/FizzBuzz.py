
first = 1
last = 20
step = 1

rules = [{"divisor": 3, "message": "Fizz"}, {"divisor": 5, "message" :"Buzz"}]

def test(sample):
	output = ""
	for rule in rules:
		if (sample % rule["divisor"] == 0):
			output +=rule["message"]

	if (output == ""):
		output = repr(sample)

	return output

for i in range(0, last - (first / step)):
	value = i * step + first
	print test(value)
	
