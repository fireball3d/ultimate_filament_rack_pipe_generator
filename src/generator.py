import math

import solid2

# Parameters
pipe_length = 120  # set between 70 and 250 mm
pipe_diameter = 25.75  # across flat (AF) of hex
thread_diameter = 20
thread_pitch = 2.5
thread_depth = 35
segments = 100  # render quality

# Validation
assert 70 <= pipe_length <= 250, "pipe_length must be between 70 and 250 mm"

# Derived radius for hex (circumcircle radius)
hex_radius = pipe_diameter / (2 * math.cos(math.pi / 6))


def hex_cylinder(h, r, fn=6):
    return solid2.cylinder(h=h, r=r, fn=fn)


def simple_thread_profile(diameter, pitch):
    """Create a simplified triangular thread profile (not exact ISO)"""
    return solid2.polygon([[0, 0], [diameter / 2, 0], [diameter / 2, 0.5], [0, 1]])


def simple_thread(diameter, pitch, height):
    turns = math.ceil(height / pitch)
    profile = simple_thread_profile(diameter, pitch)
    return solid2.linear_extrude(height=height, twist=turns * 360, center=False)(profile)


def hex_pipe():
    # Main hex-shaped body
    body = solid2.cylinder(h=pipe_length, r=hex_radius, fn=6)

    # Threads at both ends
    thread = simple_thread(thread_diameter, thread_pitch, thread_depth)

    thread1 = solid2.up(0)(thread)
    thread2 = solid2.up(pipe_length - thread_depth)(thread)

    threaded_body = solid2.difference()(body, thread1, thread2)

    return threaded_body


if __name__ == "__main__":
    scad = hex_pipe()
    scad.save_as_scad("hex_pipe.scad", file_header=f"$fn = {segments};")
