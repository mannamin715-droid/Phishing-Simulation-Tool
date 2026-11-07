
# Phishing Simulation Tool

A cybersecurity awareness training project built with Python and Flask. This application simulates phishing emails in a safe, local environment and tracks user interactions through a dashboard.

## Project Overview

I developed this project to practice cybersecurity awareness, phishing detection, web application development, and event monitoring.

The application allows users to interact with a simulated phishing email, either by clicking a suspicious link or reporting the email. These actions are recorded in a local SQLite database.

## Features

- Simulated phishing email with suspicious login activity
- Verify Account and Report Phishing buttons
- Event tracking using SQLite
- Security awareness dashboard
- Total simulated email interactions
- Click and report statistics
- Phishing click-rate calculation
- Recent activity history with timestamps

## Technologies Used
## Project Screenshots

### 1. Initial Application
![Initial Application](screenshots/0%20intial%20application.png)

### 2. Phishing Email Simulation
![Phishing Email](screenshots/1.%20Phishing%20Email%20Simulation.png)

### 3. Phishing Reported
![Phishing Reported](screenshots/2.%20Phishing%20Reported.png)

### 4. Suspicious Link Detection
![Suspicious Link](screenshots/3.%20Suspicious-%20link.png)

### 5. Security Dashboard
![Dashboard](screenshots/4.%20Dashboard.png)

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Git and GitHub

## How It Works

1. Start the Flask application.
2. Open the local security awareness dashboard.
3. Click Start Simulation.
4. Review the simulated phishing email.
5. Select Verify Account or Report Phishing.
6. The application records the event in SQLite.
7. Return to the dashboard to review updated statistics and activity history.

## Installation

Clone the repository:

```bash
git clone https://github.com/mannamin715-droid/Phishing-Simulation-Tool.git
cd Phishing-Simulation-Tool
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

Open the application at:

http://127.0.0.1:5000/

## Project Screenshots

Screenshots of the dashboard, phishing email simulation, and recorded events are available in the `screenshots/` folder.

## Security and Ethical Use

This project is designed for educational purposes and authorized cybersecurity awareness training only. It uses a simulated email and local application environment. No real account credentials are required.

The local database, virtual environment, and environment files are excluded from GitHub using `.gitignore`.

## What I Learned

Through this project, I gained hands-on experience with:

- Building a Python Flask web application
- Recording and retrieving security events from SQLite
- Tracking phishing-related user interactions
- Creating a dashboard to display security statistics
- Debugging JavaScript and integrating frontend and backend functionality
- Using Git and GitHub to document cybersecurity projects

## Author

Mann Amin

Cybersecurity Student | Temple University

