---
tags:
  - CSE_127
---

When is a program secure?
- when it doesn't do bad things
	- easier to specify bad things
	- what if most of the time it doesn't do bad things, but occasionally it does? or could? is it secure?
- Complex systems always have unintended functionality
- an **exploit** is a mechanism in which someone triggers this unintended functionality


# Vulnerabilities
- control flow integrity
	- attacker can execute any kind of code by changing how a program does its control flow
	- in particular, memory
- unsecured input, or where anything an adversary can control will be an issue
- can be caused by unsafe languages (C/C++)
	- no automatic bounds checking for strings (no `\0`)
	- `gets()`, `strcpy()`
- a single byte of buffer overflow is sometimes all is needed
- Fingerd:
	- check slides for this
	- recall back to 224 sending an EOF instantly when you had a socket in golang
	- golang is more safe


# Buffer Overflow

## Stack
- Grows downwards, from max address from top to bottom, where bottom is 0x00...
- has static data, and text in that order

## Heap
- grows on top of the stack, from the bottom


## Arrays in C
- Contiguously stored in memory
- elements stored by `base address + size of type * index`

## Function Calls
- Function calls inside other functions
- variables inside functions are allocated by the stack
- **Stack Pointer** points to the top of the stack
	- grows from from high to low addresses
	- stored at `%esp` in x86
- **Base Pointer** points to the frame
	- stored as `%ebp`

How they get called;
1. arguments called by a function are added to the stack
2. the stack pointer moves down as this is added
3. return address stored as `ret` instruction
4. save old frame pointer `%ebp` (at this point `%esp` is here)
5. set `%ebp` to here
6. execute the called function 

## x86 Review
- Registers
	- `%eax, %ebx, %ecx, %edx, %esi, %edi`
	- program counter `%eip`, stack pointer `%esp`, base pointer `%ebp`
- instructions
	- `movl`, (move to the address)
	- `pushl`, push to the stack
	- `popl`, pop to the stack
	- `call`, calls a function 
	- `ret`, return address in the stack 
- all ends with `l` because of AT&T specification
- https://godbolt.org for compiler

### Notes on Intel vs AT&T
- `%,l` used in AT&T
- intel does not

## Smashing The Stack
- copying a string past what it can hold will overwrite it into the stack:
```C
char nice[] = "is nice";
char name[8]
```
is fine. but
```C
char nice[] = "is nicejfhdsfbdgshfdsghfdhs";
char name[8]
```
will overwrite the stack.
- overwrite local variables
- saved frame pointer
- return address
- function arguments
- deeper stack frames, etc

- Changing the **return address is the worst** here
- lets attackers redirect the code to anywhere else (i.e. shellcode)
	- access to the shell -> access to the entire system (terminal)
	- `execve("/bin/sh", argv, NULL)`

## Aleph One Paper
- encode shellcode into data buffer
- set return address to the shellcode
- eliminate `0x00` which is the null terminating character 



