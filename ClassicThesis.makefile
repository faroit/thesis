ALL_FIGURE_NAMES=$(shell cat ClassicThesis.figlist)
ALL_FIGURES=$(ALL_FIGURE_NAMES:%=%.pdf)

allimages: $(ALL_FIGURES)
	@echo All images exist now. Use make -B to re-generate them.

FORCEREMAKE:

include $(ALL_FIGURE_NAMES:%=%.dep)

%.dep:
	mkdir -p "$(dir $@)"
	touch "$@" # will be filled later.

ext-tikz/ClassicThesis-figure0.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure0" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure0.pdf: ext-tikz/ClassicThesis-figure0.md5
ext-tikz/ClassicThesis-figure1.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure1" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure1.pdf: ext-tikz/ClassicThesis-figure1.md5
ext-tikz/ClassicThesis-figure2.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure2" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure2.pdf: ext-tikz/ClassicThesis-figure2.md5
ext-tikz/ClassicThesis-figure3.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure3" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure3.pdf: ext-tikz/ClassicThesis-figure3.md5
ext-tikz/ClassicThesis-figure4.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure4" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure4.pdf: ext-tikz/ClassicThesis-figure4.md5
ext-tikz/ClassicThesis-figure5.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure5" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure5.pdf: ext-tikz/ClassicThesis-figure5.md5
ext-tikz/ClassicThesis-figure6.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure6" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure6.pdf: ext-tikz/ClassicThesis-figure6.md5
ext-tikz/ClassicThesis-figure7.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure7" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure7.pdf: ext-tikz/ClassicThesis-figure7.md5
