import art
print(art.logo)

rerun=True
while rerun:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def caesar(text,shift,direction):
        output=""
        for letter in text:
            if letter in alphabet:
                if direction=="encode":
                    output+=alphabet[(alphabet.index(letter)+shift)%26]
                elif direction=="decode":
                    output+=alphabet[(alphabet.index(letter)-shift)%26]
            else:
                output+=letter
        print("--------------------------------------------")
        print(f"The {direction}d text is {output}")
        print("--------------------------------------------")

    caesar(text,shift,direction)
    state=input("Type yes if you want to go Again. otherwise type no\n").lower()
    if state=="yes":
        rerun=True
    else:
        rerun = False
        print("GoodBye")



