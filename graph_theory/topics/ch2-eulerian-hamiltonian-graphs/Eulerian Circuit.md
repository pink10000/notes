---
tags:
  - MATH_154
aliases:
  - Eulerian
  - Semi-Eulerian
---
# Bridges of Konisberg 
This is essentially the origins of graph theory. The map is decomposed to the following graph:
```tikz
\begin{document}
\begin{tikzpicture}
    % Define coordinates for the land masses
    \coordinate (A) at (0,1);
    \coordinate (B) at (0,0);
    \coordinate (C) at (0,-1);
    \coordinate (D) at (4,0);

    % Draw the land masses as filled circles
    \node[draw, circle] at (A) (L1) {A};
    \node[draw, circle] at (B) (L2) {B};
    \node[draw, circle] at (C) (L3) {C};
    \node[draw, circle] at (D) (L4) {D};

    % Draw the bridges
    % Bridge 1: A to B
    \draw[line width=1pt, bend right=20] (L1) to (L2);
    % Bridge 2: A to B (another one)
    \draw[line width=1pt, bend left=20] (L1) to (L2);
	
	% Bridge 3: A to D
	\draw[line width=1pt] (L1) to (L4);

    % Bridge 4: B to C (two bridges)
    \draw[line width=1pt, bend left=20] (L2) to (L3);
    \draw[line width=1pt, bend right=20] (L2) to (L3);

    % Bridge 5: B to D
    \draw[line width=1pt] (L2) -- (L4);

    % Bridge 6: C to D
    \draw[line width=1pt] (L3) -- (L4);
\end{tikzpicture}
\end{document}
```
Is there a [[Walk#Definition (Trail)|trail]] that visits each edge once? 

# Definition (Eulerian Graph)
A [[Graph]] $G$ is called **Eulerian** if it contains a [[Walk#Definition (Circuit)|circuit]] that visits each edge of $G$ once. That circuit is called an **Eulerian Circuit**. 

If we are talking about a trail, then the graph is called **Semi-Eulerian** and the trail is called an **Eulerian Trail**. 

## Observations On Eulerian Graphs
- We note that if $G$ is Eulerian/Semi-Eulerian, it must be [[Connectivity|connected]] since there is no way to move between two connected components.  
- In any circuit, if you enter a vertex, you must also leave it. For some vertex $v$, and edge that visits $v$ must have some edge that exits. In particular, each edge must come in *pairs*. Thus, if $G$ is Eulerian, then $\deg(v)$ must be even $\forall v \in V(G)$.
	- So, in the [[#Bridges of Konisberg]], we this graph cannot possibly be Eulerian, since $\deg(D)$ is odd. 