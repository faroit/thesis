.PHONY: thesis preview clean cleanall

all: thesis.pdf

preview: thesis.pdf
	open $< &

clean:
	latexmk -CA

cleanall: clean
	- rm -f *.pdf

icassp2016.pdf: thesis.tex
	latexmk -pdf -pdflatex="pdflatex -interactive=nonstopmode" --synctex=1 -use-make thesis.tex

# figures/boxplot.pdf:
# 	python data/make_boxplot.py data/all.pickle $@
#
# figures/iterations.pdf:
# 	python data/make_sdriteration.py data/all.pickle $@
#
# figures/gridplot.pdf:
# 	python data/make_gridplots.py
