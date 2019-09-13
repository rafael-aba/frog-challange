import random
import math

river_size = 4000
iterations = 100000

sum_jumps = 0
for x in xrange(0,iterations,1):
	total_distance = river_size
	current_distance = river_size
	total_jumps = 0


	while current_distance > 0:
		jump = random.randint(1,current_distance)
		total_jumps += 1
		current_distance = current_distance - jump
		if (current_distance == 0):
			sum_jumps += total_jumps

print 'simulation: ' + str(sum_jumps/float(iterations))


accumulated_probablities = [0.0] * river_size
for x in xrange(1,river_size+1,1):
	accumulated_probablities[x - 1] += 1/float(x)

print 'math: ' + str(sum(accumulated_probablities))	
