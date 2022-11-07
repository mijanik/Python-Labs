replace_dict = {
    " i ": " oraz ",
    "oraz": "i",
    "nigdy": "prawie nigdy",
    "dlaczego": "czemu"
}
# rozdzielenie stringa na osobne slowa
def main():
    infile = "text\\plik_testowy.txt"
    outfile = "text\\nowy_plik.txt"
    delete_list = ["oraz", "nigdy", "dlaczego", " i "]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, str(replace_dict[word]))
            fout.write(line)


if __name__ == "__main__":
    main()