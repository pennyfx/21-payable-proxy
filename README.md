# 21.co Payable Proxy

Place a payment required proxy in front of any docker service and make it payable.


## yaml Config

Configuration is based on the following yaml format.

```yaml
# config.yaml

# prefix for payable routes
prefix: /payable/
# not currently used
currency: BTC
# registered services
service:
# docker service name
  - host: tagservice
# docker service port
    port: 7313
# routes that this service handles
    routes:
    - route: tag
      price: 2000
    - route: colorify
      destination: color
      price: 1000

```

## Build
```
$ docker build -t two1proxy/1 .
```

## Run
```
$ docker run --name two1proxy -p 8928:5000 -v ~/21proxy/config:/config/ --link tagservice:tagservice  -v ~/.two1/:/root/.two1/ -d two1proxy/1
```

### Link
Use `--link` to add a hosts file entry for the service(s) you want to proxy.

### Volumes
`/config/` - yaml file with services routes to proxy and fees
`/root/.two1/ ` -  21 wallet to use

## 21 Buy Example
```
# if you have a tagging service behind the proxy, call it like so.

$ 21 buy http://[dockerip]:8928/payable/tag?url=http://i.imgur.com/aNJjbfC.jpg

```

### Notes:

Only supports GET and POST for now.




### TODO

- fiat prices
- ~~route mapping~~
- ~~POST support~~
- add tests
- round-robin if many of the same services are defined

### License

MIT
