# 0x09. Web infrastructure design

---

## Learning Objectives :bulb:
What you should learn from this project:

* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what each component is doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms:
	* LAMP - Linux OS, Apache web server, MySQL database, and PHP application server
	* SPOF - Single Point of failure
	* QPS - Query per second

## Project tasks

---

### [0. Simple web stack](./0-simple_web_stack)
* On a whiteboard, design a single server with a LAMP stack that includes
  * 1 server
  * 1 web server (Nginx)
  * 1 application server
  * 1 application files (code base)
  * 1 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to server IP 8.8.8.8

* You must be able to explain some specifics about this infrastructure:
  * What is a server
  * What is the role of the domain name
  * What type of DNS record www is in www.foobar.com
  * What is the role of the web server
  * What is the role of the application server
  * What is the role of the database
  * What is the server using to communicate with the computer of the user requesting the website
* You must be able to explain what the issues are with this infrastructure:
  * Locate all single points of failure.
  * Downtime when maintenance needed (like deploying new code web server needs to be restarted)
  * Cannot scale if too much incoming traffic


### [1. Distributed web infrastructure](./1-distributed_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`.
  * 3 servers
  * 2 web servers (Nginx)
  * 2 application servers
  * 1 load-balancer (HAproxy)
  * 2 code base
  * 2 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to server IP 8.8.8.8
* You must be able to explain some specifics about this infrastructure:
  * For every additional element, why you are adding it
  * What distribution algorithm your load balancer is configured with and how it works
  * Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
  * How a database Primary-Replica (Master-Slave) cluster works
  * What is the difference between the Primary node and the Replica node in regard to the application
* You must be able to explain what the issues are with this infrastructure:
  * Where are SPOF
  * Security issues (no firewall, no HTTPS)
  * No monitoring

### [2. Secured and monitored web infrastructure](./2-secured_and_monitored_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.
  * 3 servers
  * 2 web servers (Nginx)
  * 2 application servers
  * 1 load-balancer (HAproxy)
  * 2 code base
  * 2 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to server IP 8.8.8.8
  * 3 firewalls
  * 1 SSL certificate to serve `www.foobar.com` over HTTPS
  * 3 monitoring clients (data collector for Sumologic or other monitoring services
* You must be able to explain some specifics about this infrastructure:
  * For every additional element, why you are adding it
  * What are firewalls for
  * Why is the traffic served over HTTPS
  * What monitoring is used for
  * How the monitoring tool is collecting data
  * Explain what to do if you want to monitor your web server QPS
* You must be able to explain what the issues are with this infrastructure:
  * Why terminating SSL at the load balancer level is an issue
  * Why having only one MySQL server capable of accepting writes is an issue
  * Why having servers with all the same components (database, web server and application server) might be a problem.

### [3. Scale up](./3-scale_up)
* Scale up the previous desing
  * 4 servers
  * 2 web servers (Nginx)
  * 2 application servers
  * 2 load-balancer (HAproxy)
  * 2 code base
  * 2 database (MySQL)
  * 1 domain name `foobar.com` configured with a `www` record that points to server IP 8.8.8.8
  * 3 firewalls
  * 1 SSL certificate to serve `www.foobar.com` over HTTPS
  * 3 monitoring clients (data collector for Sumologic or other monitoring services
  * Split componenets with their own server

---

## Author
* **Amilcar Armmand** - [AmilcarArmmand](https://github.com/AmilcarArmmand)
