# **VM and Project Setup Guide - SP25_DS5111_zsf9pd**  

This repository contains scripts and setup instructions to quickly configure an AWS EC2 instance for data collection using a headless Chrome browser and Python virtual environment.

## **1. VM Bootstrap Setup**

### **Manual Steps (If Not Using Scripts)**
1. Update system packages:
   ```bash
   sudo apt update
   ```
2. Set up Git credentials and SSH key (see `scripts/00_01_setup_git_global_creds.sh`).
3. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd SP25_DS5111_zsf9pd
   ```

### **Automated Setup**
Run the initialization script to install essential tools:
```bash
./scripts/init.sh
```
This installs:
- `make` (for automation)
- `python3.12-venv` (for virtual environments)
- `tree` (for file visualization)

## **2. Project Setup**

### **Step 1: Install Headless Chrome**
Run:
```bash
./scripts/install_chrome_headless.sh
```
This will:
- Download and install **Google Chrome (headless mode)**
- Verify installation with `google-chrome --version`

### **Step 2: Set Up Python Virtual Environment**
Run:
```bash
make update
```
This will:
- Create a virtual environment (`env/`)
- Upgrade `pip`
- Install dependencies from `requirements.txt`:
  - `pandas`
  - `lxml`

### **Step 3: Test Headless Browser for Data Collection**
To extract stock gainers data, run:
```bash
make ygainers.csv
```
This will:
1. **Use Headless Chrome** to fetch stock data from Yahoo Finance.
2. **Parse the data** into a CSV file: `ygainers.csv`

Check that `ygainers.csv` exists:
```bash
ls -lh ygainers.csv
```

## **3. Project Structure**
Run the following command:
```bash
tree SP25_DS5111_zsf9pd -I env
```
Expected output:
```
SP25_DS5111_zsf9pd/
├── scripts/
│   ├── install_chrome_headless.sh
│   ├── init.sh
│   ├── 00_01_setup_git_global_creds.sh
├── Makefile
├── README.md
├── requirements.txt
```

## **4. Final Notes**
- **Ensure all scripts are executable**:
  ```bash
  chmod +x scripts/*.sh
  ```
- If changes are made, commit and push:
  ```bash
  git add .
  git commit -m "Updated setup scripts and documentation"
  git push origin main
  ```
- For troubleshooting, check logs or rerun scripts.

## **5. Summary of Key Commands**
| Action | Command |
|--------|---------|
| Clone repo | `git clone <repo-url>` |
| Run init script | `./scripts/init.sh` |
| Install Chrome | `./scripts/install_chrome_headless.sh` |
| Setup environment | `make update` |
| Fetch stock gainers data | `make ygainers.csv` |
| Check project structure | `tree -I env` |

This guide ensures a smooth setup process for your project. 🚀 Let me know if you need any refinements!
