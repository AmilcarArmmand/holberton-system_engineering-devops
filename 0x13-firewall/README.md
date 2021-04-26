# 0x13. Firewall

---
## Learning Objectives:bulb:
How to install and configure a firewall on our web servers and load balancer.

---
## Project tasks

### [0. Block all incoming traffic but](./0-block_all_incoming_traffic_but)
* Install the ufw firewall and setup a few rules on web-01.
* Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
  * 22 (SSH)
  * 443 (HTTPS SSL)
  * 80 (HTTP)

### [1. Port forwarding](./100-port_forwarding)
* Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.

---

## Author
* **Amilcar Armmand** - [AmilcarArmmand](https://github.com/AmilcarArmmand)
