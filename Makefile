all: build/mazurov-thesis.pdf

build/mazurov-thesis.pdf: mazurov-thesis.tex
	test -d build || mkdir build
	chktex mazurov-thesis.tex || exit
	cd build && rubber -d -s ../mazurov-thesis.tex || exit
	evince build/mazurov-thesis.pdf&

view: mazurov-thesis.pdf
	evince mazurov-thesis.pdf &

clean:
	rm -rf build
