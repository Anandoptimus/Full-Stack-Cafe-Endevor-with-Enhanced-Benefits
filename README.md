# Cafe Shop With Benefits

**Cafe Shop With Benefits** is a Flask web application that allows users to explore and manage information about cafes. Users can **sign up**, **log in**, view cafes, **add new cafes**, and **delete cafes**. The application is built using Flask, SQLAlchemy for database management, and incorporates user authentication for a personalized experience.

## Features

- **User Authentication:** Secure user authentication ensures that only registered users can access the application.

- **Cafe Management:** Users can view a list of cafes, **add new cafes**, and **delete cafes**. Deleted cafes are moved to a separate history table.

- **Responsive Design:** The application provides a responsive web interface, making it accessible across various devices.

## Tech Stack

- **Flask:** Web framework for building the application.
- **SQLAlchemy:** Database toolkit for managing the SQLite database.
- **Flask-Login:** User authentication and session management.
- **Werkzeug:** Security library for password hashing.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Anandoptimus/Full-Stack-Cafe-Endevor-with-Enhanced-Benefits.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Full-Stack-Cafe-Endevor-with-Enhanced-Benefits
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python main.py
    ```

5. **Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

## Screenshot

![image](https://github.com/Anandoptimus/Day88/assets/101982906/f3cc9b24-dbf0-44b8-b566-374499c8fff1)

![image](https://github.com/Anandoptimus/Day88/assets/101982906/ee8804ba-0e7e-4723-83a8-6b18da14673b)

![image](https://github.com/Anandoptimus/Day88/assets/101982906/491daf84-6e9a-4095-9b6a-205618878ccc)

![image](https://github.com/Anandoptimus/Day88/assets/101982906/ecc8cda9-2804-48c9-a709-d2b9412f8e7b)


## Usage

1. **Sign Up:** Create an account to access the full functionality.

2. **Log In:** If you already have an account, log in using your credentials.

3. **Explore Cafes:** View cafes, **add new cafes**, or **delete existing cafes**.

4. **Deleted History:** Explore the history of deleted cafes in the "Deleted History" section.

## Project Structure

- `main.py`: Main application file.
- `templates/`: HTML templates for rendering views.
- `static/`: Static files such as stylesheets and images.
- `models.py`: Database models for Cafe, Deleted History, and User.
- `requirements.txt`: List of project dependencies.

## Project link

**Open your browser and navigate to [https://anandoptimus.pythonanywhere.com/](https://anandoptimus.pythonanywhere.com/)**

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
