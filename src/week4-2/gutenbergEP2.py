from nltk.corpus import gutenberg
from nltk.probability import *

# **********************************************************************
#   Resource u'corpora/gutenberg' not found.  Please use the NLTK
#   Downloader to obtain the resource:  >>> nltk.download()
#   Searched in:
#     - '/Users/muzilan/nltk_data'
#     - '/usr/share/nltk_data'
#     - '/usr/local/share/nltk_data'
#     - '/usr/lib/nltk_data'
#     - '/usr/local/lib/nltk_data'
# ********************************************************************** nltk.download()

print gutenberg.fileids()
allwords = gutenberg.words('shakespeare-hamlet.txt')
fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])
print fd2.B()
print fd2.N()
fd2.tabulate(20)
fd2.plot(20)
fd2.plot(20, cumulative=True)
