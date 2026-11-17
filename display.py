RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

LOCKED_ICON = [
	"..####..",
	".#....#.",
	".#....#.",
	".######.",
	".##..##.",
	".###.##.",
	".###.##.",
	".######.",
]

UNLOCKED_ICON = [
        "..####..",
        ".#....#.",
        ".#......",
        ".######.",
        ".##..##.",
        ".###.##.",
        ".###.##.",
        ".######.",
]

ERROR_ICON = [
	"#......#",
	".#....#.",
	"..#..#..",
	"...##...",
	"...##...",
	"..#..#..",
	".#....#.",
	"#......#",
]

KEY_ICON = [
	"..###...",
	".#...#..",
	".#...#..",
	"..###...",
	"...#....",
	"...##...",
	"...#....",
	"...##...",
]

def show_icon(sense, icon, color): 
	pixels = [
		color if pixel == "#" else BLACK
		for row in icon 
		for pixel in row
	]
	sense.set_pixels(pixels)

def show_locked(sense):
	show_icon(sense, LOCKED_ICON, RED)

def show_unlocked(sense):
	show_icon(sense, UNLOCKED_ICON, GREEN)

def show_error(sense):
	show_icon(sense, ERROR_ICON, RED)

def show_key(sense):
	show_icon(sense, KEY_ICON, BLUE)

def show_lock_option(sense):
	show_icon(sense, LOCKED_ICON, YELLOW)

if __name__ == "__main__":
	from sense_emu import SenseHat
	from time import sleep

	sense = SenseHat()

	show_locked(sense)
	sleep(3)

	show_unlocked(sense)
	sleep(3)

	show_error(sense) 
	sleep(3)

	show_locked(sense)

