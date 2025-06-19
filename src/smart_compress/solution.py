def accumulate(word_rep,n_word):
    result=""
    if n_word > 2:
        result = word_rep+str(n_word)
    else:
         result = word_rep*n_word
    return result


def chain_compress(word):
    new_word=""
    accum=""
    n_word=1
    for i in range(len(word)): 
        if i <(len(word)-1):
            if word[i] == word [i+1]:
                n_word+=1
            else:
                word_rep=word[i]
                accum=accumulate(word_rep,n_word)
                n_word=1
                new_word=new_word + accum  
        else:
            word_rep=word[i]
            accum=accumulate(word_rep,n_word)
            new_word=new_word + accum  
        
    return new_word
