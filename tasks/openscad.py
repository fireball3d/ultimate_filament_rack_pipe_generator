# pylint: disable=W0622 # redefined-builtin

from invoke import task


@task
def create(context):
    """Create .scad File from Python Script"""
    print("\n------------")
    print("Create OpenSCAD File")
    print("------------\n")
    context.run("python -m src.generator")
