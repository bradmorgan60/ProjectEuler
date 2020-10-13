import logging
logging.basicConfig(level=logging.DEBUG)

a = 1 
b = 2

nums = [1,2]

while nums[-1] < 4000000:
	nums.append(nums[-1] + nums[-2])

del nums[-1]
logging.debug(nums)

# find even numbers
evennums = []
for num in nums:
	if num % 2 == 0:
		evennums.append(num)
logging.debug(evennums)
print(sum(evennums))

	
