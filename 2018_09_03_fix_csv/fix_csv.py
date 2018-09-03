import argparse
import csv


def main():
    description = "Turns a pipe-delimited file into a CSV file"
    p = argparse.ArgumentParser(description=description)
    p.add_argument("infile", help="Filepath for input file")
    p.add_argument("outfile", help="Filepath for output file")
    p.add_argument("--in-delimiter",
                   help="Input delimiter character")
    p.add_argument("--in-quote", help="CSV quote character")
    args = p.parse_args()

    rows = []
    delimiter = args.in_delimiter
    quotechar = args.in_quote
    if not delimiter or not quotechar:
        with open(args.infile, "r") as infile:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(infile.read())
            if not delimiter:
                delimiter = dialect.delimiter
            if not quotechar:
                quotechar = dialect.quotechar

    with open(args.infile, "r") as infile:
        rows = list(csv.reader(infile, delimiter=delimiter,
                               quotechar=quotechar))

    with open(args.outfile, "w") as outfile:
        writer = csv.writer(outfile)
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":
    main()
