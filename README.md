# Insta-Mass-Reporter

A Python automation tool to report objectionable and illegal Instagram accounts using multiple users credentials stored in file.

## 📝 Description

This project allows you to mass-report accounts on Instagram for clickbaits or inappropriate content.  
It automates the login and reporting process for multiple accounts securely.

## ⚠ Warning: 
Only For Educational Purpose . Dont use illegally otherwise i am not responsible 🙂

## Technologies used:

- Python
- Selenium
- PyAutoGUI

## 🚀 Features

- **Automated Login:** Logs in using multiple Instagram accounts one by one from a file.  
- **Report Accounts:** Navigates to target accounts and submits reports automatically.  
- **Dynamic Handling:** Waits for elements to load dynamically, making it robust on slower networks.  

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.x installed on your system.  
- A Windows, Linux, or Mac machine.  
- Installed Google Chrome   
- Read the Instagram API/web automation rules to avoid account issues.  

## ⚙️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/Insta-Mass-Reporting.git
    cd Insta-Mass-Reporting
    ```

2. **Create and activate a virtual environment (recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS & Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Go to app.py file and enter the user id of target user in userReport variable and paste your accounts credentials file path inside defaultFile variable:**
   ```bash
    reportUser="silence10103"  # Target user(userid) , set it according to yourr target
   defaultFile="loginCredentials.txt"   #this is the file where login credentials are saved ,replace with your own file name🙈
  
    ```
## 🖥️ Usage

Run the bot with the target username or account list file:

```bash
# Example: specify target username
python main.py --userName target_username

# Example: use accounts list file
python main.py --file accounts.txt
