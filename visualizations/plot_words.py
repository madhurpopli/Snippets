%matplotlib inline
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
tags = ''
for index, row in df.iterrows():
    tags = tags + ' ' + row['Tag']
    
stopwords = set(STOPWORDS)
wordcloud_tac_repro = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = stopwords, 
                min_font_size = 10).generate(tags) 
             
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud_tac_repro) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()
