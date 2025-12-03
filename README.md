# AI Sales Email Project

This project uses SendGrid to send emails via Python.

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows PowerShell (if you get execution policy error, see Troubleshooting below):**
```bash
venv\Scripts\activate
```

**Windows Command Prompt (Recommended if PowerShell has issues):**
```bash
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with your SendGrid API key:
```
SENDGRID_API_KEY=your_api_key_here
```

### 5. Run the Email Script
```bash
python send_email.py
```

## Project Structure
- `send_email.py` - Main script to send emails via SendGrid
- `.env` - Environment variables (API keys)
- `requirements.txt` - Python dependencies
- `venv/` - Virtual environment (not tracked in git)

## Troubleshooting

### PowerShell Execution Policy Error
If you get an error like "running scripts is disabled on this system" when activating the virtual environment in PowerShell:

**Option 1: Use Command Prompt instead**
```bash
cmd
venv\Scripts\activate.bat
python send_email.py
```

**Option 2: Change PowerShell execution policy (requires admin)**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Option 3: Run directly without activating**
```bash
venv\Scripts\python.exe send_email.py
```

### SendGrid 401 Unauthorized Error
If you get a 401 error, your API key might be invalid or expired:
1. Log in to [SendGrid](https://app.sendgrid.com/)
2. Go to Settings → API Keys
3. Create a new API key with "Mail Send" permissions
4. Update your `.env` file with the new key

## Security Note
⚠️ Never commit your `.env` file or API keys to version control!
