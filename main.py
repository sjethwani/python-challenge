
import os
import csv

f = open('paragraph.txt','r')
message = f.read()

#print(message)

sentences = []
letters = 0
avg_word_length = 0

avg_sentence_length = 0

words = message.split(" ")
sentences = message.split(".")

for word in words:
    letters = letters+len(word)
    
    
avg_word_length = int(letters)/(len(words)+1)
avg_sentence_length = (len(words)+1)/(len(sentences)-1)



print("Paragraph Analysis")
print("------------------")
print ("Approximate Word Count " + str(len(words)+1))
print ("Approximate Sentence Count " + str(len(sentences)-1))
print ("Average letters in a word " + str(avg_word_length))
print("Average words in a sentence " + str(avg_sentence_length))

f = open('PyParagraph.txt','w')
f.write("Paragraph Analysis\n")
f.write("------------------\n")
f.write("Approximate Word Count " + str(len(words)+1) + "\n")
f.write("Approximate Sentence Count " + str(len(sentences)-1)+"\n")
f.write("Average letters in a word " + str(avg_word_length)+"\n")
f.write("Average words in a sentence " + str(avg_sentence_length)+"\n")
f.close()

