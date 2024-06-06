import re
t = "It is sometimes said that a sentence expresses a complete thought, " \
    "This is a notional definition: it defines a term by the notion or idea it conveys.." \
    " The difficulty with this definition lies in fixing what is meant by a 'complete thought."
x = re.findall("it", t)
print(len(x))
