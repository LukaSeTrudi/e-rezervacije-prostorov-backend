# Tehnicne vescine 2.nal

# Cilj
Aplikacija je API za rezerviranje igrišč. Za večino API klicev je potrebna avtentikacija z pošiljanjem ACCESS TOKENA, ki je pridobljen z loginu. Ta containerizacija je mišljena samo za lokalni development.

Originalni cilj je bil narediti django rest api z postgres bazo, ker pa rabimo narediti 4 service sem se pa odločil še tudi dodati spletno stran, ki kliče ta api ter postgres admin aplikacijo, kjer lahko direktno upravljamo z bazo, čeprav to večinoma delamo v django admin panelu.

## Storitve

### API

API oziroma django rest api aplikacija, ki je dostopna na localhost:8000, njegove zmogljivosti so:
    - localhost:8000/api/{celotn api url} - izhodiščni API
    - localhost:8000/admin/ - admin plošča djangota, za dostop je potrebno prvo narediti superuserja z "docker exec -it reservation-api python manage.py createsuperuser"
    - localhost:8000/api/schema/swagger-ui/ - API shema

![django admin panel](images/api_1.png)
*Django admin plošča*

![Swagger api schema](images/api_2.png)
*Swagger api shema*

![django api](images/api_3.png)
*Django api*


#### Opis docker-compose
- container_name je reservation-api
- build se zgradi tako, da uporabi svoj Dockerfile v katerem vzame python alpine sliko, nastavi delovno okolje in posodobi/doda potrebne apk pakete, na koncu pa še doda potrebne python pakete iz requirements.txt 
- ports nastavi port 8000 -> 8000
- volumes nastavi trenutni direktorij v /usr/src/app/
- command prvo migrira vse potrebne migracije in nato zažene python strežnik
- env_file nastavi privzet .env file, kjer so nastavljene osnovne nastavitve in podatki za povezavo do postgres streznika
- depends_on db saj potrebuje bazo za pravilno delovanje