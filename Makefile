all:
	test -d build || mkdir build
	chktex mazurov-thesis.tex || exit
	latexmk -pv -jobname=build/mazurov-thesis -pdf mazurov-thesis


view: mazurov-thesis.pdf
	evince mazurov-thesis.pdf &

clean:
	rm -rf build