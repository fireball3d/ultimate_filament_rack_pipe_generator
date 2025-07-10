import math

# --- Your parameter setup ---
pipe_diameter = 22.5  # across flats
thread_diameter = 20
thread_pitch = 2.5
thread_depth = 35
hex_radius = pipe_diameter / (2 * math.cos(math.pi / 6))
output_file = "builds/f3d_ufr_hex_pipe_generator_makerlab.scad"


def write_customizer_scad(threads_scad_path, out_filename):
    # Read in all of threads.scad
    with open(threads_scad_path, encoding="utf-8") as f:
        threads_code = f.read()

    header = """// [metadata]
// title = "Hex Pipe With True Metric Threads"
// author = "Your Name"
// description = "Parametric hex pipe with real ISO metric internal threads for Bambu Lab MakerWorld Customizer."
// category = "Tools"
// [params]
pipe_length = 120; // [70:1:250]

"""
    # Your hex pipe module, using metric_thread as defined above
    module_def = f"""
module hex_pipe_custom(pipe_length=120) {{
    difference() {{
        // Hexagonal outer body
        cylinder(h=pipe_length, r={hex_radius}, $fn=6);
        // Internal thread at one end
        translate([0,0,0])
            metric_thread(diameter={thread_diameter}, pitch={thread_pitch}, length={thread_depth}, internal=true);
        // Internal thread at other end
        translate([0,0,pipe_length-{thread_depth}])
            metric_thread(diameter={thread_diameter}, pitch={thread_pitch}, length={thread_depth}, internal=true);
    }}
}}

// Main call for MakerWorld Customizer
hex_pipe_custom(pipe_length=pipe_length);
"""
    # Write it all to one SCAD file
    with open(out_filename, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n// ---- Start threads.scad ----\n")
        f.write(threads_code)
        f.write("\n// ---- End threads.scad ----\n")
        f.write(module_def)


if __name__ == "__main__":
    write_customizer_scad("lib/threads.scad", output_file)
    print(f"Output File: {output_file}")
