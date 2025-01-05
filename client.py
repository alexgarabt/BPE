from sys import argv
from tokenizer import BPETokenizer

def iteration_progress(**kwargs):
    i = kwargs["i"]
    k = kwargs["k"]
    # Print the % of the way
    if(i % 100 == 0):
        percentage = (i / k) * 100
        print(f"{percentage}%", end=", ...", flush=True)

if __name__ == "__main__": 
    filename = argv[1]
    print(f"Learning token vocabulary from: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        corpus = f.read()

    print("\nLearning tokens", end=": ...")
    tokenizer = BPETokenizer(corpus, t_vocabulary_size=500 ,learn_callback=iteration_progress)
    print(f"\nVocabulary length = {len(tokenizer.V)}\n")

    show_v = input("Want to display the learned token vocabulary? [Y/N]: ")
    if show_v.upper() == "Y":
        print("\nVOCABULARY:\n\n" + str(sorted(list(tokenizer.V))) + "\n") # print the learned vocabulary

    while True:
        print("\n-----------")
        sentence = input("Tokenize sentence => ")
        tokens = tokenizer.segment_string(sentence)
        print("\nTokens =>\n" + str(tokens))
        print("-----------\n")
