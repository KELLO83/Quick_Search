import pandas as pd

def filter_run(productname, dataframe):
    
    #result_df = {}
    data = pd.DataFrame(columns=['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class', 'name'])
    print("filter 실행중 productname검사 : {}".format(productname))
    for i in range(len(dataframe)):
        buffer = dataframe.iloc[i:i+1]
        
        for j in range(len(productname)):
            if(dataframe.iloc[i, 6] == productname[j]):
                data = pd.concat([data, buffer])
                break
            else:
                pass

    data = data.reset_index(drop=True)

    return data