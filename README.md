# Basic-Django-Project

This is a Django project for managing a hotel website. It includes basic functionalities such as managing different pages like Home, About, Rooms, Create feedback, Gallery, Book, Sign-in and Sign-up.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (preferably Python 3.x)
- Django

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/1chrizty/basic-django-project.git
    ```

2. Navigate into the project directory:

    ```bash
    cd hotel-management
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash 
    python manage.py makemigratios
    ```

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to [http://localhost:8000](http://localhost:8000)

## Usage

- Home: Visit the home page to get an overview of the hotel.
- About: Learn more about the hotel and its reagarding datas.
- Rooms: Explore different types of rooms available in the hotel.
- Cerate feedback: For giving an suggestion about their overall performance and to contact them in case of emergency.
- Gallery: View images of the hotel's facilities and surroundings.
- Sign-in: Allowing access to old users.
- Sign-out: Helps to create an account for new users.

## Contributing

Contributions are welcome! If you'd like to add features or fix bugs, please fork the repository and submit a pull request.
