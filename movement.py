TILT_THRESHOLD = 30
NEUTRAL_THRESHOLD = 10

def normalize_angle(angle):
	return (angle+180) % 360 - 180

def read_tilt(sense):
	orientation = sense.get_orientation()

	pitch = normalize_angle(orientation["pitch"])
	roll = normalize_angle(orientation["roll"])

	return pitch, roll

def detect_position(pitch, roll):
	if abs(pitch) <= NEUTRAL_THRESHOLD and abs(roll) <= NEUTRAL_THRESHOLD:
		return "neutral"

	if abs(roll) <= NEUTRAL_THRESHOLD:
		if pitch >= TILT_THRESHOLD:
			return "forward"
		if pitch <= -TILT_THRESHOLD:
			return "backwards"

	if abs (pitch) <= NEUTRAL_THRESHOLD:
		if roll >= TILT_THRESHOLD:
			return "right"
		if roll <= -TILT_THRESHOLD:
			return "left"
	return None

if __name__ == "__main__":
	from sense_emu import SenseHat
	from time import sleep

	sense = SenseHat()
	previous_position = None

	try:
		while True:
			pitch, roll = read_tilt(sense)
			position = detect_position(pitch, roll)

			if position != previous_position:
				if position is not None:
					print(position)

				previous_position = position

			sleep(0.1)

	except  KeyboardInterrupt:
		print("\nTest zakonczony.")
