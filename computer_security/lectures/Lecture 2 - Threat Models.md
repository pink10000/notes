- Assets - What we are protecting?
- Attackers - Who is attacking?

"Remains dependable" is about confidentiality, integrity, and availability. 

## Confidentiality
- Protection of Information, secrecy
	- Like encryption 
- prevention of **eavesdropping**, **copying**, **intercepting**

## Integrity (and Authenticity)
- Making sure there is no unauthorized modification of information, process, or function
	- Cannot change email
	- bank account does not change unless you deposit/withdraw
- prevention of **modification**, **corruption**, **tampering**

## Availability
- Prevention of unauthorized denial of service
	- Someone spams a server so other users cannot use it is an example
	- A webmaster shutting down the server is not (was authorized)
	- superglue in ATM slot
- can **destroy** data, **overwhelm** net, crash **servers** 


In general, it is about the CIA of each each message (Conf of message, integrity of message, availability of message)

## Privacy 
- person's right or expectation to control disclosure of personal information 
- **secrecy** is hiding from third parties
- **privacy** is about not being observed/monitored  


## Vulnerabilities
- weaknesses exploited by others to cause damage
	- where CIA + Privacy not enforced
- look where people assume certain things in the system

## Attackers and Risk Assessment
- **Attackers:** Can vary from individuals to state-sponsored actors, with different capabilities and motivations (e.g., curiosity, financial gain, national interest).
- **Trusted Computing Base:** Set of components essential for security.
	- about devices/software you trust
	- I trust Linux kernel, display server, software on it, etc.
- **Security Boundary:** Perimeter around components of the same trust level; interaction points across this boundary represent the attack surface.
- **Risk Assessment:** Understanding potential threats, their likelihood, and impact to decide on the appropriate security measures.

## Identifying and Addressing Risks
1. **Understand System Requirements:** Know what the system should do and its boundaries.
2. **Identify Assets and Attackers:** Identify stakeholders and what needs protection.
3. **Establish Security Requirements:** Define how confidentiality, integrity, and availability should be maintained.
4. **Review System Design:** Draw diagrams, indicate security boundaries, and identify information flow.
5. **Identify Threats:** Use adversarial mindset and techniques like attack trees and STRIDE model.
6. **Risk Classification:** Based on the likelihood and impact of threats.
7. **Risk Mitigation Strategies:**
    - Avoid: Remove risky components.
    - Mitigate: Add defense mechanisms.
    - Transfer: Make it someone else's problem (e.g., insurance).
    - Accept: Acknowledge residual risk.