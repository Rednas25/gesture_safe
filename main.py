from time import sleep
from sense_emu import SenseHat
from display import show_locked, show_unlocked, show_error
from movement import  read_tilt, detect_position

PASSWORD = ["forward", "left", "right", "backwards"]

def main():
	sense = SenseHat()

	is_locked = True
	password_index = 0
	ready_for_move = False

	show_locked(sense)

	while True:
		for event in sense.stick.get_events():
			if event.direction == "middle" and event.action == "pressed":
				is_locked = True
				password_index = 0
				ready_for_move = False
				show_locked(sense)
				print("Sejf zablokowany")

		pitch, roll = read_tilt(sense)
		position = detect_position(pitch, roll)

		if is_locked:
			if position == "neutral":
				ready_for_move = True

			elif position is not None and ready_for_move:
				ready_for_move = False

				if position == PASSWORD[password_index]:
					password_index += 1
					print(f"Poprawny ruch: {password_index}/{len(PASSWORD)}")

					if password_index == len(PASSWORD):
						is_locked = False
						show_unlocked(sense)
						print("sezamie otworz sie")

				else:
					password_index = 0
					print("zle i chuj")
					show_error(sense)
					sleep(2)
					show_locked(sense)
		sleep(0.1)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nPrzerwanie.")
