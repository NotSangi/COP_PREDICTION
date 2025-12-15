# 🪙 Colombian Currency Predictive Model

This project features a **predictive machine learning model** to forecast the value of a key Colombian currency rate (the COP/USD exchange rate or a similar economic indicator provided by the central bank). The model is trained using historical data from the **Banco de la República de Colombia** (Colombia's central bank) and is served via a lightweight **Flask** web application.

### 

---

### ✨ Features

* **Predictive Model:** Uses scikit-learn (**Random Forest Regressor**) to make predictions based on historical data.
* **Data Source:** Utilizes public datasets provided by the **Banco de la República** (Bank of the Republic) of Colombia.
* **Web API:** A lightweight RESTful API built with **Flask** to serve the model's predictions.
* **Data Preprocessing:** Handled by **Pandas** for cleaning, feature engineering, and preparing the data for the model.

### 🛠️ Technologies Used

This project is built with:

* **Python 3.13.5**
* **Flask** (for the web application/API)
* **scikit-learn (sklearn)** (for the machine learning model)
* **Pandas** (for data handling and manipulation)

### 🚀 Getting Started

Follow these steps to get a local copy up and running for testing.

#### Prerequisites

Make sure you have **Python 3.13.5** installed on your system.

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone "https://github.com/NotSangi/COP_PREDICTION.git"
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
#### Running the Application

Once the dependencies are installed, you can start the Flask application:

`python run.py`

### ⚙️ Usage
When the project is running, you will see this in the localhost:5000

<img width="1008" height="459" alt="image" src="https://github.com/user-attachments/assets/669ffcb0-ba40-4870-b011-b8bdc27d3d6a" />

All you have to do is select the date for which you want to predict the COP price. That's when the button **PREDICT** will be available.

It will throw somthing like this.

<img width="1094" height="460" alt="image" src="https://github.com/user-attachments/assets/7a35a1c2-9662-4f08-a2ae-9dbbd5e0f821" />

And that's basically it.

### Any recommendations will be gladly accepted to continue learning. 😁
