from invoke import task

from . import openscad, ruff, tests


@task
def build(context):
    """Build SCAD Files"""
    openscad.create(context)
    openscad.format(context)


@task
def fix(context):
    """Run All Automated Fixes"""
    ruff.fix(context)
    ruff.format(context)


@task
def test(context):
    """Run All Tests"""
    tests.pylint(context)
    tests.ruff_lint(context)
    tests.openscad_lint(context)
