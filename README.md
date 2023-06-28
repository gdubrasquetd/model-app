# Machine Learning Model Execution Website

This is a basic website that allows you to execute machine learning models. It is built using Flask, Angular, Bootstrap, TinyDB, and other technologies.

## Demo

https://github.com/gdubrasquetd/model-app/assets/58482474/51568670-0aed-4902-a1a8-31d26f6e42c9

## Features

- Add examples to the database
- List the examples stored in the database
- Train the machine learning model
- Predict using the trained model

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (3.10.6)
- Node.js (20.3.0)
- Angular CLI (16.1.1)
- Flask (2.3.2)
- TinyDB (4.8.0)
- Bootstrap (optional, included in the project)

## Getting Started

Follow these steps to get the application up and running:

1. Clone the repository to your local machine.

2. Set up the Flask backend:
   - Navigate to the `backend` directory.
   - Install the required Python packages using the following command:
     ```
     pip install -r requirements.txt
     ```
   - Run the Flask application using the following command:
     ```
     python app.py
     ```

3. Set up the Angular frontend:
   - Navigate to the `frontend` directory.
   - Install the required Node.js packages using the following command:
     ```
     npm install
     ```
   - Build the Angular application using the following command:
     ```
     ng build
     ```
   - Serve the application using the following command:
     ```
     ng serve
     ```

4. Access the website:
   - Open your web browser and go to `http://localhost:4200`.
   - You should see the homepage of the application.

## Usage

1. **Add Examples**:
   - Click on the "Ajouter" page in the navigation bar.
   - Fill in the input fields with the desired values and click the "Ajouter le modèle" button.
   - The model will be added to the database.

2. **List models**:
   - Click on the "Lister" page in the navigation bar.
   - The page will display a list of all models stored in the database.

3. **Train the Model**:
   - Click on the "Train Model" button located on the "Lister" page.
   - This will initiate the training process for the machine learning model.
  
4. **Train the Model**:
   - Click on the "Train Model" button located on the "List Examples" page.
   - This will update the prediction field on your model.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
