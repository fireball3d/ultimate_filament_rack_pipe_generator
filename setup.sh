# Setup Python Virtual Environment
echo -e
echo "INFO: Creating Python Virtual Environment"
uv venv .venv --python 3.13
echo -e
echo "INFO: Activating Python Virtual Environment"
source .venv/bin/activate

# Download dependencies
echo -e
echo "INFO: Installing Libraries"
# uv pip install -e . # install deps in pyproject.toml
uv sync
