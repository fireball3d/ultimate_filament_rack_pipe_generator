from invoke import Collection

from . import (
    combos,
    debug,
    openscad,
    ruff,
    tests,
    uv,
)

namespace = Collection()
namespace.configure({"auto_dash_names": False})

namespace.add_collection(debug, name="debug")
namespace.add_collection(openscad, name="openscad")
namespace.add_collection(ruff, name="ruff")
namespace.add_collection(tests, name="tests")
namespace.add_collection(uv, name="uv")

# Combo Tasks
namespace.add_task(combos.build, name="build")
namespace.add_task(combos.fix, name="fix")
namespace.add_task(combos.run, name="run")
namespace.add_task(combos.test, name="test")
namespace.add_task(combos.upgrade, name="upgrade")
