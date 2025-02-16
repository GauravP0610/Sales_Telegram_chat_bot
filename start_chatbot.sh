#!/bin/bash
chmod +x "$0"
# Set project and virtual environment paths
PROJECT_DIR="$HOME/telegram-chatbot"
VENV_DIR="$PROJECT_DIR/chatvenv"

# Update system packages
echo "Updating system packages..."
sudo apt update && sudo apt install -y python3 python3-venv python3-pip tmux git

# Navigate to the project directory
cd "$PROJECT_DIR" || exit

# Fetch the latest code from GitHub
echo "Fetching latest code from GitHub..."
git reset --hard origin/main  # Reset any uncommitted changes
git pull origin main

# Stash any local changes (optional)
echo "Stashing local changes (if any)..."
git stash


chmod +x "$PROJECT_DIR/start_chatbot.sh"

# Remove existing virtual environment if it exists
if [ -d "$VENV_DIR" ]; then
    echo "Removing existing virtual environment..."
    rm -rf "$VENV_DIR"
fi

# Create a new virtual environment
echo "Creating new virtual environment..."
python3 -m venv "$VENV_DIR"

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r "$PROJECT_DIR/requirements.txt" --break-system-packages
else
    echo "requirements.txt not found, skipping package installation."
fi


# Check if tmux session already exists
tmux has-session -t chatrepo_session 2>/dev/null

if [ $? -eq 0 ]; then
    echo "Tmux session 'chatrepo_session' already exists. Attaching..."
    tmux attach -t chatrepo_session
    exit 0
fi

# Start a new tmux session
tmux new-session -d -s chatrepo_session

# Run the first script (f_run_bot.py) in the first pane
tmux send-keys -t chatrepo_session "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && python3 f_run_bot.py" C-m

# Split the window and run the second script (f_run_loops.py)
tmux split-window -v -t chatrepo_session "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && python3 f_run_loops.py"

# Arrange panes neatly
tmux select-layout tiled

# Attach to the tmux session
tmux attach -t chatrepo_session

echo "Setup completed successfully!"