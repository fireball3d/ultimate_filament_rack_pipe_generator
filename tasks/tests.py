import subprocess

from invoke import task


@task
def openscad_lint(context):
    print("\n------------")
    print("OpenSCAD Lint")
    print("------------\n")

    def check_scad(file_path):
        try:
            subprocess.run(["openscad", "-o", "/dev/null", file_path], check=True)
            print("✅ No syntax errors in SCAD file.")
        except subprocess.CalledProcessError:
            print("❌ SCAD file contains syntax errors.")

    context.run(check_scad("export/hex_pipe.scad"))


@task
def pylint(context):
    print("\n------------")
    print("Pylint Lint")
    print("------------\n")
    context.run("pylint --verbose --rcfile=.pylintrc .")


@task
def ruff_lint(context):
    print("\n------------")
    print("Ruff Lint")
    print("------------\n")
    context.run("ruff check .")
