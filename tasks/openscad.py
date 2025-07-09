from invoke import task


@task
def create(context):
    print("\n------------")
    print("Create OpenSCAD File")
    print("------------\n")
    context.run("python src/generator.py")
