
import random
import matplotlib.pyplot as plt
import math
import time

pi = 3.14159265359
power = [2, 3, 4, 5, 6, 7, 8]
pis = []
errors = []
simulation_times = []

for k in power:
	print k
	NUMSIMULATIONS = 10 ** k

	in_circle_count = 0.0
	out_circle_count = 0.0

	for j in range(NUMSIMULATIONS):
		initial_time = time.time()
		x = random.uniform(-1, 1)
		y = random.uniform(-1, 1)
		r = math.sqrt(x**2 + y**2)
		if r <= 1:
			in_circle_count += 1.0
			plt.scatter(x, y, s = 0.01, c = 'r')
		else:
			out_circle_count += 1.0
			plt.scatter(x, y, s = 0.01, c = 'b')
		
	end_time = time.time()
	plt.xlim(-1, 1)
	plt.ylim(-1, 1)
	plt.gca().set_aspect('equal', adjustable='box')	
	plt.savefig("pi_estimation_power-" + str(k) + "png")
	plt.close("all")
	MC_pi = 4 * in_circle_count / (in_circle_count + out_circle_count)
	pis.append(MC_pi)
	simulation_times.append(end_time - initial_time)

plt.plot(power, pis)
plt.xlabel("Number of iterations(10^x)")
plt.ylabel("estimation of pi")
plt.savefig("Estimation_of_pi_wrt_num_iterations.png")

for j in pis:
	errors.append( math.abs((j - pi) / pi) )

plt.plot(power, errors)
plt.xlabel("Number of iterations(10^x)")
plt.ylabel("error")
plt.savefig("Estimation_of_pi_wrt_num_iterations_error.png")

f = open("pi.txt", "r")
for j in pis:
	f.write("%s\t" % j)
f.write("\n")
for j in errors:
	f.write("%s\t" % j)
f.write("\n")
for j in simulation_times:
	f.write("%s\t" % j)
f.close()