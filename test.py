import spacy
nlp = spacy.load('en_core_web_md')

print("Enter one")
word = input()
word=word.split(' ')
word=[word[0]]
liss = ["hello",
    "addemail",
    "addb_day",
    "addaddress",
    "add",
    "congrat",
    "change",
    "phone",
    "showall",
    "search",
    "deladdress",
    "delphone",
    "delb_day",
    "delemail",
    "delcontact",
    "close",
    "goodbye",
    "exit",
    "help",
]
liss=' '.join(liss+word)
tokens=nlp(liss)
fin={}
x=1
if(tokens[-1] and tokens[-1].vector_norm):
    for token2 in tokens:
        if(token2 and token2.vector_norm):
            if x==22:
                break
            try:
                token1 = tokens[-1]
                b=token1.similarity(token2)
                fin[token2]=b
                x+=1
            except IndexError:
                break
fin={k: v for k, v in sorted(fin.items(), key=lambda item: item[1])}
  
print(f"Similarity: {fin}")