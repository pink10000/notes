- ways to **corrupt control flow**
	1. stack overflow
	2. heap overflow
	3. pointer subterfuge
	4. double free
	5. format strings
- control control flow $\to$ run code of choice or ROP
- mitigations make it **harder**, but **do not stop** it

# Secure Design Principles
- **Least Privilege** - only provide as much privilege to a program as needed to do its job
- **Privilege Separation** - divide system into separate pieces, requiring multiple different privileges to access sensitive data/code
	- multiple locks
- **Complete Mediation** - check every access that crosses a trust boundary 
	- scan key code every time you enter a door
- **Defense in Depth** - use more than one security mechanism
	- walls on a castle
- **Simple Designs are Preferred** - self-explanatory

### Example: Web Browsers
- processes need to be sandboxed,
- network requests, bookmarks, address bar
- renderer needs to be restricted, especially with access to GPU

### Example: Modern OSes
- process abstraction (each process has a UID), and can only access certain resources
- process isolation (each process can only touch its own memory)
- user/kernel privilege separation 
- Linux uses UIDs and an Access Control List (ACL) to store permissions

## Virtual Memory
- each process get its own **virtual address space**
- mapped to **physical addresses**
- you already know this, let's be real.

## OS Specific Protections
- memory accesses
- privileged instruction
- system calls/faults
- device accesses 
- hardware needs to be combined with software for best protection

### Intel Privilege Levels
- **Ring 0** - Most privileged, kernel mode, can do anything
- **Ring 1, Ring 2** - device drivers
- **Ring 3** - User Applications 
### Arm Privilege Levels
- 2 Worlds, secure and non-secure
- 4 exception levels to do OS related stuff
### System Calls
- user-mode process may need frequent assistance from kernel
- I/O operations, system information, process control
- kernel has its own page table for code/data 
- switch between two different **usermode** processes requires switching between the respective process' address spaces
	- requires flushing TLB
- System calls are **slow**
	- system calls are mapped into kernel's memory space, but **inaccessible** in usermode
	- thus, separate permission bits in page tables


## Elevation of Privilege
- **Threat Model** - how kernel can be attacked
	- treat **ALL** usermode processes as untrusted, in potentially **malicious**
- **Operating Model** - what the kernel needs to function as 
	- usermode processes make a lot of kernel system calls
- usermode process may trick kernel into writing attacker controlled data into memory or leaking kernel memory 

### Null Dereference
- dereferencing `NULL` can lead to crash, but is actually dereferencing address `0x0`
- `NULL` dereference will not cause kernel to crash, but use the bad code on page `0` that is controlled by attacker (**Return-to-User** attack) 

# Virtual Machines
- Isolate OSes to do testing, etc
- hardware that runs OS is virtualized (virtual machine)
- **Hypervisor** implements VM environment and provides isolation between VMs

#### One-Stage
$$
\text{Virtual Address} \to \text{Physical Address}
$$
#### Two-Stage
$$
\text{Virtual Address} \to \text{Intermediate Physical Address}\to \text{Physical Address}
$$
