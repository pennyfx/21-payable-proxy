# 21.co Payable Proxy

Place a payment required proxy in front of any docker service to require a payment before passing requests.

```yaml
# config.yaml

# prefix for payable routes
prefix: /payable/
# not used, yet but plans to support fiat prices
# by looking up the current price
currency: BTC
# registered services
service:
# docker service name
  - host: clarify
#docker service port
    port: 7313
#routes that this service handles
    routes:
    - route: tag
      price: 2000
    - route: rotate
      price: 1

```

