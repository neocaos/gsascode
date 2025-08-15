.PHONY: Run
# https://medium.com/geobeyond/geoserver-docker-starter-guide-ef8ad78450

.PHONY: kill

.PHONY: open

Run:
	docker run -e GEOSERVER_ADMIN_USER=geobeyond  -e GEOSERVER_ADMIN_PASSWORD=myawesomegeoserver -p 8090:8080 kartoza/geoserver:2.18.7


kill:
	docker ps -q --filter ancestor=kartoza/geoserver | xargs -r docker kill


open:
	xdg-open "http://localhost:8090/geoserver/web?0"

