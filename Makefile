thesis.pdf: references.bib ClassicThesis.tex classicthesis-config.tex Chapters/*.tex FrontBackmatter/*.tex
	latexmk -recorder -pdf -pdflatex="pdflatex -interactive=batchmode" --synctex=1 -use-make ClassicThesis

clean:
	rm -f *.lot *.lof *.lol *.toc *.log *.out *.aux *.blg *.bbl thesis.pdf Chapters/*.aux Chapters/**/*.aux frontback/*.aux

rebuild: clean thesis.pdf
