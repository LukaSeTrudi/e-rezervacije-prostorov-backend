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

## Locations
 - GET /locations/ ( 'id', 'name' )
 - GET /locations/<location_id> ( 'id', 'name', 'latitude', 'longitude', 'website_url', 'phone_number', 'email', 'owner', 'created_at', 'updated_at')

> GET filters - 'owner'
> GET search - 'name'

## Courts
 - GET /courts/<court_type*> ('id', 'name', 'location', ['court_types'], 'created_at', 'updated_at', 'is_outside')

> GET filters - 'location', '[court_types]'
> GET search - 'name'

## Schedules
Gives you schedule for current week
 - GET /schedules/
 - Filters:
  - date (YY-MM-DD defaults to current date if not given)
  - location (int)
  - court (int)
  - day (1-7) - only gives schedules for that day
  - month (bool, if given, gives you schedule for 6 weeks)
  - if day or month are not given it defaults to current week schedule
 - returns ( 'id', 'court', 'title', 'date','reservation_taken', 'start_datetime', 'end_datetime', 'day', 'day_formatted', 'start_time', 'end_time', 'price', 'created_at', 'updated_at' )


## Management

### Location
 - GET /management/locations/ ( 'id', 'name', 'is_active', 'owner', 'created_at', 'updated_at' )
 - GET /management/locations/<location_id> ( 'id', 'name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active', 'created_at', 'updated_at')
 - POST, PUT, PATCH /management/locations/<location_id*>/ ( 'name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active' )

### Court types
 - GET /management/court-types/ ( 'id', 'name' )

### Location Court
 - GET /management/locations/<location_id>/courts/<court_id*> ( 'id', 'name', ['court_types'], 'location', 'is_outside', 'is_active' )
 - POST, PUT, PATCH /management/locations/<location_id>/courts/<court_id*>/ ( 'name', ['court_types'], 'is_outside', 'is_active' )

### Schedules
 - GET /management/locations/<location_id>/courts/<court_id>/schedules/<schedule_id*> ( 'id', 'court', 'day', 'day_formatted', 'start_time', 'end_time', 'price', 'is_active', 'created_at', 'updated_at' )
 - POST, PUT, PATCH /management/locations/<location_id>/courts/<court_id>/schedules/<schedule_id*>/ ( 'day', 'start_time', 'end_time', 'price', 'is_active')

> NOTES: day represents day in the week from 1(Monday) to 7(Sunday)

### Analytics
 - GET /management/analytics/
 - Only for companies, gives you some analytics
 - Params are type, location, court, user
 - types are (user_shown, user_detail, location_shown, location_detail, court_shown, court_detail)
 - location, court, user are ids for filtering

 - shown means everytime they are queried in a list
 - detail means everytime they are queried by an id

 - returns ('id', 'user', 'log_type', 'created_at', 'location', 'court', 'user_profile')

### Reservations
 - GET /management/locations/<location_id>/courts/<court_id>/schedules/<schedule_id>/reservations/<reservation_id*> ( 'id', 'schedule', 'user', 'date', 'confirmed', 'created_at', 'updated_at' )
