# Heap Vulnerabilities 
- happens via memory management errors
- attacker can attempt to get victim to invoke `malloc()` and `free()` in unintended sequences or with invalid arguments
- free does not remove memory, just puts it in a list that says that chunk is free now
- use after free  
	- 
```C
free(p); p->foo();
free(p); q = malloc(n); memcpy(p, buf, k);
```
- double free
```C
free(p); free(p); q = malloc(n); r = malloc(n); 
free(p); q = malloc(n); free(p);
```          
- multi threaded programs 
```C
malloc();
b = 200;
printf(b);
free(); // not always 200
```

- free will add the same chunk twice if called on already freed object.


## How to fix
- safe heap implementations
- implement a safe unlinking
- cookies on heap (secrets on heap, checked on free)
- heap integrity check to make sure `malloc()` does not fail
- key heap function pointers
- garbage collector !!!!!!! (i fucking love gc)
- centralize memory allocation


# Integer Overflow/Underflow
- `C` defines fixed-width integer types (`short`, `int`, `long`) that do not always behave like regular integers
- fixed width $\implies$ overflow or wrap maximum expressible number for type used
```C
 my_type* foo(int n) {
	 my_type *ptr = malloc(n * sizeof(my_type));
	 for(int i = 0; i < n; i++) {
		 memset(*ptr[i] = i, sizeof(mytype));
	 }
	 return ptr;
 }
```
- if `n` is too large, the number will wrap around to something negative or small. 
- if `n`is negative, it will immediately exit (look at the for loop)
- can fix with unsigned overflow checks with the **complementary** operation 
	- subtraction for addition overflow: `if (UINT32_MAX - a < b)`
	- division for multiplication overflow: `if ((0 != a) && (UINT32_MAX / a < b))`
	- more complex for signed types

## Types
- `char` = 8 bits, 1 byte
- `short` = 16 bits
- `int` = depends on architecture
- `long` = 32 bits

## Conversion
- **Truncation**: when value with wider type is converted to narrower type
	- i.e. `uint32_t` $\to$ `uint16_t`, removes the top parts
- **Zero-extension**: narrow to wide type
	- i.e. `uint16_t` $\to$ `uint32_t`, adds `0`s to top part
- **Sign Extension**: Occurs when narrower, signed type is converted to wider type
	- if negative, adds ones to the top parts
	- if positive, adds zeros to the top parts
- Can be **explicit** or **implicit**
	- **explicit**: `int i = (int) 4.5;`
	- **implicit**: 
		- `signed short i = 1`
		- `if (i < j) { ... }`
		- `void f(int arg); f(5.3);`
- conversion rules are complex, and have some rank to them (typically to at least `int` first)
- this bad implementation is for natural size and architecture, avoid arithmetic errors


## How to Fix
- use strongly typed language
	- like `Java` or `Rust`
- runtime checking
	- trap overflows
	- use safe libraries
	- is *slower*
- static checking (range analysis)