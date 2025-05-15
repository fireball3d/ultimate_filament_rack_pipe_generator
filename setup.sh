# Setup Python
echo -e
echo "INFO: Setup Python"
uv python install 3.13 --preview

# Setup Python Virtual Environment
echo -e
echo "INFO: Creating Python Virtual Environment"
uv venv
echo -e
echo "INFO: Activating Python Virtual Environment"
source .venv/bin/activate

# Download dependencies
echo -e
echo "INFO: Installing Libraries"
uv sync
