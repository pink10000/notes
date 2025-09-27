# Web Architecture
1. browser $B$ issues requests to internet $I$
2. server $S$ responds through $I$
3. $B$ renders response
$$B \iff I \iff S$$

## Anatomy of a Request

```
GET /index.html HTTP/1.1

Accept: image/gif, image/x-bitmap, image/jpeg, */* 
Accept-Language: en 
Connection: Keep-Alive 
User-Agent: Mozilla/1.22 (compatible; MSIE 2.0; Windows 95) 
Host: www.example.com 
Referer: http://www.google.com?q=dingbats
```
Does a `GET` request on the server for the page `index.html` on the root `\` directory with some headers. 
- `GET`: retrieve a resource
- `POST`: update a resource

### HTTP/2
- 47% of the web as of October 2021
- allows pipelining requests for multiple objects
- multiplexing allows multiple requests over one TCP connection 
- header compression
- server push
### HTTP/3
- 22% of the web
- uses QUIC instead of TCP

## Response
- Had a status code,
```
HTTP/1.0 200 OK

<HEADERS>

<BODY>
```
The body is typically some `html` code.
- `200`: OK
- `303`: See other (redirect)
- `404`: Not Found

# Web Cookies
- HTTP is stateless, but cookies are needed to keep session
	- sessions
	- personalization
	- tracking
```
cookieID=cookieValue
```
like a dictionary.

# Nested Execution Model
- windows may countain frames from different sources
	- `Frame`: rigid visible division
	- `iFrame`: floating inline frame
- frames are used to delegate screen area to content from another sources
- browser decides **isolation** based on frames
Message passing via postMessage API: 
- Sender:
```js
targetWindow.postMessage(message, targetOrigin);
```
- Receiver: 
```js
window.addEventListener("message", receiveMessage, false); 
function receiveMessage(event) { 
	if (event.origin !== "http://example.com") 
		return; 
	...
}
```

# Document Object Model (DOM)
- JS can read/modify page by interacting with the DOM. 
	- OOP way to interface reading/writing website content.
- access window, document, and other state like *history*, *browser navigation*, and *cookies*.
- JS can change the webpage contents dynamically and itself.

# Browser Security
- **Network Attacker**: attack on the connection between both the client and the server
- **Web Attacker**: someone attacking the webpage
	- **Gadget Attacker**: capabilities to inject limited content into honest page
	- attacks pretending to be legit, embedding bad webpages into good ones and vice versa

- Browswer isolates each page as if were a process:
$$\begin{aligned}
	Process &\iff Page \\
	File System &\iff Cookies/HTML Local \\
	Addr Space, UID &\iff SOP \\
\end{aligned}$$
## Same Origin Policy (SOP)
- the isolation unit/trust boundary on the web
- `(scheme, domain, port)` triple derived from URL
- every frame has its own origin, and can only access data from the same origin
	- can load cross-origin HTML in frames, but not inspect/modify the content
	- scripts can be loaded across origins
	- images can be rendered, but not inspected pixel by pixel
- Cookie SOP: `(scheme, domain, path)`
	- `(https, cseweb.ucsd.edu, /classes/fa24/cse127-a)`
	- Domain is any suffix of the URL hostname, except public ones. 
	- ![[Pasted image 20241116163717.png]]
	- Path can be set to anything.  
	- Deciding to send cookies is determined by the "file path". In general, you do not have access to previous domains. 
	- `login.site.com` $\neq$ `other.site.com`
	- not fine grain