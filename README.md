# Telegram Meeting Reminder Bot

This bot will check Discord voice channel presence and notify users on Telegram if they're late for the meeting.

## Prerequisites

1. **Python**: This bot is written in Python, so you will need to have Python installed.

## Installation Guide

### 1. Install Python

#### macOS:

1. Visit the official [Python downloads page](https://www.python.org/downloads/mac-osx/).
2. Download the latest version for macOS.
3. Follow the installation instructions.
4. Confirm the installation by opening a terminal and typing:

   ```bash
   python3 --version
   ```

#### Linux:

Most Linux distributions come with Python pre-installed. To check, open a terminal and type:

```bash
python3 --version
```

If it's not installed, use your package manager to install it. For example, on Ubuntu:

```bash
sudo apt update
sudo apt install python3
```

### 2. Clone the repository

If you have git installed, you can clone the repository:

```bash
git clone [URL_OF_YOUR_REPOSITORY]
```

Replace `[URL_OF_YOUR_REPOSITORY]` with the actual URL of your git repository.

### 3. Set up a virtual environment (optional but recommended)

Navigate to the bot's directory:

```bash
cd path/to/directory
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **macOS & Linux**:

  ```bash
  source venv/bin/activate
  ```

### 4. Install the required packages:

```bash
pip install -r requirements.txt
```

### 5. Run the bot

```bash
python main.py
```

Replace `main.py` with the actual name of your bot script.

---

## Usage

Once the bot is running, you can use it as described in the previous sections, such as checking who's late with the `/check_meeting <meeting_id>` command.