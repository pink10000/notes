---
tags:
  - MATH_158
---
# Definition
A **graph** $G$ is a tuple $(V, E)$ where 
- $V$ is a set of **vertices**
- $E$ is a set of **edges** connecting two vertices. Formally, it is a set of *unordered pairs* of elements of $V$.

Mermaid:
```mermaid
graph LR
    A((A)) x--x B((B));
    A((A)) x--x D((D));
    B((B)) x--x C((C));
    B((B)) x--x D((D));
    C((C)) x--x E((E));
    D((D)) x--x E((E));
```

