# ValueVerse


![Python](https://img.shields.io/badge/Python-3.0-blue) 
![Flask](https://img.shields.io/badge/Flask-2.3.2-lightgrey) 
![HTML](https://img.shields.io/badge/HTML-5-orange) 
![CSS](https://img.shields.io/badge/CSS-3-blue) 
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow) 
![License](https://img.shields.io/badge/License-MIT-green)

## 📝 Description
**ValueVerse** is a simple web application designed to simplify stock valuation using three well-known financial models: **Discounted Cash Flow (DCF)**, **Dividend Discount Model (DDM)**, and a **Warren Buffett-inspired formula**. This tool allows users to input company-specific data and receive calculated stock values based on their chosen model. 

This project was primarily developed to deepen my knowledge of HTML, CSS and JavaScript, and have a little fun trying to build a functional and visually appealing web interface, rather than providing sophisticated financial valuation models. 

---

## 📚 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🛠️ Installation

To run ValueVerse locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/adourian/ValueVerse.git
    cd ValueVerse
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```bash
    export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
    flask run --port=5001
    ```

4. **Open the app in your browser:**
    - Ctrl+Click the link provided in the terminal (usually `http://127.0.0.1:5001`).

---

## 🚀 Usage

### 1. **Home Page**

![Home Page Screenshot](https://github.com/adourian/ValueVerse/blob/main/images/Homepage.PNG)

- Home page with navigation bar.

### 2. **Models Page**

![Models Page Screenshot](https://github.com/adourian/ValueVerse/blob/main/images/ModelSelection.PNG)

- Displays selection of models to pick from.

### 3. **Model Selection and Calculation**

![Calculation Screenshot](https://github.com/adourian/ValueVerse/blob/main/images/ValueCalculation.PNG)

- Input your company data into the calculator widget.
- Hit "Calculate" and see the stock value displayed dynamically without page reload.

---

## 🌟 Features

- **Interactive Calculations:** Perform sensitivity analysis by adjusting inputs and instantly seeing the results.
- **Sticky Navigation Bar:** Easily access different pages as you explore the app.
- **Model Explanations:** Understand when and why to use each model, complete with risks and limitations.

---

## 🧰 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Deployment:** TBC (working on it)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 📫 Contact

- **Email:** kariad@seas.upenn.edu
- **LinkedIn:** [Kari Adourian](https://www.linkedin.com/in/kariadourian/)

