# Separation and Count Estimation for Audio Sources Overlapping in Time and Frequency
Ph.D. Thesis from Fabian-Robert Stöter

## References

* `references.bib`: Main references of all cited works. This will be rendered in the last chapter of the thesis.
* `ownref.bib`: References where I am the main/first author. This will be rendered in the introduction and also appear in references at the end of the thesis.
* `ownsideref.bib`: References where I am __not__ the main/first author. This will be rendered in the introduction and also appear in references at the end of the thesis.
* `owndata.bib`: Data and Software References where I am the main author. This will be rendered in the introduction and also appear in references at the end of the thesis.

## Create PDF

### Requirements

TexLive 2019

### Build Document

Run `make`.

### Create diff using git-latex diff

due to bugs in the git-latex diff's flatten, we need to manually create a flattened latex file:

```bash
python latex-flatten.py ClassicThesis.tex thesis_original.tex
git checkout XXXXXX
python latex-flatten.py ClassicThesis.tex thesis_revisionXXXXXX.tex
latexdiff thesis_original.tex thesis_revisionXXXXXX.tex > diff.tex
make diff.pdf
```
