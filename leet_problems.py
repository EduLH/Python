# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:31:40 2022

@author: Du
"""
import collections
import unidecode


def non_maching_chars(str1, str2):
    col_str1 = collections.Counter(str1)
    col_str2 = collections.Counter(str2)
    missing_chars = []
    chars = sorted(set(str1 + str2))
    for char in chars:
        if col_str1[char] != col_str2[char]:
            missing_chars.append(char)
    return missing_chars


print(non_maching_chars("salve mano, bom dia! como vc ta?", "iae veio! to otimo e vc?"))


def conta_vogal_consoante(str1):
    clean_string = unidecode.unidecode(''.join(e for e in str1 if e.isalnum()))
    col_str1 = collections.Counter(clean_string)
    contador_vogal = col_str1['a']
    contador_vogal += col_str1['e']
    contador_vogal += col_str1['i']
    contador_vogal += col_str1['o']
    contador_vogal += col_str1['u']
    return {'vogal': contador_vogal, 'consoante': len(clean_string) - contador_vogal}


print(conta_vogal_consoante('qqqaaaaaááá'))


def anagram(word1, word2):
    return sorted(word1) == sorted(word2)


print(anagram('amor', 'roma'))


def count_char_on_string(word, letter):
    return collections.Counter(word)[letter]


print(count_char_on_string("iae galerinha hj tamo aqui pra falar da tecpix", 'a'))


def get_digits(someString):
    counter = 0
    for char in someString:
        if char.isdigit():
            counter += 1
    return counter


print(get_digits('tyuguhjhfjdsfyu89fyusgt438762d2376d370d6hj7f6hdfgb9dtxfnd'))


