#1.සංඛ්‍යා දෙකක් පරාමිති ලෙස ලබාගෙන එම සංඛ්‍යා දෙකම බෙදිය හැකි සංඛ්‍යා ලයිස්තුවක් ප්‍රත්‍යාගමනය කිරීමට ශ්‍රිතය ගොඩනගන්න.

def cf(a, b):
    return [d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0]


#2.එක් සංඛ්‍යාවක් පරාමිතියක් ලෙස ලබාගෙන එම සංඛාව ඉතිරි නැතිව බෙදිය හැකි කුඩාම සංඛ්‍යාව ප්‍රත්‍යාගමනය කිරීමට ශ්‍රිතය ගොඩනගන්න.

def sf(x):
    return ([y for y in range(1, x) if x % y == 0])[0]
