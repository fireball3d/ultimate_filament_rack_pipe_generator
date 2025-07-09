import subprocess


def check_scad(file_path):
    try:
        subprocess.run(["openscad", "-o", "/dev/null", file_path], check=True)
        print("✅ No syntax errors in SCAD file.")
    except subprocess.CalledProcessError:
        print("❌ SCAD file contains syntax errors.")


check_scad("hex_pipe.scad")
