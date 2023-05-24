import pandas as pd


def Recommend_Songs(pred_class):
    df = pd.read_csv('Streamlit/songs_mood.csv')
    if( pred_class=='disgust' ):

        Play = df[df['mood'] =='Sad' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    

    elif( pred_class=='fear' or pred_class=='angry' ):

        Play = df[df['mood'] =='Calm' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)
        
    elif( pred_class=='surprise' or pred_class=='neutral' or pred_class =='rocrock' or pred_class == 'susurprise'):

        Play = df[df['mood'] =='Energetic' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    else:
        Play = df[df['mood'] =='Happy' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)


    song_lst = []
    for i in range(len(Play['id'])) :
        song_lst.append(Play['id'][i])
    return song_lst