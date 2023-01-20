import rotatescreen
from time import sleep

rs = rotatescreen.get_primary_display()


def spin(times, t):
    orientations = (rs.set_landscape,rs.set_portrait_flipped,
    rs.set_landscape_flipped,rs.set_portrait,rs.set_landscape)
    sleeptime = t
    for i in range(times):
        for x in orientations:
            x()
            sleep(sleeptime)

spin(5, 0.3)