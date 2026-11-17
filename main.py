from time import sleep
from sense_emu import SenseHat
from display import show_locked, show_unlocked, show_error
from movement import  read_tilt, detect_position
from menu import MENU_OPTIONS, show_menu, move_selection

PASSWORD = ["forward", "left", "right", "backwards"]

def main():
	sense = SenseHat()

	is_locked = True
	password_index = 0
	ready_for_move = False
	menu_index = 0

	show_locked(sense)

	while True:
		for event in sense.stick.get_events():
			if event.action != "pressed":
				continue

			if is_locked:
				if event.direction == "middle":
					password_index = 0
					ready_for_move = False
					show_locked(sense)
					print("Reset")

			else:
				if event.direction in ("left", "right"):
					menu_index = move_selection(menu_index, event.direction)
					show_menu(sense, menu_index)

				elif event.direction == "middle":
					option = MENU_OPTIONS[menu_index]

					if option == "lock":
						is_locked = True
						password_index = 0 
						ready_for_move = False
						show_locked(sense)
						print("sejf zablokowsany")
					elif option == "change_password":
						print("tu bedzie zmiana hasla(kiedys)")


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
						sleep(3)

						sense.stick.get_events()
						menu_index = 0
						show_menu(sense, menu_index)

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

