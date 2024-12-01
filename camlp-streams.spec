%undefine _debugsource_packages

Name: camlp-streams
Version: 5.0.1
Release: 3
Source0: https://github.com/ocaml/camlp-streams/archive/refs/tags/v%{version}.tar.gz
Summary: The Stream and Genlex libraries for OCaml 5.0
URL: https://github.com/ocaml/camlp-streams
License: LGPL-2.1
Group: Development/Other
BuildRequires: ocaml-compiler

%description
The Stream and Genlex modules have been part of the OCaml standard library for
a long time, and have been distributed as part of the core OCaml system.
They have been removed from the OCaml standard library, but will be maintained
and distributed separately in this camlp-streams package.

%prep
%autosetup -p1

%build
cd src
ocamlc -g stream.mli
ocamlc -g stream.ml
ocamlc -g genlex.mli
ocamlc -g stream.cmo genlex.ml
ocamlc -o stream.cma -a stream.cmo
ocamlc -o genlex.cma -a genlex.cmo
ocamlopt -o stream.cmx -c stream.ml
ocamlopt -o genlex.cmx -c genlex.ml
ocamlopt -o stream.cmxa -a stream.cmx
ocamlopt -o genlex.cmxa -a genlex.cmx

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
mv src/* %{buildroot}%{_libdir}/ocaml

%files
%{_libdir}/ocaml/*
