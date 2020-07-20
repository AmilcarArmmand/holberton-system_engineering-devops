# 0x09. Web infrastructure design

---

## Learning Objectives :bulb:
What you should learn from this project:

* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what each component is doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

## Project tasks

---

### [0. Simple web stack](./0-simple_web_stack)
* On a whiteboard, desogn a single server with a LAMP stack that includes
  * 1 server
  * 1 web server (Nginx)
  * 1 application server
  * 1 application files (code base)
  * 1 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to server IP 8.8.8.8


### [1. Distributed web infrastructure](./1-distributed_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.
  * 3 servers
  * 2 web servers (Nginx)
  * 2 application servers
  * 1 load-balancer (HAproxy)
  * 2 code base
  * 2 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to server IP 8.8.8.8


### [2. Secured and monitored web infrastructure](./2-secured_and_monitored_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
  * 3 servers
  * 2 web servers (Nginx)
  * 2 application servers
  * 1 load-balancer (HAproxy)
  * 2 code base
  * 2 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to server IP 8.8.8.8
  * 3 firewalls
  * 1 SSL certificate to serve www.foobar.com over HTTPS
  * 3 monitoring clients



### [3. Scale up](./3-scale_up)
* Readme

---

## Author
* **Amilcar Armmand** - [AmilcarArmmand](https://github.com/AmilcarArmmand)
