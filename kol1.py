#damianswist

import random
import sys


class Plane(object):
	def __init__(self):
		pass

	# returns current orientation
	def get_current_orientation(self):
		current_orientation = random.randint(0,360)
		return current_orientation

	def correct_orientation(self, current_orientation, max_correction_step):
		new_orientation = 0

		if 180 - max_correction_step < current_orientation < 180 + max_correction_step:
			new_orientation = 180
		elif current_orientation > 180:
			new_orientation = current_orientation - max_correction_step
		elif current_orientation < 180:
			new_orientation = current_orientation + max_correction_step
		return new_orientation


class Simulation(object):

	def start_simulation(self, max_correction_step, plane):
		while True:
			current_orientation = plane.get_current_orientation()
			corrected_orientation = plane.correct_orientation(current_orientation, max_correction_step)
			print ("Current orientation {0}: ".format(current_orientation))
			print ("Corrected orientation {0}: ".format(corrected_orientation))
			print ()

if __name__=="__main__":
	plane = Plane()
	simulation = Simulation()

	max_correction_step = int(sys.argv[1])
	simulation.start_simulation(max_correction_step, plane)