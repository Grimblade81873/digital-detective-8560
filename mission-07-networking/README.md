# Mission 7 — How Computers Communicate

## 1. Task / Objective

Explain basic network types and concepts, observe network lookup and connectivity information, and describe the step-by-step process of what happens when a website is opened.

## 2. Work Completed

- Completed the network concepts table with explanations and examples for LAN, MAN, WAN, DNS, router, protocol, packet switching and client-server.
- Ran a connectivity test (`ping`) and a DNS lookup (`nslookup`) from Terminal.
- Wrote a 7-step explanation of what happens when a website is opened in a browser.

## 3. Commands / Tools Used

| Command | Purpose |
|---------|---------|
| `ping -c 2 example.com` | Send two packets to example.com to test whether my computer can reach it over the network |
| `nslookup example.com` | Look up the IP address associated with the domain name example.com |

## 4. My Understanding

### Task 7.1 — Network Concepts

| Concept | Explanation (in my own words) | Example |
|---------|------------------------------|---------|
| **LAN** (Local Area Network) | A network that covers a small area and connects devices that are close together. All the devices usually share one internet connection. | The Wi-Fi network at my home connecting my laptop, phone and smart TV. |
| **MAN** (Metropolitan Area Network) | A network that covers a larger area than a LAN, like a city or a large university campus. It connects multiple LANs together. | A university network that links all the buildings and hostels on a large campus spread across the city. |
| **WAN** (Wide Area Network) | A network that covers a very large geographical area, often connecting cities or countries. The internet is the biggest WAN. | The internet itself, which connects billions of devices across the world. |
| **DNS** (Domain Name System) | A system that translates human-readable domain names (like google.com) into IP addresses (like 142.250.182.14) that computers use to find each other. | When I type `github.com` in my browser, DNS finds the IP address of GitHub's server so my browser knows where to send the request. |
| **Router** | A device that connects different networks and decides the best path to forward data packets between them. | My home router connects my local home network to my internet service provider's network. |
| **Protocol** | A set of rules that devices follow so they can communicate and understand each other. Without protocols, devices would not know how to format or interpret messages. | HTTP (HyperText Transfer Protocol) defines how web browsers request pages and how servers respond. |
| **Packet switching** | A method where data is broken into small chunks called packets. Each packet can take a different route through the network and they are reassembled at the destination. | When I download a file, it does not travel as one big block. It is split into packets that may take different paths and arrive in any order, then get put back together on my computer. |
| **Client-server** | A model where one device (the client) requests a service and another device (the server) provides it. The client asks, the server answers. | My web browser (client) sends a request to GitHub's server, and the server sends back the web page. |

### Task 7.2 — Observe Network Information

**Connectivity test (`ping`):**

```
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=57 time=18.904 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=57 time=54.832 ms

--- example.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
```

- **What does a connectivity test help me check?** It tells me whether my computer can reach another device over the network. If I get replies back, the connection is working. It also shows the round-trip time (how long it takes for data to travel there and back), which indicates how fast the connection is.

**DNS lookup (`nslookup`):**

```
Server:    8.8.8.8
Address:   8.8.8.8#53

Non-authoritative answer:
Name:   example.com
Address: 104.20.23.154
```

- **What information does a DNS lookup display?** It shows the IP address (or addresses) associated with a domain name. It also shows which DNS server answered the query (in my case, 8.8.8.8, which is Google's public DNS server).

- **Role of DNS when entering a website name:** When I type a website name in the browser, the browser does not understand words — it needs a numerical IP address. DNS acts like a phone book: it looks up the domain name and returns the IP address so the browser knows where on the internet to send its request.

### Task 7.3 — What Happens When You Open a Website?

Here is what happens step by step when I type `example.com` into my browser and press Enter:

1. **Browser parses the URL.** The browser reads the address I typed and identifies the protocol (HTTPS) and the domain name (example.com).

2. **DNS lookup.** The browser asks a DNS server to translate `example.com` into an IP address. The DNS server responds with something like `104.20.23.154`.

3. **Browser connects to the server.** Using the IP address, the browser (acting as the **client**) sends a connection request through my **router** and across the internet to the web server at that address. This uses the TCP protocol to establish a reliable connection.

4. **Browser sends an HTTP request.** The browser sends an HTTP GET request to the server, asking for the web page. This request travels as **packets** across the network.

5. **Server processes the request.** The **server** receives the request, finds the requested page, and prepares a response. The server sends back an HTTP response containing the HTML code of the page, along with a status code (like 200 for success).

6. **Data travels back through the network.** The server's response is broken into packets that travel back through routers across the internet to my computer. The packets are reassembled in the correct order.

7. **Browser renders the page.** The browser receives the HTML (and any CSS, JavaScript or images), processes it, and displays the finished web page on my screen. I see the content of example.com.

## 5. Difficulties Faced

I was confused about the difference between a protocol and a standard at first. I also noticed that `nslookup` returned two different IP addresses for example.com and was not sure why.

## 6. How I Resolved Them

I understood that a protocol is specifically about communication rules (like HTTP defining how to request and serve web pages), while a standard can be broader. As for the two IP addresses, I realised that many websites have multiple servers (or use a CDN) so they can handle more traffic and serve users from the nearest location.

## 7. Evidence / Files

- `mission-07-networking/README.md` — this file with all network concepts, observations and the website explanation

## 8. Commit Details

**Commit message:** "Explain networking concepts and website communication"
Work has been pushed to GitHub and verified.
