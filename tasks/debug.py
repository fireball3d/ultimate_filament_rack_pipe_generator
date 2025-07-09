from invoke import task


@task
def env(context):
    print("\n------------")
    print("Debugging Environment")
    print("------------\n")
    context.run("pwd && env | sort")
