# Access to django admin panel
 - url: http://django-rezervacije.azurewebsites.net/admin/
 - username: tpo_root
 - password: tpo_root

# Access to api
  - base url: http://django-rezervacije.azurewebsites.net/api/


# API CALLS

'*' means optional

## FILTERING AND SEARCH
 - Search (url/?search=keywords)
 - Filter (url/?field_name=some_value)

## Auth
 - POST /auth/register/ ( 'username', 'password', 'email', 'first_name', 'last_name' )
 - POST /auth/token/ ( 'username', 'password' )
 - POST /auth/token/refresh ( 'refresh' )

## UserProfiles
 - GET /users/ ('id', 'username', 'full_name', 'email', 'is_company', 'bio', 'avatar')
 - GET /users/current/ ('id', 'username', 'full_name', 'email', 'phone', 'bio', 'location', 'birth_date', 'is_company', 'avatar')
 - GET /users/<user_id> ('id', 'username', 'full_name', 'email', 'phone', 'bio', 'location', 'birth_date', 'is_company', 'avatar')
 - PUT, PATCH /users/<user_id>/ ('phone', 'bio', 'location', 'birth_date')


## Management

### Location
 - GET /management/locations/ ( 'id', 'name', 'is_active', 'owner' )
 - GET /management/locations/<location_id> ( 'id', 'name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active')
 - POST, PUT, PATCH /management/locations/<location_id*>/ ( 'name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active' )

### Location Court
 - GET /management/locations/<location_id>/courts<court_id*>/ ( 'id', 'name', ['court_types'], 'location' )
 - POST, PUT, PATCH /management/locations/<location_id>/courts/<court_id*>/ ( 'name', ['court_types'] )

### Court types
 - GET /management/court-types/ ( 'id', 'name' )