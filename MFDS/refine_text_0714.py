# load libraries
import os 
import pandas as pd
import numpy as np

# change your directory
os.chdir(r'C:\Users\MI2RL-KHJ\mfds')


#####
# test.txt is original file 
criterias = []
descs = [] 

k = 0
f= open('test.txt', 'rt', encoding='UTF8')
for line in f.readlines():
    line = line.split(',')
    line = [i.strip() for i in line]

    fs = ','.join(line)        #fs = full sentence

    creteria = fs.split('\t')[0]
    try:
        desc = fs.split('\t')[1]
    # exception: 407:치과용도포기
    except:
        desc = fs
        print(k)
        print(fs)
    k += 1

    criterias.append(creteria)
    descs.append(desc)

# divide into two columns: product and description 
df = pd.DataFrame({'Product': criterias, 'Principle':descs})

# ndf: new dataframe  for prodouct, criteria, content, criteria_index, origial description
ndf = pd.DataFrame(columns = ('product', 'criteria', 'content', 'criteria_index','full_content'))#, index = 'num')

k = 0
p = 0
t = 0
processed = []

for i in range(len(df)):
    prod = df.iloc[i,[0]] 
    prin = df.iloc[i,[1]]

    if '작용원리' in prin['Principle']:
        processed.append(i)
        p += 1
        pindex = prin['Principle'].find('작용원리')
        if not i in [130, 245]:
            if pindex < 20:
                try:
                    work = prin['Principle'].split('작용원리')[1].lstrip().replace('- 1 -','').rstrip()
                    #print('1:',work)
                    tmp_criteria = '작용원리'
                    #print(len(work))
                    workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, pindex, prin['Principle'].lstrip() ]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
                    ndf = ndf.append(workdf)
                except:
                    work = prin['Principle'].lstrip().replace('- 1 -','').rstrip()
                    tmp_criteria = '작용원리'
                    workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, pindex, prin['Principle'].lstrip() ]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
                    ndf = ndf.append(workdf)  
            else: 
                work =  prin['Principle'].lstrip().replace('- 1 -','').rstrip()
                workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, pindex, prin['Principle'].lstrip() ]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
                ndf = ndf.append(workdf)  
        else: 
            work = prin['Principle'].split('작용원리')[2].lstrip().replace('- 1 -','').rstrip()
            tmp_criteria = '작용원리'
            workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, pindex, prin['Principle'].lstrip() ]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
            ndf = ndf.append(workdf) 
        
        
        
        
    elif '개요' in prin['Principle']:
        processed.append(i)
        k += 1
        kindex = prin['Principle'].find('개요')
        if kindex < 20:
            try: 
                intro = prin['Principle'].split('개요')[1].lstrip().replace('- 1 -','').rstrip()
                #print(intro)
                tmp_criteria = '개요'
                introdf = pd.DataFrame([[prod['Product'], tmp_criteria, intro, kindex, prin['Principle'].lstrip() ]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
                ndf = ndf.append(introdf)
            except:
                #print(prin['Principle'])
                intro = prin['Principle'].lstrip().replace('- 1 -','').rstrip()
                print(intro)
                tmp_criteria = '개요'
                introdf = pd.DataFrame([[prod['Product'], tmp_criteria, intro, kindex, prin['Principle'].lstrip() ]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
                ndf = ndf.append(introdf)
        else:
            intro =  prin['Principle'].lstrip().replace('- 1 -','').rstrip()
            introdf = pd.DataFrame([[prod['Product'], tmp_criteria, intro, kindex, prin['Principle'].lstrip() ]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
            ndf = ndf.append(introdf)            
            
    
    elif i in [187, 198, 256, 296, 311, 351, 407, 413, 420]:
        processed.append(i)
        tindex = prin['Principle'].find('작용 원리')
        t += 1
        if tindex < 20:
            try:
                work = prin['Principle'].split('작용 원리')[1].lstrip().replace('- 1 -','').rstrip()
                #print('1:',work)
                tmp_criteria = '작용원리'
                workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, tindex, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
                ndf = ndf.append(workdf)
            except:
                work = prin['Principle'].lstrip().replace('- 1 -','').rstrip()
                tmp_criteria = '작용원리'
                workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, tindex, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
                ndf = ndf.append(workdf)      
        else:
            work =  prin['Principle'].lstrip().replace('- 1 -','').rstrip()
            workdf = pd.DataFrame([[prod['Product'], tmp_criteria, work, tindex, prin['Principle'].lstrip()]], columns = ['product', 'criteria', 'content', 'criteria_index', 'full_content'], index = [i])
            ndf = ndf.append(workdf)                

print('k:{}, p:{}, t:{}'.format(k,p,t))



'''
/// extra processing /////
# detect exception
for i in range(len(df)):
    if not i in processed:
        print(i)
        print(df.loc[i])
        
# detect index exception
tmp = ndf[ndf['criteria_index'] > 10]
tmp

# contents including 'intro' + 'principle'
k = 0 
for i in range(len(ndf)):
    if '개요' in ndf['full_content'][i]:
        if '작용원리' in ndf['full_content'][i]:
            k += 1 
            print(ndf.loc[i])
print(k)     
 '''
