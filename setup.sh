# Setup Python Virtual Environment
echo -e
echo "INFO: Creating Python Virtual Environment"
python3.13 -m venv --upgrade-deps venv

echo -e
echo "INFO: Activating Python Virtual Environment"
source venv/bin/activate

echo -e
echo "INFO: Install UV"
pip install uv

# Setup Project
# uv init

echo -e
echo "INFO: Installing Libraries"
uv sync
