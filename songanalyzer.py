"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #10 - Song Analyzer (songanalyzer.py)


Author: Carter Berlind

Difficulty Level: 5/10

Prompt: Freddy is trying to write a song to impress his friends but needs help 
checking his lines. He decides to enlist you, a python programmer, to create a 
program to see if his lines are good. He tells you that he wants his lines to 
be judged off of whether they rhyme and how much alliteration is there.

Create a program in which the user can input a sentence and the program will 
report back how many words start with the same letters and what those letters 
are and how many words end in the same last three letters (If a word is less 
than three letters we do not consider its rhymes). 

Constraints: Words must be separated by a space. Only report if letters occur at the 
beginning of words multiple times. Don’t worry about commas and punctuation.

Test Cases:
Input: “carter is cool and not a fool”;                     Output: ”c=2,a=2, 2 rhyming words”
Input: “running jumping and swimming are really fun”;       Output: ”r=2, a=2, 3 rhyming words"
Input: “a ban on that book”;                                Output: ”b=2, 0 rhyming words”
Input: “good food for nice mice”;                           Output: ”f=2, 4 rhyming words”
Input: “howdy rowdy hikers hope you have a great time”;     Output: "h=4, 2 rhyming words”
"""

class Solution:
    def song_analyze(self,lyric):
        # type lyric: string
        # return: string 
        
        # TODO: Write code below to return a string with the solution to the prompt
        letter_count = {}
        for word in lyric.split(" "):
            character = word[0]
            if character != "" and character not in letter_count:
                letter_count[character] = 1
            else:
                letter_count[character] += 1
        rhyming_words = {}
        for word in lyric.split(" "):
            last = word[-3:]
            if last not in rhyming_words:
                rhyming_words[last] = 1
            else:
                rhyming_words[last] += 1
        
        to_ret = ""
        for key in letter_count.keys():
            if letter_count[key] > 1:
                to_ret += str(key) + "=" + str(letter_count[key]) + ", "
        rhyme_total = 0
        for key in rhyming_words.keys():
            if rhyming_words[key] > 1:
                rhyme_total += rhyming_words[key]
        to_ret += str(rhyme_total) + " rhyming words"
        return to_ret
def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.song_analyze(string1)
    print(ans)

if __name__ == "__main__":
    main()