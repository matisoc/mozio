# mozio

 - http://server/ -> swagger doc.
 - http://server/admin/ -- admin panel
 - http://server/api/v1/ -- API

## API ##

GEOJSON Objects examples:

	- {"type":"Point","coordinates":[9.26436996459961,10.564178042345375]}
	- {"type":"Polygon","coordinates":[[[6.15234375,10.9423828125],[6.328125,9.31640625],[8.701171875,9.84375],[7.8662109375,11.513671875],[6.6357421875,12.1728515625],[6.15234375,10.9423828125]]}

Methods
	- Get all providers -> `GET /api/v1/providers/` 
	- Create new provider `POST /api/v1/providers/ {"name": "required", "email": "", "phone": null, "language": null, "currency": ""}`
	- Get all services-areas `GET /api/v1/service-areas/` 
	- Get services-areas filtered `GET /api/v1/service-areas/?poly__contains={"type":"Point","coordinates":[9.26436996459961,10.564178042345375]}`
	- Get all services areas filtered by providerID `GET /api/v1/service-areas/?provider_id=1` 
	- Create new service provider area `POST /api/v1/service-areas/ {"name": "required", "provider_id": "required", "price": "required", "poly": "required; GeoJson Polygon"}` 


### Requirements
1. Docker
1. docker-compose

### Steps to reproduce

1. Start Docker Native
1. Build images - `docker-compose build`
1. Create the database migrations - `docker-compose run web python manage.py migrate`
1. Start services - `docker-compose up`	
1. View in browser http://127.0.0.1:8000/
