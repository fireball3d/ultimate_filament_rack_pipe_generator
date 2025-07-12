from invoke import task

from . import openscad, ruff, tests


@task
def build(context):
    """Build SCAD Files"""
    openscad.create(context)


@task
def fix(context):
    """Run All Automated Fixes"""
    ruff.fix(context)
    ruff.format(context)


@task
def run(context):
    """Run Project main.py"""
    print("\n------------")
    print("Running Project main.py")
    print("------------\n")
    context.run("python main.py")


@task
def test(context):
    """Run All Tests"""
    tests.pylint(context)
    tests.ruff_lint(context)
    tests.yaml_lint(context)
