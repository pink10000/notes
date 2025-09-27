---
tags:
  - CSE_127
---
## **Introduction to Cryptography**  
Cryptography provides methods to ensure **confidentiality** and **integrity** over potentially insecure communication channels.

- **Primary Goals**: 
  - **Confidentiality**: Only intended recipients can read the message.
  - **Integrity**: Ensures the message is not altered.
  - **Authenticity**: Verifies the sender's identity.

---

## **Motivating Example**  
Consider **Alice** and **Bob** wanting to communicate a simple message (like "yes" or "no") without letting **Eve** (an observer) know its content.

- Questions:
  - How can Alice communicate securely with Bob without Eve knowing?
  - How can Bob trust that the message is from Alice?

---

## **Basic Concepts in Cryptography**  
- **Threat Model**: Understanding the attacker’s capabilities (e.g., passive or active interception).
- **Key Distinctions**:
  - Confidentiality and integrity require **different cryptographic techniques**.
  - Protection against passive attackers does not imply security against active or man-in-the-middle (PitM) attacks.

### **Encryption Basics**  
- **Plaintext**: Original, readable message.
- **Ciphertext**: Encrypted, unreadable version of the message.
- **Cipher**: The algorithm for transforming plaintext into ciphertext and vice versa.
$$
c = E(m) \quad\quad m = D(c)
$$

where $c$ is the ciphertext, $m$ is the plain text, $E$ is the encryptor, $D$ is the decryptor.


## **One-Time Pad (OTP)**  
A one-time pad achieves **perfect secrecy** by XORing plaintext with a random key known only to sender and receiver.
$$c = m \oplus r$$
- **Perfect Secrecy**: Every plaintext is equally probable given the ciphertext.
- **Drawbacks**: Requires a unique key of the same length as the message for each communication.

Given a shared key, that is completely random, you can encode messages into numbers, and perform modulo arithmetic to get a completely random ciphertext.

---

## **Computational Cryptography**  
**Modern cryptography** sacrifices perfect secrecy for practicality, using shorter keys to achieve security within **computational limits**.

- **Kerckhoffs's Principle**: Cryptosystems should be secure even if everything except the key is public.
	- only the key is *secret*
- **Shannon's Maxim**: "The enemy knows the system," meaning security should not rely on obscurity.

---

## **Cryptographic Primitives**  
### **Symmetric Cryptography**
- **Shared Secret Key**: Both parties use the same key for encryption and decryption.
- Commonly known as **Secret-Key Cryptography**.
- **Message Authentication Code**: provides *integrity* w/o *confidentiality*.
	- adversary cannot generate a valid MAC or signature without knowing the secret key.
 
 ### **Asymmetric Cryptography**
- **Two Keys**: Each party has a public key (shared openly) and a private key (kept secret).
- **Public-Key Cryptography** allows for secure communication without a shared secret, enabling encryption and verification using public keys.
- **Digital Signature**: provides *integrity* w/o *confidentiality*
	- adversary cannot generate a valid MAC or signature without knowing the secret key.
### Encryption
- provides *confidentiality* without *integrity* protection.
- adversary should not be able to determine which is encrypted without knowing the secret key
- changes to ciphertext can lead to predictable changes in decripted plaintext.
---
## **Randomness in Cryptography**  
Cryptographic algorithms rely on **cryptographically secure pseudo-random number generators (CSPRNGs)** for randomness, which must be:
  - **Unpredictable** and **uniformly distributed**.
  - Securely generated, especially using system APIs for critical applications.

---

## **Hash Functions**  
A cryptographic **hash function** maps data to a fixed-size string and ensures:
  - **Pre-image Resistance**: It’s difficult to find an input that matches a specific output.
  - **Collision Resistance**: It’s challenging to find two inputs that produce the same output.
  
Common hashes:
  - **SHA-2**: Widely used but susceptible to future collision attacks.
  - **SHA-3**: Newer, recommended for applications needing strong collision resistance.

---

## **Symmetric Encryption Techniques**  
### **Stream Ciphers**  
Generate a pseudorandom keystream, XORed with plaintext for encryption.
- Example: **ChaCha20** (secure with 256-bit keys and unique initialization vectors).

### **Block Ciphers**  
Encrypt data in fixed-size blocks (e.g., **AES** with 128-bit blocks).
- **Modes of Operation**:
  - **Electronic Code Book (ECB)**: Encrypts each block independently but is insecure due to pattern exposure.
  - **Cipher Block Chaining (CBC)**: Chains blocks by XORing each plaintext block with the previous ciphertext.
  - **Counter (CTR)**: Converts a block cipher into a stream cipher by XORing with successive encrypted counter values.

### **Authenticated Encryption**  
Combines confidentiality and integrity in a single algorithm. Recommended modes include **AES-GCM** and **ChaCha20+Poly1305**.

---

## **Limitations of Symmetric Cryptography**  
- Requires secure key exchange for each pair of communicators, which is challenging to scale.
  
---

## **Asymmetric Cryptography**  
Each participant has a **public and private key**.
- **Public Key**: Used by others to encrypt messages or verify signatures.
- **Private Key**: Used to decrypt messages or create signatures.

### **Common Asymmetric Algorithms**  
- **RSA**: Based on the difficulty of factoring large integers.
- **DSA and ElGamal**: Rely on the difficulty of discrete logarithms.

---

## **Combining Symmetric and Asymmetric Cryptography**  
- **Hybrid Approach**: Use asymmetric cryptography to establish a symmetric session key, which is then used for efficient encryption of message data.
  - **Example**: Encrypt the message with a symmetric key, encrypt the key with the recipient’s public key, and send both.

### **Signing and Verification in Practice**  
- **Signing**: Hash the message, then sign the hash using the sender’s private key.
- **Verification**: Hash the message again and verify it matches the received signed hash using the sender’s public key.

---

## **Summary**  
### Key Points  
- Cryptographic mechanisms for **confidentiality** and **integrity** are separate and need careful selection.
- **Use established libraries** and avoid implementing cryptography independently due to complexity and risk.
