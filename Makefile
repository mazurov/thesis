all:
	test -d build || mkdir build
	chktex mazurov-thesis.tex || exit
	latexmk -pv -jobname=build/mazurov-thesis -pdf mazurov-thesis


view: build/mazurov-thesis.pdf
	evince build/mazurov-thesis.pdf &

clean:
	rm -rf build