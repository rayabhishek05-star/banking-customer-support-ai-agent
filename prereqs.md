# Prerequisites for Banking Customer Support AI Agent

**📧 Send this to learners BEFORE the session to ensure they're ready!**

## System Requirements

### For macOS Users
- **Operating System**: macOS 10.14 (Mojave) or later
- **Python**: Python 3.8 - 3.13 (recommended: Python 3.11 or 3.12)
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: At least 2GB free space
- **Internet**: Stable internet connection for OpenAI API calls

### For Windows Users
- **Operating System**: Windows 10 or Windows 11
- **Python**: Python 3.8 - 3.13 (recommended: Python 3.11 or 3.12)
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: At least 2GB free space
- **Internet**: Stable internet connection for OpenAI API calls

### For Linux Users
- **Operating System**: Ubuntu 18.04+ / CentOS 7+ / Debian 9+
- **Python**: Python 3.8 - 3.13 (recommended: Python 3.11 or 3.12)
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: At least 2GB free space
- **Internet**: Stable internet connection for OpenAI API calls

## Python Installation

### macOS
```bash
# Using Homebrew (recommended)
brew install python@3.11

# Or download from python.org
# Visit: https://www.python.org/downloads/macos/
```

### Windows
```bash
# Download from python.org (recommended)
# Visit: https://www.python.org/downloads/windows/
# Make sure to check "Add Python to PATH" during installation

# Or using winget
winget install Python.Python.3.11
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Linux (CentOS/RHEL)
```bash
sudo yum install python3 python3-pip
# or for newer versions: sudo dnf install python3 python3-pip
```

## Required Python Packages (Exact Versions)

The following packages will be automatically installed when you run `pip install -r requirements.txt`:

### Core Dependencies
- **streamlit>=2.14.0** - Web application framework
- **openai>=2.14.0** - OpenAI API client
- **python-dotenv==1.0.0** - Environment variable management
- **pandas** - Data manipulation and analysis

### Complete Package List
```
streamlit>=2.14.0
openai>=2.14.0
python-dotenv==1.0.0
pandas
```

## Git Installation

### Windows
- Download from [git-scm.com](https://git-scm.com/download/win)
- Install with default settings

### macOS
```bash
# Option 1: Download from git-scm.com
# Option 2: Install Xcode Command Line Tools
xcode-select --install
```

### Linux
```bash
# Ubuntu/Debian
sudo apt install git

# CentOS/RHEL
sudo yum install git
```

## OpenAI API Requirements

### API Key Setup
1. **Create OpenAI Account**: Visit [OpenAI Platform](https://platform.openai.com)
2. **Add Billing Information**: Required for API access
3. **Generate API Key**: Go to API Keys section
4. **Minimum Credit**: $5-10 recommended for testing

### API Usage Costs (Approximate)
- **GPT-3.5-Turbo**: ~$0.002 per 1K tokens
- **Typical Session**: $0.10 - $0.50 for extensive testing
- **Monthly Usage**: $5-20 for regular development work

## Pre-Installation Checklist

### Before Starting
- [ ] Python 3.8+ installed and accessible via command line
- [ ] pip package manager working
- [ ] Git installed (for cloning repository)
- [ ] OpenAI account created with billing enabled
- [ ] OpenAI API key generated and saved securely
- [ ] Stable internet connection
- [ ] Text editor (VS Code, Sublime Text, etc.)

## Verification Commands

### macOS/Linux
```bash
# Check Python version
python3 --version

# Check pip
pip3 --version

# Check Git
git --version
```

### Windows
```bash
# Check Python version
python --version

# Check pip
pip --version

# Check Git
git --version
```

## Common Installation Issues & Solutions

### macOS
- **Issue**: `command not found: python3`
- **Solution**: Install Python via Homebrew or python.org

- **Issue**: Permission denied during pip install
- **Solution**: Use virtual environment (recommended) or `pip3 install --user`

### Windows
- **Issue**: `'python' is not recognized`
- **Solution**: Add Python to PATH during installation or manually add to environment variables

- **Issue**: Long path names causing issues
- **Solution**: Enable long path support in Windows or use shorter directory names

### Both Platforms
- **Issue**: Package compilation errors
- **Solution**: Ensure you have the latest pip: `pip install --upgrade pip`

- **Issue**: OpenAI API errors
- **Solution**: Verify API key and billing setup

## Recommended Development Environment

### Code Editors
- **VS Code** (recommended) - Free, excellent Python support
- **PyCharm** - Professional Python IDE
- **Sublime Text** - Lightweight and fast
- **Vim/Nano** - For terminal-based editing

### Terminal/Command Line
- **macOS**: Terminal.app or iTerm2
- **Windows**: Command Prompt, PowerShell, or Windows Terminal
- **Linux**: Terminal (built-in)

## 🎯 What to Bring to the Session

1. **Your OpenAI API Key** (saved securely)
2. **Laptop** with all software installed
3. **Stable internet connection**
4. **Enthusiasm to learn!** 🚀

## Support & Troubleshooting

If you encounter issues:
1. Check the main README.md troubleshooting section
2. Verify all prerequisites are met
3. Ensure virtual environment is activated
4. Check OpenAI API key and billing status
5. Try reinstalling packages: `pip install -r requirements.txt --force-reinstall`

## 🎯 Session Day

On the day of the session, we'll:
1. Verify your setup quickly using `python verify_setup.py`
2. Clone the project repository
3. Set up the virtual environment
4. Configure your API key
5. Run the Banking Customer Support AI Agent!

**You're going to build an amazing multi-agent AI system! 🤖✨**

---
*Note: These requirements were tested and confirmed working as of December 2024. Using different versions may cause compatibility issues.*
