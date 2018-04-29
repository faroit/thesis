% ICA 2013
% by Alireza Najaf-Yazdi
% McGill University
% 
% Licensed under the CC-GNU GPL version 2.0 or later.
% See http://creativecommons.org/licenses/GPL/2.0
% 
% See http://ankurdave.com/tex for more document classes.

\ProvidesClass{ica2013_2}

\LoadClass[11pt]{article}

% fields that user can set (in addition to title, author, etc)
\makeatletter
	\newcommand{\subtitle}[1]{\def \@subtitle {#1}}
	\newcommand{\subject}[1]{\def \@subject {#1}}
	\newcommand{\wordcount}[1]{\def \@wordcount {#1}}
        \newcommand{\affilation}[1]{\def \@affilation {#1}}
	\subtitle{}
	\subject{}
	\wordcount{}
	\affilation{}
\makeatother

% margins
\usepackage[top=1in,bottom=1in,left=1in,right=1in]{geometry}

% fonts
\usepackage{newcent}
\usepackage{fouriernc}
\renewcommand{\ttdefault}{cmtt}

% alignment
% (must be before indentation because raggedright clears parindent)
\raggedright

% indentation
\usepackage{indentfirst}
\setlength{\parindent}{18pt}
\setlength{\parskip}{3pt}

% spacing
\usepackage{setspace}

% references
\usepackage{varioref}

% figures
\usepackage[pdftex]{graphicx}

\usepackage[font=footnotesize,labelfont={bf,sc}]{caption}

\usepackage{titlesec, blindtext, color}
\newcommand\secformat[1]{%
\begin{center}
  \huge ~#1
\end{center}} 
\titleformat{\section}{\centering\bf\large\scshape}{}{12pt}{}
\titleformat{\subsection}{\centering\bf\large}{}{12pt}{}
\titleformat{\subsubsection}{\centering}{}{12pt}{}


% title
\makeatletter
\def \@maketitle {%
\begin{center}
%\includegraphics[width=\textwidth,angle=0]{template_04_bw.png}
\hrule
\vspace{14pt} % provide vertical space between section title and contents
		
}
\makeatother

%\thispagestyle{empty}
\pagestyle{empty}


