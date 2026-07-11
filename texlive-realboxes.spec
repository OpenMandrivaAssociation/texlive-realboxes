%global tl_name realboxes
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Variants of common box-commands that read their content as real box and not a...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/realboxes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses the author's package collectbox to define variants of
common box related macros which read the content as real box and not as
macro argument. This enables the use of verbatim or other special
material as part of this content. The provided macros have the same
names as the original versions but start with an upper-case letter
instead. The "long-form" macros, like \Makebox, can also be used as
environments, but not the "short-form" macros, like \Mbox. However,
normally the long form uses the short form anyway when no optional
arguments are used.

