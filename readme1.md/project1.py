# here in this project we want to load a story and changes some words according to users
# firstly load file according to path as f , with = taaki f.close ki need na pade 
with open("d:\\python_practice\\alien.txt","r") as f:
    # reading mode mein daal di story 
    story = f.read()
    # print(story)
    
    
    
    # now convert into set it is helpful to remove duplicate
    words = set()
    # suppose starting word is not in story so we set -1 by default 
    start_word = -1
    # target is [] here suppose [ is start point of target and ] is end point of target 
    target_start = "["
    target_end = "]"
    # now we are using a loop enumeration on story where we check the element with targetif target found then start point is i 
    for i ,char in enumerate(story):
        if char == target_start:
            start_word = i
            # another case if target reaches to end point and start point is not -1 at that stage 
        if char== target_end and start_word!=-1:
            # now slicing from start word to last index of word it is because we want to eliminate taht word from story and add it to the set 
            word = story[start_word:i+1] 
            words.add(word)
            # for further check we use start word is -1 again 
            start_word = -1
            # print those words in set 
    print(words) 
    
    
    
    # suppose ther is a dict named answers 
    answers = {}  
    # loop over the eliminating words and ask the user for input     
    for word in words:
        # input by users 
        answer =input("enter the word for "+ word + ":") 
        # add there input in dict with specific indices
        answers[word] = answer
#
# 
# 
#  again loop in words because our main motto is to replace all words with the user's input 
    for word in words:
        # replace all words with new one in story 
        story.replace(word,answers[word])
        # at last print story with the user input 
    print(story)        





