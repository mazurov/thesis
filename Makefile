all: view

build/mazurov-thesis.pdf: mazurov-thesis.rst
	test -d build || mkdir build
	bin/thesis2latex.py mazurov-thesis.rst build/mazurov-thesis.tex || exit
	# rst2latex mazurov-thesis.rst build/mazurov-thesis.tex || exit
	cd build && pdflatex mazurov-thesis  || exit

view: build/mazurov-thesis.pdf
	evince build/mazurov-thesis.pdf &

regen:
	cd build && pdflatex mazurov-thesis  || exit

clean:
	rm -rf build