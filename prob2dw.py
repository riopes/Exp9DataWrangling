import pandas as pd
data = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length', 'Width', 
        'Height','Length', 'Width','Height'],'Value':[6,4,2,5,3,4]}
messy = pd.DataFrame (data,columns=['Box','Dimension','Value'])

tidy = messy.pivot_table(index=['Box'],columns = 'Dimension',values = 
                         'Value').reset_index()
print ('Tidy Dataset:\n',tidy)

volume = tidy['Volume']=tidy.Length*tidy.Height*tidy.Width

print ('\nTidy Dataset with Volume column:',tidy)