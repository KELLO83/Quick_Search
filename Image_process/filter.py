import pandas as pd

def filter_run(productname:str, dataframe):
    
    #result_df = {}
    data = pd.DataFrame(columns=['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class', 'name'])

    for i in range(len(dataframe)):
        buffer = dataframe.iloc[i:i+1]

        if(dataframe.iloc[i, 6] == productname):
            data = pd.concat([data, buffer])
        else:
            pass

    data = data.reset_index(drop=True)

    return data