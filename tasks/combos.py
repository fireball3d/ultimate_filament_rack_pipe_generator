from invoke import task

from . import ruff, tests


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
