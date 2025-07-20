# pylint: disable=W0622 # redefined-builtin

from invoke import task


@task
def upgrade(context):
    """Upgrade Project Libs"""
    print("\n------------")
    print("Upgrade Project Libs")
    print("------------\n")
    context.run("uv sync --upgrade")
