
output/figures/figure_1.png: data/benefits.json
	python src/barplot.py -i data/benefits.json -x "potential benefits" -y "number of votes" -o output/figures/figure_1.png

figures : output/figures/figure_1.png