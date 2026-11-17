from display import show_locked, show_key, show_lock_option

MENU_OPTIONS = ["lock", "change_password"] 

def show_menu(sense, menu_index):
	option = MENU_OPTIONS[menu_index]

	if option == "lock":
		show_lock_option(sense)
	elif option == "change_password":
		show_key(sense)

def move_selection(menu_index, direction):
	if direction == "right":
		return (menu_index + 1) % len(MENU_OPTIONS)
	if direction == "left":
		return (menu_index -1) % len(MENU_OPTIONS)

	return menu_index

if __name__ == "__main__":
	from sense_emu import SenseHat
	from time import sleep

	sense = SenseHat()
	menu_index = 0
	show_menu(sense, menu_index)

	try:
		while True:
			for event in sense.stick.get_events():
				if event.action != "pressed":
					continue
				if event.direction in ("left", "right"):
					menu_index = move_selection(menu_index, event.direction)
					show_menu(sense, menu_index)

				elif event.direction == "middle":
					print(f"Wybrano: {MENU_OPTIONS[menu_index]}")

			sleep(0.1)
	except KeyboardInterrupt:
		print("\nTest koniec")
