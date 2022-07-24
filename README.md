<a href="https://www.linkedin.com/in/almir-redzematovic-05b734201/" style="outline: none;"><img src="https://res.cloudinary.com/iamalmiir/image/upload/v1655748669/Linkedin-logo-png_ufs32u.png" alt="linkedin logo" style="float: left; margin-top: 10px;width: 180px;"/></a>
<br />
<br />

- Project Title: AR Realty App
- Language: Python
- Frameworks: Django, Resful Framework
- Database: PostgreSQL
- File storage: Cloudinary
- Deployment: Heroku

## Description

As part of the [AR Realty](https://ar-realty-client.vercel.app/) website, this is a front-end application that allows you to add and manage your realtor account's real estate properties. You can achieve this by using the Django admin panel or sending HTTP requests to the API endpoints for specific actions. This app utilizes [Cloudinary](https://cloudinary.com/) to fast and efficiently store media files for listings, realtors, users, and all other media related to your website.

## Instalation

> Please make sure to create your own .env file with all necessary credentials before you continue. [^1] [^2]

[^1]: You can see `.env.example` file.
[^2]: _Following commands are for macOS_

Create virtual environment: `python -m venv ./venv`

Activate virtual environment: `source ./venv/bin/activate`

Install all requirements: `pip install -r requirements.txt`

## Technologies used

- Django
  - Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development.
- Django REST framework

  - Lets you create RESTful APIs: A way to transfer information between an interface and a database in a simple way. DRF, as much as Django, makes everything simple and easier. Learn more [here](https://www.django-rest-framework.org/).

### Future development

- In the future I aim to implement
  - Functionality for managing rental listings.
  - Image optimization when uploading
  - More security measures
