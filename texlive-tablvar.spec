%global tl_name tablvar
%global tl_revision 72007

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Typesetting pretty tables of signs and variations according to French usage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tablvar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablvar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablvar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablvar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a complete and easy-to-use package for typesetting pretty tables
of signs and variations according to French usage. The syntax is similar
to that of the array environment and uses intuitive position commands.
Arrows are automatically drawn (with PSTricks or TikZ). Macros are
provided for drawing double bars, single bars crossing zero values,
intervals where the function is not defined, or for placing special
values. Many features of variations tables can be customized.

