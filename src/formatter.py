import math

# Fixed geometry parameters
pipe_diameter = 25.75  # across flats
thread_diameter = 20
thread_pitch = 2.5
thread_depth = 35

hex_radius = pipe_diameter / (2 * math.cos(math.pi / 6))


def write_customizer_scad(file="../exports/hex_pipe.scad"):
    # Customizer metadata and param declaration (pipe_length adjustable in MakerWorld)
    header = """// [metadata]
// Author = "Fireball 3D"
// Title = "Ultimate Filament Rack Hex Pipe Generator"
// Category = "Storage"

// [params]
// Enter Pipe Length in mm from 70mm to 250
Length = 120; // [70:1:250]

pipe_length = Length;
"""

    module_def = f"""
module hex_pipe_custom(pipe_length=120) {{
    // Pipe with hex profile and threaded holes at each end
    difference() {{
        cylinder(h=pipe_length, r={hex_radius}, $fn=6);
        translate([0,0,0])
            threaded_hole_with_thread({thread_diameter}, {thread_depth}, {thread_pitch});
        translate([0,0,pipe_length-{thread_depth}])
            threaded_hole_with_thread({thread_diameter}, {thread_depth}, {thread_pitch});
    }}
}}

module threaded_hole_with_thread(diameter, depth, pitch) {{
    difference() {{
        cylinder(h=depth+1, d=diameter+0.4);
        modeled_thread(diameter, pitch, depth+1);
    }}
}}

module modeled_thread(diameter, pitch, length) {{
    // Approximated 60-degree thread
    r = diameter / 2;
    thread_height = 1.2;
    profile = [
        [r - thread_height/2, 0],
        [r + thread_height/2, pitch/2],
        [r - thread_height/2, pitch]
    ];
    turns = length / pitch;
    linear_extrude(height=length, twist=turns*360)
        polygon(profile);
}}

// Main call for MakerWorld Customizer
hex_pipe_custom(pipe_length=pipe_length);
"""

    with open(file, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(module_def)


if __name__ == "__main__":
    write_customizer_scad("exports/hex_pipe_makerlab.scad")
    print("Customizer-ready SCAD generated: hex_pipe_makerlab.scad")
