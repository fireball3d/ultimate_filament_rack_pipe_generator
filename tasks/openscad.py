# pylint: disable=W0622 # redefined-builtin

from invoke import task


@task
def create(context):
    print("\n------------")
    print("Create OpenSCAD File")
    print("------------\n")
    context.run("python src/generator.py")


@task
def format(context):  # noqa: A001
    print("\n------------")
    print("Format OpenSCAD File for Maker World")
    print("------------\n")
    context.run("python src/formatter.py")
