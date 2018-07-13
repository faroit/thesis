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
ext-tikz/ClassicThesis-figure8.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure8" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure8.pdf: ext-tikz/ClassicThesis-figure8.md5
ext-tikz/ClassicThesis-figure9.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure9" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure9.pdf: ext-tikz/ClassicThesis-figure9.md5
ext-tikz/ClassicThesis-figure10.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure10" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure10.pdf: ext-tikz/ClassicThesis-figure10.md5
ext-tikz/ClassicThesis-figure11.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure11" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure11.pdf: ext-tikz/ClassicThesis-figure11.md5
ext-tikz/ClassicThesis-figure12.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure12" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure12.pdf: ext-tikz/ClassicThesis-figure12.md5
ext-tikz/ClassicThesis-figure13.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure13" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure13.pdf: ext-tikz/ClassicThesis-figure13.md5
ext-tikz/ClassicThesis-figure14.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure14" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure14.pdf: ext-tikz/ClassicThesis-figure14.md5
ext-tikz/ClassicThesis-figure15.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure15" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure15.pdf: ext-tikz/ClassicThesis-figure15.md5
ext-tikz/ClassicThesis-figure16.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure16" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure16.pdf: ext-tikz/ClassicThesis-figure16.md5
ext-tikz/ClassicThesis-figure17.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure17" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure17.pdf: ext-tikz/ClassicThesis-figure17.md5
ext-tikz/ClassicThesis-figure18.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure18" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure18.pdf: ext-tikz/ClassicThesis-figure18.md5
ext-tikz/ClassicThesis-figure19.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure19" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure19.pdf: ext-tikz/ClassicThesis-figure19.md5
ext-tikz/ClassicThesis-figure20.pdf: 
	pdflatex -shell-escape -halt-on-error -interaction=batchmode -jobname "ext-tikz/ClassicThesis-figure20" "\def\tikzexternalrealjob{ClassicThesis}\input{ClassicThesis}"

ext-tikz/ClassicThesis-figure20.pdf: ext-tikz/ClassicThesis-figure20.md5
