
# Return-To-libc
```C
int system(const char *command);
```
Uses `fork` to create a child process that executes the shell command specified in command using `execl` as follows:
```C
execl("/bin/sh", "sh", "-c", commnd, (char *) 0);
```
- Needs to find the address of `system()` and string `/bin/sh`
- Overwrite the return address of `system()` and take control of it.

## How To:
- setup stack frame to look like a normal call to `system()`
- prof talks about calling and returning on the stack (review!)
- when system runs the stack needs to look like this:
```C
cmd="/bin/sh"
&cmd
&exit
```
so it looks like a legit call to the system, but we're going to use `ret` not `call` to the function.
![[Pasted image 20241017141300.png]]
Here, we are about to return to `bar`, but then transfers control to the system function.
- many different ways to get access to the system

# Return Oriented Programming
- what if you need to do something more complicated?
- what happens if we jump to *almost* the end of some function?
	- execute last few instructions
	- `ret` call.... but where?
	- return to address on the stack, but if we change it, we can control this address
	- choose to return to another tail of an existing function
- make complex shellcode out of *existing application code*
- most processors work the same way
	- `x86` is a bit different since instructions are variable length
	- more function tails to look at for the return call, `0xC3`
- eventually becomes a Turing Computer
	- load, store gadgets
	- arithmetic and logic gadgets
	- control flow gadgets
- OK I LITERALLY DON'T UNDERSTAND ANYTHING UP TO HERE


# Control Flow Integrity (CFI)
- given a new attack technique, we must develop a new countermeasure
- Almost all attacks we've seen is attacker *overwriting jump targets*
- what if `ret`, `calls`, etc could only go to known good targets
- focus on protecting indirect transfer of control flow instructions

## Direct
- advancing to next sequential instruction
- jumping to a hard-coded address
- static in code, so assume attacker can't control them (if they can overwrite code segments, it is `gg no re`)

## Indirect
- jumping to or calling a function at an address in register or memory
- **Forward Path**: indirect calls and branches (function you are calling)
- **Reverse Path**: return addresses on the stack (return from called function)

-----
- what is a **legitimate target**?
- how do we know if when we return, it is the right place?

## Basic Design
- restrict all control transfers to the control flow graph
- assign labels to all indirect jumps and their targets
- before taking an indirect jump, validate that target label matches jump site
- this is like [[Lecture 6 - Countermeasures and Mitigations#Stack Canaries|stack canaries]]. 
- assign label to each target of indirect control transfer
- instrument indirect control transfers to compare label of destination, to ensure it is valid

# Shadow Stack
- keep main stack for legacy
- shadow stack is unwritable, to save call control flow data
- on return from main stack, check the shadow stack that it is correct
- requires **compiler support**, **fast hardware support**.

# Coarse-Grained CFI
- trade off speed for precision
- identify if control transfer is clearly wrong, but not that is right
- 2 labels, no shadow stack
- label for destination of **indirect calls (forward)** 
- label of destination of **`ret`s** and **indirect jumps (reverse)**

## Tradeoffs:
- additional computation needed for free branch instruction. 
- more code size, needs strong enough computer
- needs reliable DEP

do not validate all data=dependent 