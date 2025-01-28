#!/bin/zsh

# Check if python3 is installed
if ! command -v python3 &>/dev/null; then
  echo "Python3 is not installed. Would you like to install it? (y/n)"
  read -r install_python
  if [[ "$install_python" =~ ^[Yy]$ ]]; then
    # Arch Linux using yay (AUR helper) for Python installation
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
      if [[ -f /etc/arch-release ]]; then
        yay -S python3.13
        yay -S python-pip
      else
        echo "Non-Arch Linux system detected. Please install Python 3.13.1 or newer manually."
        exit 1
      fi
    else
      echo "Unsupported operating system. Please install Python 3.13.1 or newer manually."
      exit 1
    fi
  else
    echo "Python3 is required. Exiting."
    exit 1
  fi
fi

# Function to check Python version
check_python_version() {
    python_version=$(python3 --version 2>&1 | awk '{print $2}')
    required_version="3.13.1"
    if [[ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" == "$required_version" ]]; then
        return 0  # Python is up-to-date
    else
        return 1  # Python is not up-to-date
    fi
}

# Check if Python version is 3.13.1 or newer
if ! check_python_version; then
    echo "Python version is outdated. Please update to Python 3.13.1 or newer."
    exit 1
fi

# Check if pip3 is installed
if ! command -v pip3 &>/dev/null; then
  echo "pip3 is not installed. Would you like to install it? (y/n)"
  read -r install_pip
  if [[ "$install_pip" =~ ^[Yy]$ ]]; then
    # Install pip3 using yay for Arch
    yay -S python-pip
  else
    echo "pip3 is required. Exiting."
    exit 1
  fi
fi

echo "Creating a virtual environment..."
python3 -m venv pickle_venv

source pickle_venv/bin/activate

echo "Installing pygame 2.6.1..."
pip3 install pygame==2.6.1

# Temporary alias for running the game
alias pickle="python3 $(pwd)/main.py"
echo "Temporary alias 'pickle' set for this session."

# Add permanent alias for the user (in ~/.zshrc)
if ! grep -q "alias pickle" ~/.zshrc; then
    echo "Adding permanent alias 'rungame' to ~/.zshrc..."
    echo "alias pickle='python3 $(pwd)/main.py'" >> ~/.zshrc
    echo "Permanent alias 'pickle' added to ~/.zshrc."
fi

# Run the game
pickle

deactivate
