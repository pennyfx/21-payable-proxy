# 21.co Payable Proxy

Place a payment required proxy in front of any docker service and make it payable.

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
  - host: clarify
# docker service port
    port: 7313
# routes that this service handles
    routes:
    - route: tag
      price: 2000
    - route: rotate
      price: 1000

```

```
# build

$ docker build -t two1proxy/3 .
$ docker run --name two1proxy -p 8928:5000 -v ~/21proxy/config2:/config/ --link clarify:clarify  -v ~/.two1/:/root/.two1/ -d two1proxy/3

# Use --link to add a hosts file entry for the service you want to proxy.
# There are two volume mount points for configuration and a 21.co Wallet.

```

### TODO

- Add fiat prices
- Add route mapping
- Add POST support
- Add tests

