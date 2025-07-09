import math

import solid2

# Parameters
pipe_length = 120  # settable, 70–250 mm
pipe_diameter = 25.75  # across flats
thread_diameter = 20
thread_pitch = 2.5
thread_depth = 35  # mm

hex_radius = pipe_diameter / (2 * math.cos(math.pi / 6))


def hex_prism(h, r):
    return solid2.cylinder(h=h, r=r, _fn=6)


def modeled_thread(diameter, pitch, length, thread_height=1.2):
    # 60-degree triangle profile approximates ISO metric thread visually
    r = diameter / 2
    profile = [[r - thread_height / 2, 0], [r + thread_height / 2, pitch / 2], [r - thread_height / 2, pitch]]
    turns = length / pitch
    return solid2.linear_extrude(height=length, twist=turns * 360)(solid2.polygon(profile))


def threaded_hole_with_thread(diameter, depth, pitch):
    hole = solid2.cylinder(h=depth + 1, d=diameter + 0.4)
    thread = modeled_thread(diameter, pitch, depth + 1)
    return hole - thread  # Subtract thread for an internal (female) thread


def hex_pipe():
    body = hex_prism(pipe_length, hex_radius)
    thread_cut = threaded_hole_with_thread(thread_diameter, thread_depth, thread_pitch)
    thread1 = solid2.up(0)(thread_cut)
    thread2 = solid2.up(pipe_length - thread_depth)(thread_cut)
    return solid2.difference()(body, thread1, thread2)


if __name__ == "__main__":
    model = hex_pipe()
    model.save_as_scad("export/hex_pipe.scad")
