# Non-Profit Events App

## Description

The Non-Profit Events App is a Django-based web application designed to help non-profit organizations manage and display their events. The app features a post board for announcements and a calendar to display events. Admins can add, edit, and delete events and posts.

## Features

- Post board for announcements
- Calendar view for events
- Modal pop-up with event details
- Admin interface for managing posts and events
- User authentication for admin access

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 4.x
- Git

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/eliaslichi96/Non-Profit-App.git
    cd Non-Profit-App
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```sh
    python manage.py runserver
    ```

7. **Access the application**:

    Open your browser and navigate to `http://127.0.0.1:8000`.

### Usage

1. **Admin Access**:
   - Log in as an admin to add, edit, or delete posts and events.
   - Navigate to `/admin` to access the Django admin interface.

2. **Adding Events**:
   - Admins can add events via the Django admin interface or using the front-end form.

3. **Viewing Events**:
   - Events are displayed on the home page in a calendar view. Clicking on an event opens a modal with the event details.

### Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [Django](https://www.djangoproject.com/)
- [FullCalendar](https://fullcalendar.io/)
- [Bootstrap](https://getbootstrap.com/)

