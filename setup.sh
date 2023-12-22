# install requirements.txt for project
# Usage: source setup.sh

# create virtual environment
python3 -m venv nlp_treo

# activate virtual environment
source ./nlp_treo/bin/activate

# Install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# INFO message
echo "Successfully installed requirements.txt"

# Deactivate virtual environment
deactivate
