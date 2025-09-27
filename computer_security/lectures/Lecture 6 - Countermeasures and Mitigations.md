---
tags:
  - CSE_127
---


- asking developers to not insert vulnerabilities has not worked
	- people make mistakes
	- not all are discovered
- countermeasures as a next line of defense
	- reduce what the attacker can access
	- reduce how much damage the attacker can do (or steal)


# What are we preventing?
- overwriting of the return address
- hijacking of the control flow
- all out of bounds memory access

## Approaches
- Stack canaries/cookies (detect overwrites)
	- canary in mine, if dies, all miners need to leave ASAP
- Memory Protection (difficult to redirect control flow)
- Address Space Layout Randomization

# Stack Canaries
- stack based buffer overflows
- goal is to detect if the return address is overwritten
- place a special value between local variables and the saved frame pointer
- check value before popping saved frame pointer
![[canarystack.png]]
- When returning, check canary against **gold** copy.
- jump to exception handler if different
- best canary:`0x000A0D0FF`
	- stores `NUL`, `CR`, `LF`, `EOF`
- Canary must be secret (if it is fixed, it is easy to know what to put there)
- do not protect against non-sequential overwrites

## How to use them? and when?
- `-fstack-protector` 
	- for functions with char buffers $\geq$ ssp-buffer-size
	- functions with variable sized `alloc()`
- `-fstack-protector-strong`
	- functions with local arrays of any size/type
	- functions that have references to local stack variables
- `-fstack-protector-all`
	- all functions'
- more protection $=$ increase cost for every function

## Bypass
- skip over the canary 
- attacker can overwrite the canary with the correct value
- terminator canaries are impossible to is overwrite
- canary value is selected at process creation, and has the same value
- can brute force
	- forked process has some memory layout and contents as parent, including **canary values**
	- lets us try a bunch of canaries and crashing the program
- attacker can overwrite local variables, security checks, function pointers, or data pointers

### Pointer Subterfuge
- skips over the pointer
- add more here to understand it

# Non-executable Stack
- Goal: prevent execution of shellcode on stack
- Modern processors can mark virtual memory pages with permission bits: 
	- **R**ead, **W**rite, E**X**ecute 
	- RWX
- Mark all pages either writable or executable, but not both
- sometimes called `W^X` to show write XOR executable

### Pros
- no changes to application software
- little to no performance impact (due to TLB lookup)
### Cons
- requires hardware support 
- does not work automatically with certain programming tricks

## Assumptions
- prevent attackers from injecting code $\implies$ deny ability to execute malicious code
- all pages are either write-able or executable

## DEP Bypass
- special handling needed for JIT code (JS), memory overlays, and self-modifying code
- extremely common
- transferring control flow to existing function can be coerced into doing something bad
- attacker can execute arbitrary code **without** even needing to **inject** it into the victim process

### Prevention: Hide Shellcode's Location
- Assumptions:
	- stack smashing exploits depend on being able to predict stack addresses
	- harder to guess the location of the shellcode on the stack
		- bypass would only work with info leak, guessing, and longer `NOP` sled.
- requires compiler, linker, and loader support
- increases code size, and performance overhead
- RNG dependency on canaries
- potential load time impact for relocation
- Bypass:
	- information leak/guessing
	- heap spraying

### Heap Spraying
- what if we used **overwhelming force** to go to everywhere, and then use a long NOP sled and find where you need to be in the stack
- make a bunch small items of the bad code in the heap, then have them try to find the shellcode location


# Summary
- theory, kind of reliable, by making it harder for exploits to work
- practice, varying effectiveness, typically decreases with time as new bypasses are developed