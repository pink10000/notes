---
tags:
  - MATH_158
---
# Definition
A **graph** $G$ is a tuple $(V, E)$ where 
- $V$ is a set of **vertices**
- $E$ is a set of **edges** connecting two vertices. Formally, it is a set of *unordered pairs* of elements of $V$.
```dataviewjs
const { default: {mermaidAPI} } = await import('https://cdn.jsdelivr.net/npm/mermaid@11.12/dist/mermaid.esm.min.mjs') 

mermaidAPI.initialize({ startOnLoad: false }); 

let el = dv.el("div", null); 
const graphDefinition = ` 
graph LR
    A((A)) --- B((B));
    A((A)) --- D((D));
    B((B)) --- C((C));
    B((B)) --- D((D));
    C((C)) --- E((E));
    D((D)) --- E((E));
` 
const {svg} = await mermaidAPI.render("graphDiv", graphDefinition); el.innerHTML = svg;
```
