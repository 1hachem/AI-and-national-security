import argparse

import matplotlib.pyplot as plt
import seaborn as sns

from utils.utils import read_json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input data", required=True)
    parser.add_argument("-x", "--xlabel", help="x axis label", required=True)
    parser.add_argument("-y", "--ylabel", help="y axis label", required=True)
    parser.add_argument("-o", "--output", help="output file", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    data = read_json(args.input)
    # plot and save plot
    sns.barplot(y=list(data.keys()), x=list(data.values()),
                palette="Blues_d", orientation='horizontal')
    plt.xticks(rotation=90)
    plt.ylabel(args.xlabel)
    plt.xlabel(args.ylabel)
    plt.tight_layout()
    plt.savefig(args.output)


if __name__ == "__main__":
    main()
