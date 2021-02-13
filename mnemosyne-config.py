# Mnemosyne configuration file.

# This file contains settings which we deem to be too specialised to be
# accesible from the GUI. However, if you use some of these settings, feel
# free to inform the developers so that it can be re-evaluated if these
# settings need to be exposed in the GUI.

# Science server. Only change when prompted by the developers.
science_server = "mnemosyne-proj.dyndns.org:80"

# Set to True to prevent you from accidentally revealing the answer when
# clicking the edit button.
only_editable_when_answer_shown = False

# Set to False if you don't want the tag names to be shown in the review
# window.
show_tags_during_review = True

# The number of daily backups to keep. Set to -1 for no limit.
backups_to_keep = 10

# Start the card browser with the last used colum sort. Can have a serious
# performance penalty for large databases.
start_card_browser_sorted = False

# The moment the new day starts. Defaults to 3 am. Could be useful to change
# if you are a night bird. You can only set the hours, not minutes, and
# midnight corresponds to 0.
day_starts_at = 3

# On mobile clients with slow SD cards copying a large database for the backup
# before sync can take longer than the sync itself, so we offer reckless users
# the possibility to skip this.
backup_before_sync = True

# Latex preamble. Note that for the pre- and postamble you need to use double
# slashes instead of single slashes here, to have them escaped when Python
# reads them in.
latex_preamble = r"""
\documentclass[12pt]{article}
\usepackage{geometry}
\geometry{paperwidth=2.0\paperwidth} %make the page twice as wide for big ass bussproofs
\usepackage{a4wide}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage[bbgreekl]{mathbbol}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{stmaryrd} 
\usepackage{mathpartir}
\usepackage{mathtools}
\usepackage{bussproofs}
\usepackage{tikz}
\usepackage{stackengine}
\usepackage{diagrams}
\usepackage{multicol}
\usepackage{listings}% http://ctan.org/pkg/listings
\lstset{
  basicstyle=\ttfamily,
  mathescape,
  numbers=left
}
\usetikzlibrary{cd}

\newcommand{\inconsist}{\mathrel{\substack{\smile \\ \frown}}}
\newcommand{\consist}{\mathrel{\substack{\frown \\ \smile}}}

\newcommand{\boxto}{~\fbox{\to}~}
\newcommand{\lpar}{~\raisebox{1.2ex}{\rotatebox{180}{\&}}~}
\newcommand{\upand}{~\raisebox{1.2ex}{\rotatebox{180}{\&}}~}
\newcommand{\drto}{~\raisebox{1.2ex}{\rotatebox{-45}{$\to$}}~}
\newcommand{\with}{~\&~}
\newcommand{\boxarrow}{~\raisebox{0.5ex}{\fbox{\scriptsize{\to}}}~}
\newcommand{\relto}{- \! \! \! \mapsto}
\newcommand{\bimpl}[2]{
\mprset{fraction={===}}
\inferrule{#1}{#2 }
}

\newcommand{\slangle}{\scalebox{0.5}{$\langle~$}}
\newcommand{\srangle}{\scalebox{0.5}{$~\rangle$}}
\newcommand{\chan}{~\stackinset{l}{.5ex}{c}{}{\scalebox{0.6}{$\circ$}}{$\to$}~}
\newcommand{\dotto}{~\stackinset{l}{}{c}{}{$\bullet$}{$\to$}~}
\newcommand{\antiphi}{~\stackinset{l}{}{c}{}{$\backslash$}{$o$}~}
\newcommand{\absepi}{~\stackinset{r}{}{c}{}{\scalebox{0.5}{$\triangleright$}}{$-$}~}
\newcommand{\absmono}{\mapsto}

\newcommand{\vrt}[2]{
\pile{
#1 \\
\downarrow \\
#2
}
}

\newcommand{\ddisp}[3]{
\left(
\scriptsize
\begin{tikzcd}
#1 \ar[d, "\footnotesize{#2}"] \\
#3
\end{tikzcd}
\normalsize
\right)
}

\newcommand{\xdisp}[4]{
\left(
\scriptsize
\begin{tikzcd}
#1 \ar[d, "\footnotesize{#3}", #2] \\
#4
\end{tikzcd}
\normalsize
\right)
}

\newcommand{\disp}[3]{
\left(
\tiny
\begin{array}{l}
#1 \\
\downarrow #2 \\
#3
\end{array}
\normalsize
\right)
}

\newcommand{\colimit}[2]{\underset{\overset{\longrightarrow}{#1}}{\text{lim}}~#2}
\newcommand{\limit}[2]{\underset{\overset{\longleftarrow}{#1}}{\text{lim}}~#2}
\newcommand{\sem}[1]{\llbracket #1 \rrbracket}
\newcommand{\mbf}[1]{\mathbf{#1}}
\pagestyle{empty}
\begin{document}"""

# Latex postamble.
latex_postamble = r"""\end{document}"""

# Latex command.
latex = "pdflatex --shell-escape -interaction=nonstopmode"

# Latex dvipng command.
dvipng = "mnemosyne.bat"
#dvipng = "convert -trim -density 136 -colorspace rgb tmp.pdf tmp1.png"

# Latex command.
#latex = "pdflatex --shell-escape -interaction=nonstopmode"
#latex = "latex -interaction=nonstopmode"

# Latex dvipng command.
#dvipng = "mnemosyne.bat"
#dvipng = "dvipng -D 136 -T tight tmp.dvi" #& convert tmp1.png -transparent white tmp2.png & del tmp1.png & rename tmp2.png tmp1.png" #maybe use a batch which calls convert to change white to transparent
