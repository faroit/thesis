.PHONY: paper preview clean cleanall

all: figures/boxplot.pdf figures/iterations.pdf icassp2016.pdf

preview: icassp2016.pdf
	open $< &

clean:
	latexmk -CA

cleanall: clean
	- rm -f *.pdf
	- rm -f figures/boxplot.pdf figures/iterations.pdf

icassp2016.pdf: icassp2016.tex 1_introduction.tex 2_model.tex 3_experiments.tex 4_conclusion.tex
	latexmk -pdf -pdflatex="pdflatex -interactive=nonstopmode" --synctex=1 -use-make icassp2016.tex

figures/boxplot.pdf:
	python data/make_boxplot.py data/all.pickle $@

figures/iterations.pdf:
	python data/make_sdriteration.py data/all.pickle $@

figures/gridplot.pdf:
	python data/make_gridplots.py
