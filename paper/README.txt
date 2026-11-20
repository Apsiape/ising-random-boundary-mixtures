Every phase mixture recurs: The planar Ising model with random boundary spins
Seth Douglas and Nidhal Mghirbi
Version 2.0.0, November 2026

abstract.txt contains the abstract in plain text. main.pdf is the compiled preprint.
The source consists of main.tex, sections/ and references.tex.

From this directory run:
    python -I build.py

The driver uses pdfLaTeX without shell escape or automatic package installation,
waits for reference files to stabilize, and rejects every final warning,
unresolved reference, missing character, overfull box or underfull box.
Build intermediates are placed in .build/; only the clean PDF is copied here.
A pre-existing MiKTeX installation with the packages in main.tex is required.
No external figures or bibliography processor are needed.
