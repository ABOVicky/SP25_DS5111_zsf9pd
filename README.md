![Workflow Status](https://github.com/ABOVicky/SP25_DS5111_zsf9pd/actions/workflows/validations.yml/badge.svg)

# **VM and Project Setup Guide - SP25_DS5111_zsf9pd**  

This repository contains scripts and setup instructions to quickly configure an AWS EC2 instance for data collection using a headless Chrome browser and Python virtual environment.

## **1. Clone Repository and Set Up Credentials**

1. Clone Repository:

   ```bash
   git clone https://github.com/ABOVicky/SP25_DS5111_zsf9pd.git
   ```
   
   ```bash
   cd SP25_DS5111_zsf9pd
   ```
   
2. Set up Git Credentials and SSH Key (see `scripts/00_01_setup_git_global_creds.sh`).

## **2. VM Bootstrap Setup**

### **Manual Steps (If Not Using Scripts)**
Update System Packages:

```bash
# To bring VM snapshot up to date with package versions
sudo apt update
```

```bash
# To use makefiles
sudo apt install make -y
```

```bash
# To create python virtual environments
sudo apt install python3.12-venv -y
```

```bash
# To list files in tree form
sudo apt install tree
```

### **Automated Setup**
Run Initialization Script (All Manual Steps):

```bash
./scripts/init.sh
```

## **3. Project Setup**

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
ls
```

## **4. Project Structure**
Run Following Command:

```bash
tree -I env
```

Expected Output (Based on File Structure):

```
.
├── LICENSE
├── README.md
├── google-chrome-stable_current_amd64.deb
├── makefile
├── requirements.txt
├── sample_data
│   └── ygainers.csv
├── scripts
│   ├── 00_01_setup_git_global_creds.sh
│   ├── init.sh
│   └── install_chrome_headless.sh
└── ygainers.html
```

## **5. Final Notes**
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

This guide ensures a smooth setup process for your project.
