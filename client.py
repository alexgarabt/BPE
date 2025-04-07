from sys import argv
from tokenizer import BPETokenizer

def iteration_progress(**kwargs):
    i = kwargs["i"]
    k = kwargs["k"]

    #dictionary = kwargs["D"]
    #vocabulary = kwargs["V"]

    # Print the % of the way
    if(i % 100 == 0):
        percentage = (i / k) * 100
        print(f"{percentage}%", end=", ...", flush=True)

if __name__ == "__main__": 
    filename = argv[1]
    new_eow = "_"
    print(f"Learning token vocabulary from: {filename}")
    num_tokens = int(input("\nEnter number of tokens to learn (k) = "))
    with open(filename, "r", encoding="utf-8") as f:
        corpus = f.read()

    print("\nLearning tokens", end=": ...")
    tokenizer = BPETokenizer(corpus, t_vocabulary_size=num_tokens ,learn_callback=iteration_progress)
    print(f"\nVocabulary length = {len(tokenizer.V)}\n")

    show_v = input("Want to display the learned token vocabulary? [Y/N]: ")
    if show_v.upper() == "Y":
        tokens = [token.replace(BPETokenizer.EOW, new_eow) for token in list(tokenizer.V)]
        print("\nVOCABULARY:\n\n" + str(tokens) + "\n") # print the learned vocabulary

    while True:
        print("\n-----------")
        sentence = input("Tokenize sentence => ")
        tokens = tokenizer.segment_string(sentence)
        tokens = [token.replace(BPETokenizer.EOW, new_eow) for token in tokens]
        print("\nTokens =>\n" + str(tokens))
        print("-----------\n")
