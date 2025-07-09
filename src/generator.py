import math

import solid2

# Parameters
pipe_length = 120  # settable, 70–250 mm
pipe_diameter = 25.75  # across flats
thread_diameter = 20
thread_pitch = 2.5
thread_depth = 35  # mm
hex_sides = 6

# Derived
hex_radius = pipe_diameter / (2 * math.cos(math.pi / 6))


def hex_prism(h, r):
    # Hexagon across-flats to circumcircle
    return solid2.cylinder(h=h, r=r, _fn=6)


def fake_thread(diameter, pitch, height):
    # Simplified visual thread: a helical cut using linear_extrude with twist
    turns = int(math.ceil(height / pitch))
    profile = solid2.polygon([[diameter / 2 - 0.4, 0], [diameter / 2, 0.5], [diameter / 2 - 0.4, 1], [0, 1], [0, 0]])
    return solid2.linear_extrude(height=height, twist=turns * 360)(profile)


def threaded_hole_with_thread(diameter, depth, pitch):
    # Union of a main hole and a thread groove
    hole = solid2.cylinder(h=depth + 1, d=diameter + 0.3)  # +0.3mm for clearance
    thread = fake_thread(diameter, pitch, depth + 1)
    return hole + thread


def hex_pipe():
    # The main solid hex bar
    body = hex_prism(pipe_length, hex_radius)
    # Threaded holes at each end
    thread_cut = threaded_hole_with_thread(thread_diameter, thread_depth, thread_pitch)
    thread1 = solid2.up(0)(thread_cut)
    thread2 = solid2.up(pipe_length - thread_depth)(thread_cut)
    # Subtract threaded holes from each end
    return solid2.difference()(body, thread1, thread2)


if __name__ == "__main__":
    model = hex_pipe()
    model.save_as_scad("export/hex_pipe.scad")
