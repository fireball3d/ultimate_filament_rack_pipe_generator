from invoke import task

from . import openscad, ruff, tests, uv


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
    """Create OpenSCAD File"""
    print("\n------------")
    print("Create OpenSCAD File")
    print("------------\n")
    context.run("python -m src.generator")


@task
def test(context):
    """Run All Tests"""
    tests.actionlint(context)
    tests.pylint(context)
    tests.ruff_lint(context)
    tests.yaml_lint(context)


@task
def upgrade(context):
    """Upgrade Libs"""
    uv.upgrade(context)
