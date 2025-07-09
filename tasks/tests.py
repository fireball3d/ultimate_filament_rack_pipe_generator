import subprocess

from invoke import task


@task
def openscad_lint(context):
    """Run OpenSCAD Linter on Entire Repo"""
    print("\n------------")
    print("OpenSCAD Lint")
    print("------------\n")

    def check_scad(file_path):
        try:
            subprocess.run(["openscad", "-o", "/dev/null", file_path], check=True)
            print("✅ No syntax errors in SCAD file.")
        except subprocess.CalledProcessError:
            print("❌ SCAD file contains syntax errors.")

    context.run(check_scad("exports/f3d_ultimate_filament_rack_hex_pipe_generator.scad"))


@task
def pylint(context):
    """Run PyLint on Entire Repo"""
    print("\n------------")
    print("Pylint Lint")
    print("------------\n")
    context.run("pylint --verbose --rcfile=.pylintrc .")


@task
def ruff_lint(context):
    """Run Ruff Linter on Entire Repo"""
    print("\n------------")
    print("Ruff Lint")
    print("------------\n")
    context.run("ruff check .")


@task
def yaml_lint(context):
    """Run Yaml Linter on Entire Repo"""
    print("\n------------")
    print("Yaml Lint")
    print("------------\n")
    context.run(
        """
        yamllint --list-files -c .yamllint . &&
        echo '------------' &&
        echo -e &&
        yamllint -f parsable -c .yamllint .
        """
    )
