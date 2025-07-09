from invoke import task


@task
def pylint(context):
    print("\n------------")
    print("Pylint Lint")
    print("------------\n")
    context.run("pylint --verbose --rcfile=.pylintrc .")


@task
def rufflint(context):
    print("\n------------")
    print("Ruff Lint")
    print("------------\n")
    context.run("ruff check .")
