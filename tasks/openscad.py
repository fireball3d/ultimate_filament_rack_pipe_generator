# pylint: disable=W0622 # redefined-builtin

from invoke import task


@task
def create(context):
    """Create .scad File from Python Script"""
    print("\n------------")
    print("Create OpenSCAD File")
    print("------------\n")
    context.run("python src/generator.py")


@task
def format(context):  # noqa: A001
    """Create .scad File for MakerLabs from Standard .scad Creation"""
    print("\n------------")
    print("Format OpenSCAD File for Maker World")
    print("------------\n")
    context.run("python src/formatter.py")
