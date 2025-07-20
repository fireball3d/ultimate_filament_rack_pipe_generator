from invoke import task


@task
def actionlint(context):
    """Run Action Lint"""
    print("\n------------")
    print("Action Lint")
    print("------------\n")
    context.run("actionlint")


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
