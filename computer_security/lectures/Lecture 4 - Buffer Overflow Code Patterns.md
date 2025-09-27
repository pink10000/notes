---
tags:
  - CSE_127
---
3 Checks;


## Missing Check
- does the code perform bounds checking on memory checks?

## Avoidable Check
- is the check happening?
- test to make sure memory writes stay within intended bounds can be bypassed 
- checks need to happen **before** the offending interruption or else it will be too late

## Wrong Check
- is the check right?
- test to make sure memory writes stay within intended bounds is wrong
- look for complicated runtime arithmetic in length checks 
- is `\0` accounted for?
- if you see non trivial arithmetic operations inside a length check, assume something is wrong


## Addressing Buffer Overflows
- using memory safe languages
- train developers to write secure code with secure tools
- language choice is frequently not an option
	- manual code reviews, static analysis, adversarial testing
	- make remaining bugs harder to exploit


# Format String Vulnerabilities
- function arguments and local variables are stored on the stack
- next to data like return address and saved frame pointer
- implicit agreement on caller/callee w/ number/size/ordering of function arguments

## `printf()`
- has set parameters each with a specific type 
- has many different versions of `printf()`
- each argument has max length or max size
- `C` supports variable number of arguments
- different ways to do so:
	- argument to specify count
	- last argument has terminator value
	- another argument that implicit encodes count (`printf()` does this)
- caller pushes arguments onto stack, pushes pointer to format string onto stack
- callee 
	- parses format string itself via the pointer 
	- uses the format string to read the arguments off the stack
	- reads one value off stack for each `%` parameter
	- `printf` is looking up the stack, controlled by `% parameters`
```C
printf("%d\n", 10, 20, 30); // print 10
printf("%d - %d\n", 10); // print 10, then random stuff on memory
```
- user is responsible for enforcing one-to-one mappings between _format specifiers_ (`%`) and _arguments_
	- too many $\to$ match first, then print garbage values (go beyond arguments to local var, `%ebp`, etc)
	- too little $\to$ match first, then done
- attacker can use this vulnerability to print off stack values to read/write memory with arbitrary 

### Reading
- imagine you just printed:
```C
str[80] = "x10\x01\x48\x08_%08x.%08x.[%s]";
int i, j;
printf(str);
// 0x08480110
```
- this will go to the address and print the stack
- uses `%08x` to move printf internal argument pointer up the stack, back past locals into the format string itself in the stack pointer until it reads the string itself
- reads the first of the string which is a memory address, and goes to that place
### Writing
- simple buffer overflow:
```C
if (strlen(src) < sizeof(dst)) sprintf(dst, src);
```
- writes `src` into `dst` after checking if the size of the source is small enough
- using `%n` is the only specifier that has a write call
	- stores number of characters up until the `%` in `%n`
```C
int x = 0;
printf("Hello %n", &x) // after call x == 6
```
- exists for pretty printing
- combine with reading trick to write to arbitrary addresses $\to$ write one byte at a time to arbitrary addresses

## Summary
- Functions that take format strings act like little command interpreters
- do not let attackers decide which commands to pass to your command interpreters


# Heap Vulnerabilities
- `C` uses **explicit memory management**
	- data is allocated dynamically from the heap with `malloc` and `free`
	- accessed via pointers
	- programmer is responsible for the details, system does not track memory (no garbage collection)
- what if attacker is able to **corrupt** data on the heap
	- program data
	- heap metadata
- what if attacker can cause the program to use `malloc` and `free` in unexpected **combinations**?
## (Typical) Heap Implementation
- heap managed by **heap manager**
	- many different one sin a system
- heap manager contains chunks of available memory
- layout changes based on `malloc()` and `free()`
	- coalesce, allocate, split
- chunks stored in doubly linked lists (called **bins**)
- 3 Flags:
	- **size**: stores size of it
	- **N**: non main arena (not relevant)
	- **M**: is Mmapped (not relevant) 
	- **P**: previous chunk is in use
	- **prev size**: contains previous size of the chunk (easy to coalesce)
- `malloc` returns pointer to the _start_ of the free chunk 
- last chunk points to first chunk and vice versa (doubly linked)

## Overwriting Program Data
- effect depends on variable semantics
- variables that store result of a security check (BAD!)
- variables used in security checks
	- `isAuthenticated`, `isValid`, `isAdmin`
- data pointers
	- `database`
- function pointers 
	- direct transfer of control when function is called through *overwritten pointer*
	- in `C++`, `vTables`, functions can be called through abstracted interfaces (like in Java)
### C++:`vTables`
```C
clase Base {public: virtual void foo() {cout << "hi\n"; } };
clase Deri: public Base {public: void foo() {cout << "bye\n";} };

void bar(Base* obj) {obj->foo();}

int main() {
	Base *b = new Base();
	Deri *d = new Deri();

	bar(b); // hi
	bar(d); // bye
}
```
- `vTable` is an array of function pointers
	- every object in `C++` has a `vTable`
- based on class and function, the compiler knows which offset to use in the `vTable`
- interfaces and multiple inheritances, let use print random stuff by overwriting it as if it were still valid
- when a `vTable` is compromised, an attacker can use their `vTable` which can contain any arbitrary code and compromise the system
	- overwrite/change/replace `vTable` $\to$ change control flow
- `unlink(P, BK, FD)` is a `C` macro 
	- write, what, where
	- pointer, back pointer, forward pointer
	- if hacker can get access to the address of the <INSERT THINGS HERE>