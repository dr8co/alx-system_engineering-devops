# 0x10. HTTPS SSL

A secure connection between a client and a server is established using `SSL` (Secure Sockets Layer) or `TLS` (Transport Layer Security).

`SSL` creates a secure tunnel and all data that travels through this tunnel is encrypted.
The two parties must authenticate each other using digital certificates.

`SSL` is now deprecated and has been replaced by `TLS`, which is the new industry standard for secure connections.

**TLS is backward compatible with SSL,** and is based on SSL 3.0.
Most web browsers still refer to the protocol as SSL. However, the protocol is now officially known as TLS.

![SSL](./ssl.png)

This project covers the following concepts:

- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means
