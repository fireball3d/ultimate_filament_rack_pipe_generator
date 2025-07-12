import math

# --- Your parameter setup ---
pipe_diameter = 22.5  # across flats
thread_diameter = 20
thread_pitch = 2.5
thread_depth = 35
hex_radius = pipe_diameter / (2 * math.cos(math.pi / 6))
output_file = "builds/f3d_ufr_hex_pipe_generator_makerlab.scad"

# Calculate cone (drill tip) depth for 118° included angle
drill_tip_angle_deg = 118
drill_tip_half_angle_deg = drill_tip_angle_deg / 2
drill_tip_depth = (thread_diameter / 2) / math.tan(math.radians(drill_tip_half_angle_deg))


def write_customizer_scad(threads_scad_path, out_filename):
    with open(threads_scad_path, encoding="utf-8") as f:
        threads_code = f.read()

    header = """// [metadata]
// title = "Hex Pipe With True Metric Threads and Tapered Drill Tip"
// author = "Fireball 3D"
// description = "Hex pipe with real ISO metric threads and a 118-degree tapered hole bottom for MakerWorld Customizer."
// category = "Tools"
// [params]
pipe_length = 120; // [70:1:250]

"""

    module_def = f"""
module hex_pipe_custom(pipe_length=120) {{
    difference() {{
        // Outer hex body
        cylinder(h=pipe_length, r={hex_radius}, $fn=6);

        // Thread at near end
        translate([0,0,0])
            metric_thread(diameter={thread_diameter}, pitch={thread_pitch}, length={thread_depth}, internal=true);
        // Tapered cone at one end (matches drill tip)
        translate([0,0,{thread_depth + drill_tip_depth}])
            rotate([0,180,0])
                cylinder(h={drill_tip_depth}, r1=0, r2={thread_diameter / 2}, center=false);

        // Internal thread at other end
        translate([0,0,pipe_length-{thread_depth}])
            metric_thread(diameter={thread_diameter}, pitch={thread_pitch}, length={thread_depth}, internal=true);
        // Tapered cone at other end
        translate([0,0,pipe_length-{thread_depth + drill_tip_depth}])
            cylinder(h={drill_tip_depth}, r1=0, r2={thread_diameter / 2}, center=false);
    }}
}}

// Main call for MakerWorld Customizer
hex_pipe_custom(pipe_length=pipe_length);
"""

    with open(out_filename, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n// ---- Start threads.scad ----\n")
        f.write(threads_code)
        f.write("\n// ---- End threads.scad ----\n")
        f.write(module_def)


if __name__ == "__main__":
    write_customizer_scad("assets/threads.scad", output_file)
    print(f"Output File: {output_file}")
