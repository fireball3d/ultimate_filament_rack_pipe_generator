from invoke import Collection

from . import (
    combos,
    ruff,
    tests,
)

namespace = Collection()
namespace.configure({"auto_dash_names": False})

namespace.add_collection(ruff, name="ruff")
namespace.add_collection(tests, name="tests")

# Combo Tasks
namespace.add_task(combos.fix, name="fix")
namespace.add_task(combos.test, name="test")
