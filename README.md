# mozio_challenge
## django API rest project ##
**Web service project to manage providers and their corresponding service areas.**

### Requirements
1. Docker
1. docker-compose

### Used tools
1. Django
1. Postgres / postgis
2. nginx

### Deployment

1. Build images - `docker-compose build --no-cache`
1. Start services - `docker-compose up -d`	
1. Navigate in browser http://127.0.0.1:1337/

### Links

 - http://server:1337/ -> swagger doc.
 - http://server:1337/admin/ -- admin panel 
 - http://server:1337/api/v1/ -- API and API documentation

### Demo (links)

 - http://54.146.203.58:1337/ -> swagger doc.
 - http://54.146.203.58:1337/admin/ -- admin panel { user: 'app', pass: 'adminpass'}
 - http://54.146.203.58:1337/api/v1/ -- API and API documentation

## API ##
## Endpoints ###
- Get all providers -> `GET /api/v1/providers/`
- Create new provider `POST /api/v1/providers/`
- Get all services-areas `GET /api/v1/service-areas/` 
- Get services-areas filtered `GET /api/v1/service-areas/?poly__contains={"type":"Point","coordinates":[9.26436996459961,10.564178042345375]}`
- Get all services areas filtered by providerID `GET /api/v1/service-areas/?provider_id=1` 
- Create new service provider area `POST /api/v1/service-areas/` 
### Payloads
- Provider  `{"name": "required", "email": "", "phone": null, "language": null, "currency": ""}`
- Service-areas `{"name": "required", "provider_id": "required", "price": "required", "poly": "required; GeoJson Polygon"}`
- GeoJson Polygon `{"type":"Point","coordinates":[9.26436996459961,10.564178042345375]}`
- GeoJson Polygon `{"type":"Polygon","coordinates":[[[6.15234375,10.9423828125],[6.328125,9.31640625],[8.701171875,9.84375],[7.8662109375,11.513671875],[6.6357421875,12.1728515625],[6.15234375,10.9423828125]]}`
 
