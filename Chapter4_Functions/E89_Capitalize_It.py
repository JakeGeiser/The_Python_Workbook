import re

## function for capitalizing a collection of sentences correctly
# @params s : Input sentences as a string
def capitalize_it(s):
    # Capitalize the first word in each sentence
    sentences = re.split(r'([!?.]\s)',s)
    for i in range(0,len(sentences)):
        sentences[i] = sentences[i].capitalize()
    sentences = "".join(sentences)
    # Capitalize the pronoun "i" to be "I"
    sentences = sentences.split()
    for j in range(0,len(sentences)):
        if sentences[j] == 'i':
            sentences[j] = 'I'
    sentences = " ".join(sentences)
    return(sentences)

def main():
    my_input = "what time do i have to be there? what’s the address?"    
    print(capitalize_it(my_input))

if __name__ == "__main__":
    main()
