# Meal-Craft


Meal Craft is a web application that allows users to fetch and display Meals for a the given ingredients. The app utilizes the <a href="https://spoonacular.com/food-api">spoonacular API</a> to display the meals which can ve made with the given ingredients.

<!-- Check it out at <a href="https://vikranth3140.pythonanywhere.com/">vikranth3140.pythonanywhere.com</a> -->


## Features

- Enter the ingredients and get the meals that can be made.
- Randomised Meals can also be selected.


## File Structure
   <!-- Fix this -->
    userproject/
    │
    ├── home/                  # Home application directory
    │   ├── migrations/        # Database migrations for 'home' app
    │   │   ├── __init__.py
    │   │   └── admin.py
    │   │   └── apps.py
    │   │   └── forms.py
    │   │   └── models.py
    │   │   └── tests.py
    │   │   └── urls.py
    │   │   └── views.py
    │   │
    │   └── templates/         # HTML templates for 'home' app
    │       ├── about.html
    │       ├── background-img.png
    │       ├── index.html
    │       ├── ingredients.html
    │       ├── login.html
    │       ├── random-recipe.html
    │       ├── results.html
    │       ├── save_recipes.html
    │       ├── saved_recipes.html
    │       ├── search.html
    │       └── signin.html
    │
    ├── userproject/           # Main project folder
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── db.sqlite3             # SQLite database file
    ├── manage.py              # Django's command-line utility for administrative tasks
    ├── .gitignore             # Specifies intentionally untracked files to ignore
    ├── LICENSE                # License file for the project
    └── README.md              # Markdown file with project description


## Tech Stack

- HTML, CSS
- Django (Python)
- spoonacular API


## How to Use

1. **Installation:**
   - Clone the repository.

    ```bash
    git clone https://github.com/swara14/Meal-Craft.git
    ```

   - Install required dependencies

    ```bash
    pip install -r requirements.txt
    ```

2. **API Configuration:**
   - Obtain your API key from [SerpApi](https://spoonacular.com/).

   <!-- Fix this -->
   - Replace `SERPAPI_KEY` in `config.py` your actual key.

3. **Run the Application:**

   <!-- Fix this -->
   - Execute the Python app

    ```bash
    python run main.py
    ```

   - Enter the desired scholor's name.

4. **View Results:**
   - Open the app in your web browser.

        [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

   - The application will display real-time research paper information and the corresponding paper links.

## License

This project is licensed under the [MIT License](LICENSE).
