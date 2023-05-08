# Postmortem Report

## 503 - Service Unavailable Error while accessing `boujee.tech`

![meme](./7ky843.gif)

### Issue Summary

On May 8th, 2023 at 1:00 PM East African Time (EAT),
an outage was reported on `boujee.tech`, which lasted for 1 hour and 30 minutes.
We investigated the issue and found that the website was returning a 503 error.
We found that the issue was caused by a misconfiguration of
the `ufw` firewall on the load balancer server.
The `ufw` firewall was blocking the port 80 which is used by `HAProxy`
to forward requests to the `nginx` server.

### Timeline

* 1:00 PM EAT - The outage was reported by one of the users.
* 1:05 PM EAT - We ensured that HAProxy was running on the load balancer server, and that the `nginx` server was running on the web servers.
* 1:10 PM EAT - We checked the `HAProxy` configuration file and found that it was configured to forward requests to the `nginx` server on port 80.
* 1:15 PM EAT - We restarted the `HAProxy` service and checked the status of the service.
* 1:20 PM EAT - `HAProxy` was running, but the website was still returning a 503 error.
* 1:25 PM EAT - Started debugging the `HAProxy` service, and the logs showed that the backend servers were not accessible.
* 1:30 PM EAT - We used curl to check if the backend servers were accessible from a different server, and they were accessible.
* 1:35 PM EAT - We checked the firewall rules on the load balancer server and found that the port 80 was blocked.
* 1:40 PM EAT - We added a rule to allow traffic on port 80 and restarted the `HAProxy` service.
* 1:45 PM EAT - The website was accessible, and the issue was resolved.

### Root Cause and Resolution

`boujee.tech` is a website that is hosted on two web servers behind a load balancer.
The load balancer is configured to forward requests to the web servers on port 80,
and the web servers are configured to listen on port 80.
Based on the timeline above, we found that the issue was caused by a misconfiguration
of the `ufw` firewall on the load balancer server.
The `ufw` firewall was blocking the port 80 which is used by `HAProxy` to forward requests
to the `nginx` servers.
Upon further investigation, we found that the misconfuguration was caused by a script
that was used to enhance the security of the load balancer server,
which was run by one of the system administrators.

We resolved the issue by adding a rule to allow traffic on port 80 and restarted the `HAProxy` service.

### Corrective and Preventive Measures

* Ensure that the firewall rules are checked before running any scripts that may affect the firewall rules.
* Ensure that the firewall rules are also checked after running any scripts that may affect the firewall rules.
* Verify that the website is accessible after running any scripts that may affect the firewall rules.
