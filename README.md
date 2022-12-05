# Access to django admin panel
 - url: https://lp0667.pythonanywhere.com/admin/
 - username: tpo_root
 - password: tpo_root

# Access to api
  - base url: https://lp0667.pythonanywhere.com/api/


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
 - GET /users/ ('id', 'username', 'full_name', 'email', 'is_company', 'bio', 'avatar', 'created_at', 'updated_at')
 - GET /users/current/ ('id', 'username', 'full_name', 'email', 'phone', 'bio', 'location', 'birth_date', 'is_company', 'avatar', 'created_at', 'updated_at')
 - GET /users/<user_id> ('id', 'username', 'full_name', 'email', 'phone', 'bio', 'location', 'birth_date', 'is_company', 'avatar', 'created_at', 'updated_at')
 - PUT, PATCH /users/<user_id>/ ('phone', 'bio', 'location', 'birth_date')


## Management

### Location
 - GET /management/locations/ ( 'id', 'name', 'is_active', 'owner', 'created_at', 'updated_at' )
 - GET /management/locations/<location_id> ( 'id', 'name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active', 'created_at', 'updated_at')
 - POST, PUT, PATCH /management/locations/<location_id*>/ ( 'name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active' )

### Court types
 - GET /management/court-types/ ( 'id', 'name' )

### Location Court
 - GET /management/locations/<location_id>/courts/<court_id*> ( 'id', 'name', ['court_types'], 'location' )
 - POST, PUT, PATCH /management/locations/<location_id>/courts/<court_id*>/ ( 'name', ['court_types'] )

### Schedules
 - GET /management/locations/<location_id>/courts/<court_id>/schedules/<schedule_id*> ( 'id', 'court', 'day', 'day_formatted', 'start_time', 'end_time', 'price', 'is_active', 'created_at', 'updated_at' )
 - POST, PUT, PATCH /management/locations/<location_id>/courts/<court_id>/schedules/<schedule_id*>/ ( 'day', 'start_time', 'end_time', 'price', 'is_active')

> NOTES: day represents day in the week from 1(Monday) to 7(Sunday)

### Reservations
 - GET /management/locations/<location_id>/courts/<court_id>/schedules/<schedule_id>/reservations/<reservation_id*> ( 'id', 'schedule', 'user', 'date', 'confirmed', 'created_at', 'updated_at' )
