# Text generator based on machine learning
# text="the man was ...they...then...the...then...the dog "

# X is the sequence of 'k=3' and Y is predicted character and k+1 will be the character.



# Down below is the transition table.
# x       y     fq
# the    " "     3
# he_     m      1
# e m     a      1
#  ma     n      1
# the     y      1
# the     n      2



"""def generate_table(data,k=1):
    """"""this function generates a transition table by giving frequency""""""
    T={}
    for i in range(len(data)-k):
        x=data[i:i+k]
        y=data[i+k]

        if T.get(x) is None:
            T[x]={}
            T[x][y]=1
        else:
            if T[x].get(y) is None:
                T[x][y]=1
            else:
                T[x][y]+=1
    return T
T=generate_table("hii hello how are you what you are doing is the")
# print(T)

def fq_2_probab(T):
    """"""this function returns probability of frequency from the transition table""""""
    for kx in T.keys():
        s=sum(T[kx].values())
        for k in T[kx].keys():
            T[kx][k]=T[kx][k]/s
    return T

t=fq_2_probab(T)
# print(t)

# Data reading
def read_data(filepath):
    with open(filepath) as f:
        return f.read().lower()
text=read_data("data.txt")
# print(text)


# Training the marchov chain model

def train_model(text,k=1):
    T=generate_table(text,k)
    T=fq_2_probab(T)

    return T

model=train_model(text)
# print(t)

# Generate text
import random

def text_generate(Context,T,k):
    """"""Final model"""""""
    Context = Context[-k:]
    if T.get(Context) is None:
        return " "
    possible_chars=list(T.get(Context).keys())
    possible_probab=list(T.get(Context).values())
    return random.choices(possible_chars,weights=possible_probab)[0]


text_generate("The ",model,k=1)

def generate_text(starting_sent,T,k=1,max_len=100):
    sentence=starting_sent
    context=starting_sent[-k:]

    for i in range(max_len):
        next_pred=text_generate(context,T,k)
        sentence+=next_pred
        context=sentence[-k:]
    return sentence
print(generate_text("India",model,k=4,max_len=100))"""






