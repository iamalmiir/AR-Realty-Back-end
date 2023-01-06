<a href="https://www.linkedin.com/in/almir-redzematovic-05b734201/" style="outline: none;"><img src="https://res.cloudinary.com/iamalmiir/image/upload/v1655748669/Linkedin-logo-png_ufs32u.png" alt="linkedin logo" style="float: left; margin-top: 10px;width: 180px;"/></a>
<br />
<br />

- Project Title: AR Realty App
- Language: Python
- Frameworks: Django, Resful Framework
- Database: PostgreSQL
- File storage: Cloudinary
- Deployment: Digital Ocean

## Description

As part of the [AR Realty](https://ar-realty.iamalmir.tech/) website, this is a back-end application that allows you to manage Django-powered website through web interface. You can achieve this by using the Django admin panel or sending HTTP requests to the API endpoints for specific actions. This app utilizes [Cloudinary](https://cloudinary.com/) to fast and efficiently store media files for listings, realtors, users, and all other media related to website.

## Screenshots

Admin Panel
<img src="https://res.cloudinary.com/iamalmiir/image/upload/v1669624330/django_admin_panel1_et7wom.png" alt="Admin Panel 1" />
<img src="https://res.cloudinary.com/iamalmiir/image/upload/v1669624442/django_admin_panel2_duuzsq.png" alt="Admin Panel 2" />

## Instalation

> Please make sure to create your own .env file with all necessary credentials before you continue. [^1] [^2]

[^1]: You can see `.env.example` file.
[^2]: _Following commands are for Unix-like operating systems_

Create virtual environment:

```bash
python -m venv ./venv
```

Activate virtual environment:

```bash
source ./venv/bin/activate
```

Install all requirements:

```bash
pip install -r requirements.txt
```

## Technologies used

- Django
  - Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.
    Built by experienced developers, Django takes care of much of the hassle of web development. I highly encourage
    you to read more [about Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction).
- Django REST framework

  - Lets you create RESTful APIs: A way to transfer information between an interface and a database in a simple way.
    DRF, as much as Django, makes everything simple and easier. Learn
    more [here](https://www.django-rest-framework.org/).

- PostgreSQL

  - PostgreSQL is a powerful, open source object-relational database system. It has more than 15 years of active development
    and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness.
    Learn more [here](https://www.postgresql.org/).

- Digital Ocean

  - DigitalOcean is a cloud platform that provides developers cloud services that help to deploy and scale applications
    that run simultaneously on multiple computers. Learn more [here](https://www.digitalocean.com/).

###

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=flat&logo=postgresql&logoColor=white) ![DigitalOcean](https://img.shields.io/badge/Digital_Ocean-0080FF?style=flat&logo=DigitalOcean&logoColor=white)

### Future development

- In the future I aim to implement
  - Functionality for managing rental listings.
  - Image optimization when uploading
  - More security measures
