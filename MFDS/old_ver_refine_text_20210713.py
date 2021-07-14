# load libraries
import os 
import pandas as pd
import numpy as np

# change your directory
os.chdir(r'C:\Users\MI2RL-KHJ\mfds')

# test.txt is original file 
creterias = []
descs = [] 

f= open('test.txt', 'rt', encoding='UTF8')
for line in f.readlines():
    line = line.split(',')
    line = [i.strip() for i in line]
    #print(line)
    
    #print(line)
    fs = ','.join(line)        #fs = full sentence
    #print(fs)
    
    creteria = fs.split('\t')[0]
    desc = fs.split('\t')[1]
    print(creteria)
    print(desc)
    
    creterias.append(creteria)
    descs.append(desc)
    

# divide into two columns: product and description 
df = pd.DataFrame({'Product': creterias, 'Principle':descs})


# ndf: new dataframe  for prodouct, criteria, content, origial description
ndf = pd.DataFrame(columns = ('product', 'criteria', 'content', 'full_content'))

k = 0
p = 0
t = 0

for i in range(len(df)):
    
    # prod: 품명 , prin: description(principle)
    prod = df.iloc[i,[0]] 
    prin = df.iloc[i,[1]]

     # including '작용원리' in description
    if '작용원리' in prin['Principle']:
        p += 1
        try:
            work = prin['Principle'].split('작용원리')[1].lstrip().replace('- 1 -','').rstrip()
            #print('1:',work)
            tmp_criteria = '작용원리'
            workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content','full_content'], index = [i])
            ndf = ndf.append(workdf)
        except:
            work = prin['Principle'].lstrip().replace('- 1 -','').rstrip()
            tmp_criteria = '작용원리'
            workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content','full_content'], index = [i])
            ndf = ndf.append(workdf)  
    
    # including '개요' in description
    elif '개요' in prin['Principle']:
        k += 1
        try: 
            intro = prin['Principle'].split('개요')[1].lstrip().replace('- 1 -','').rstrip()
            tmp_criteria = '개요'
            introdf = pd.DataFrame([[prod['Product'], tmp_criteria, intro, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content','full_content'], index = [i])
            ndf = ndf.append(introdf)
        except:
            intro = prin['Principle'].lstrip().replace('- 1 -','').rstrip()
            tmp_criteria = '개요'
            introdf = pd.DataFrame([[prod['Product'], tmp_criteria, intro, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content','full_content'], index = [i])
            ndf = ndf.append(introdf)      
    
    
    # extra index 
    elif i in [187, 198, 256, 296, 311, 351]:
        t += 1
        try:
            work = prin['Principle'].split('작용 원리')[1].lstrip().replace('- 1 -','').rstrip()
            #print('1:',work)
            tmp_criteria = '작용원리'
            workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content','full_content'], index = [i])
            ndf = ndf.append(workdf)
        except:
            work = prin['Principle'].lstrip().replace('- 1 -','').rstrip()
            tmp_criteria = '작용원리'
            workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content','full_content'], index = [i])
            ndf = ndf.append(workdf)      

# chcek the number of data lists
print('k:{}, p:{}, t:{}'.format(k,p,t))




