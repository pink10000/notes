---
tags:
  - CSE_127
---

# Cross-Site Request Forgery (CSRF)
- browser sends `GET` request attaches all cookies associated with the target site
	- user clicks link
	- another page embedded as an iFrame
	- client-side script
	- cannot see requests authorized by user, only what is coming out of it.

#### Example:
User signs into `bank.com` with a session cookie. User visits malicious site with a fake cookie that looks just like `bank.com`. Attacker cannot see result, but all the money is gone. 

## Secret Validation Token
- `bank.com` can have a secret value in every form that only `bank.com` can validate
	- like a [[Lecture 6 - Countermeasures and Mitigations#Stack Canaries|canary]]. 
	- needs to be dynamically generated
## Referer/Origin Validation
- referer request header contains the URL of the previous web page from which a link to the currenrly requested page was followed
	- like a path of webpage history to verify you have been at the right places
- assumes `GET` has no side effects (not always true)
- assumes browswers respect `SameSite` attribute
	- cookie option that prevents browser from sending a cookie with cross-site requests
	- `Strict`: never send cookies
	- `Lax`: session cookie is allowed only on navigation link
	- `None`: send cookies from any context
## Fetch Metadata
```
Sec-Fetch-Site: {cross-site, same-origin, same-site, none} 
	Who is making the request? 
Sec-Fetch-Mode: {navigate, cors, no-cors, same-origin, websocket} 
	What kind of request? 
Sec-Fetch-User: ?1 
	Did the user initiate the request? 
Sec-Fetch-Dest: {audio,document,font,script,..} 
	Where does the response end up?
```
- has direct identification of request context `Site`, `Mode`, `Dest`
- built-in resistance to spoofing `Site`
- usually only for newer browsers
