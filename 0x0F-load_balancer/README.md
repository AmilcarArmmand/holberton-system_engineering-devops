# 0x0F. Load balancer

---

## Learning Objectives:bulb:
Concepts covered in this project:

---
### [0. Double the number of webservers](./0-custom_http_response_header)
* Create a Bash script to configure web-02 to be identical to web-01.

### [1. ](./1-install_load_balancer)
* Install and configure HAproxy on your lb-01 server.
* Requirements:
  * Configure HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02
  * Distribute requests using a roundrobin algorithm
  * Make sure that HAproxy can be managed via an init script
  * Make sure that your servers are configured with the right hostnames

### [](./2-puppet_custom_http_response_header.pp)
* Automate the task of creating a custom HTTP header response, but with Puppet

---

## Author
* **Amilcar Armmand** - [GitHub](https://github.com/AmilcarArmmand)
