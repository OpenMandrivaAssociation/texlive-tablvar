Name:		texlive-tablvar
Version:	69212
Release:	1
Summary:	Typesetting pretty tables of signs and variations according to French usage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tablvar
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablvar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablvar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablvar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a complete and easy-to-use package for typesetting
pretty tables of signs and variations according to French
usage. The syntax is similar to that of the array environment
and uses intuitive position commands. Arrows are drawn
automatically (using PSTricks by default or TikZ as an option).
Macros are provided for drawing twin bars, single bars crossing
the zeros, areas where the function is not defined, or placing
special values. Several features of the variation tables can be
customized.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tablvar
%{_texmfdistdir}/tex/latex/tablvar
%doc %{_texmfdistdir}/doc/latex/tablvar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
