
.PHONY: lint sort

output/figures/benefits.png: data/benefits.json src/barplot.py
	python src/barplot.py -i data/benefits.json -x "potential benefits" -y "number of votes" -o output/figures/benefits.png

output/figures/risks.png: data/risks.json src/barplot.py
	python src/barplot.py -i data/risks.json -x "potential risks" -y "number of votes" -o output/figures/risks.png

figures : output/figures/benefits.png output/figures/risks.png


lint:
	flake8 .

sort:
	isort .

all : sort lint