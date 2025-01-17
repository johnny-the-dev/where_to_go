# Where to go

This is a Django project to show places on a map and provide descriptions.

## Features

* Show places on a map
* Provide descriptions for places
* Show photos of places

## Usage

1. Open a web browser and navigate to `https://johnnythedev.pythonanywhere.com/`
2. Click on a place on the map to show its description

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install the dependencies with `pip install -r requirements.txt`
4. Create a database and configure it in `settings.py`
5. Run `python manage.py migrate` to create the database tables
6. Run `python manage.py runserver` to start the server

### Loading Places
Optionally you can load places into the database using the console

- Run `python manage.py load_place <url_to_data_json>`

#### Example of a JSON file
```json
{
    "title": "Place name",
    "title_full": "Place full name (optional)",
    "imgs": [
        "https://image1.jpg",
        "https://image2.jpg",
        "https://image3.jpg",
    ],
    "description_short": "Short description of the place",
    "description_long": "<p>Use html tags to define the structure of your text</p><p>Long description of the place</p><address class=\"post-list-item-info\"><span class=\"address\"><i class=\"font-icon icon-location\"> my_address </i> </span></address>",
    "coordinates": {
        "lng": "38.68171061700625",
        "lat": "55.31744823804868"
    }
}
```

### Creating a Superuser

   - Open the command line terminal.
   - Navigate to the root directory of the project.
   - Run the command: `python manage.py createsuperuser`
   - Enter the username, email, and password as prompted.

## Moderator Documentation

As a moderator, you have the ability to add new places and images, as well as edit existing objects in the system. Follow the instructions below to perform these tasks:

### Adding Places and Images

1. **Log in to the Admin Panel:**
   - Navigate to the admin panel using the URL: `https://johnnythedev.pythonanywhere.com/admin`.
   - Use your assigned moderator credentials to log in.

   - ***Test credentials:*** username: `moderator`, password: `moderpass`

2. **Add a New Place:**
   - In the admin panel, click on "Локации" under the "Локации" section.
   - Click on the "Добавить локация" button in the top right corner.
   - Fill out the required fields such as `title`, `short description`, and `long description`.
   - Use the TinyMCE editor for formatting the long description, if needed.
   - Save the changes by clicking the "Сохранить" button.

3. **Add Images to a Place:**
   - Navigate to "Изображения" under the "Локации" section in the admin panel.
   - Click on the "Добавить изображение" button.
   - Select the place you want to associate the image with.
   - Upload the image file.
   - Arrange the order of images if necessary by setting the `number` field.
   - Save the changes by clicking the "Save" button.

### Editing Existing Objects

1. **Edit a Place:**
   - In the admin panel, go to "Локации".
   - Click on the place you want to edit from the list.
   - Make the necessary changes to the place's details.
   - Save the changes by clicking the "Сохранить" button.

2. **Edit Place Images:**
   - Navigate to "Изображения" in the admin panel.
   - Click on the image you want to edit.
   - Modify the image details or replace the image file as needed.
   - Save the changes by clicking the "Сохранить" button.
