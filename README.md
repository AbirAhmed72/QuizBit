# QuizBit - MCQ Practice Platform

**QuizBit** is a simplified MCQ practice platform built using Django. It allows users to register, log in, attempt questions, and track their practice history. The project demonstrates the core functionalities of a question-answering system with proper API design following RESTful principles.

---

## Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Setup Guide](#setup-guide)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
     - [Using PowerShell Command for Windows](#using-powershell-command-for-windows)  
     - [Using Shell Script for Linux](#using-shell-script-for-linux)  
     - [Traditional Way](#or-you-can-proceed-with-the-traditional-way)
4. [Using API Collection with Postman](#using-api-collection-with-postman)

---

## Features

- **User Authentication**: Register and log in using Django's built-in user management system.  
- **Question Bank**: Retrieve a list of questions and their answer choices.  
- **Question Details**: Retrieve all the details of a particular question and it's answer choices.  
- **Submit Answers**: Submit answers and get instant feedback on correctness.  
- **Practice History**: View the history of attempted questions and their results.  
- **API Documentation**: Interactive API testing using Swagger.

---

## Tech Stack

- **Backend**: Django 4.2, Django REST Framework  
- **Database**: SQLite (default, can be switched to PostgreSQL or MySQL)  
- **API Documentation**: Swagger (via `drf-yasg`)  
- **Environment Management**: Python `venv`

---

## Setup Guide

### Prerequisites

- Python 3.8+ installed  
- Git installed  
- Virtual environment tool (`venv`)  

---

### Installation

---

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/AbirAhmed72/QuizBit.git
   cd Quizbit
   ```

2. **Create a Virtual Environment**  
   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For macOS/Linux
   ```

---

#### **Using PowerShell Command for Windows**

1. **Make the Script Executable**:
    After cloning the repository, users need to allow script execution (if not already allowed):
   ```bash
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```

2. **Run the Script**:
   Users can then run the script using:
   ```bash
   .\setup.ps1
   ```

---

#### **Using Shell Script for Linux**

1. **Make the Script Executable**:
    After cloning the repository, users need to make the script executable by running:
   ```bash
   chmod +x setup.sh
   ```

2. **Run the Script**:
   Users can then run the script using:
   ```bash
   ./setup.sh
   ```

---

#### **What the Script Does**

1. **Installs Dependencies**:
   - Ensures all required Python packages from `requirements.txt` are installed.

2. **Applies Migrations**:
   - Ensures the database schema is up-to-date.

3. **Seeds the Database**:
   - Calls your custom `seed_data` management command to populate initial data.

4. **Starts the Development Server**:
   - Launches the Django server at `http://127.0.0.1:8000`.

---

#### **Or you can proceed with the traditional way**

1. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**  
   ```bash
   python manage.py migrate
   ```

3. **Seed the Database (Add Sample Data)**  
   ```bash
   python manage.py seed_data
   ```

4. **Start the Development Server**  
   ```bash
   python manage.py runserver
   ```

---

#### **Access the Application**  
   - API: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)  
   - Swagger Documentation: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  

---


## Using API Collection with Postman

1. **Download the Postman Collection**:  
   - The Postman collection file (`QuizBit.postman_collection.json`) is available in the root directory of the project.  

2. **Import the Collection**:  
   - Open Postman.  
   - Go to **File > Import** or click the **Import** button.  
   - Select the `QuizBit.postman_collection.json` file and click **Open**.  

3. **Set Headers for Authentication**:  
   - In Postman, press `Headers` tab then press `bulk edit`.  
   - Paste the following Header:
        ```
        Authorization:Token <your_token>
        Content-Type:application/json
        ```

4. **Test the APIs**:  
   - Use the `Register` endpoint to create a new user.  
   - Use the `Login` endpoint to log in and copy the returned token.  
   - Update the `your_token` variable in the header with the copied token.  
   - Now you can test the protected endpoints, like `Submit Answer`, `Practice History`, `Question Bank` and `Question Details`.  

---