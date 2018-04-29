thesis.pdf: Bibliography.bib ClassicThesis.tex classicthesis-config.tex Chapters/*.tex FrontBackmatter/*.tex
	pdflatex -shell-escape ClassicThesis
	bibtex ClassicThesis
	pdflatex -shell-escape ClassicThesis
	pdflatex -shell-escape ClassicThesis --synctex=1

partial:
	bibtex thesis
	pdflatex -shell-escape thesis --synctex=1

clean:
	rm -f *.lot *.lof *.lol *.toc *.log *.out *.aux *.blg *.bbl thesis.pdf Chapters/*.aux Chapters/**/*.aux frontback/*.aux

rebuild: clean thesis.pdf
