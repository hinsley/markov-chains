#!/usr/bin/env python3

import fileinput
import markov
import random

class TextGenerator(object):
    def trainText(self, source_text):
        self._markov_chain = markov.MarkovChain()
        self._source_text = source_text

        words = source_text.lower().split() + [None]
        length = len(words) - 1

        i = 0
        while i < length:
            a = words[i]
            b = words[i + 1]

            weight = self._markov_chain.getNode(a, b)

            if weight == None:
                weight = 0
            elif b == None:
                weight = 1
            
            self._markov_chain.setNode(a, b, weight + 1)

            i += 1

    def generateText(self):
        current_word = random.choice([word for word in self._markov_chain.getNode()])
        self._markov_chain.setState(current_word)

        text = [current_word]

        while True:
            self._markov_chain.nextNode()
            current_word = self._markov_chain.getState()

            if current_word == None:
                return ' '.join(text)
            else:
                text.append(current_word)

if __name__ == "__main__":
    tg = TextGenerator()

    input_text = ""
    for line in fileinput.input():
        input_text += line
    tg.trainText(input_text)

    print(tg.generateText())
