def main():
    infile = "text\\plik_testowy.txt"
    outfile = "text\\nowy_plik.txt"
    delete_list = ["sie", " i", "i ", "oraz", "nigdy", "dlaczego"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, " ")
            fout.write(line)

if __name__ == "__main__":
    main()