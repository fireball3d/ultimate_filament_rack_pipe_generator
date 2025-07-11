import subprocess
import tempfile

from invoke import task


# TODO: ? would need openscad setup in pipeline and it's blowing up on the build file
@task
def openscad_lint(context):
    """Run OpenSCAD Linter on Entire Repo"""
    print("\n------------")
    print("OpenSCAD Lint")
    print("------------\n")

    # def check_scad(file_path):
    #     try:
    #         subprocess.run(["openscad", "-o", "/dev/null", file_path], check=True)
    #         print("✅ No syntax errors in SCAD file.")
    #     except subprocess.CalledProcessError:
    #         print("❌ SCAD file contains syntax errors.")

    def check_openscad_syntax(file_path, timeout=10):
        with tempfile.NamedTemporaryFile(suffix=".stl", delete=True) as tmpfile:
            try:
                result = subprocess.run(
                    ["openscad", "-o", tmpfile.name, file_path],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                )
                if result.returncode == 0:
                    print("No syntax errors.")
                else:
                    print("Error output:")
                    print(result.stderr)
            except subprocess.TimeoutExpired:
                print(f"OpenSCAD check timed out after {timeout} seconds.")

    # context.run(check_openscad_syntax("builds/f3d_ufr_hex_pipe_generator_makerlab.scad"))
    context.run(check_openscad_syntax("builds/test.scad"))


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
