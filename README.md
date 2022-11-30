# Access to django admin panel
 - url: http://django-rezervacije.azurewebsites.net/admin/
 - username: tpo_root
 - password: tpo_root

# Access to api
  - base url: http://django-rezervacije.azurewebsites.net/api/


# API CALLS
 - POST /auth/register/ (username, password, email, first_name, last_name)
 - POST /auth/login/ (username, password)
 - POST /auth/token/refresh (refresh)