import tkinter as tk
root = tk.Tk()
root.title('25-26プレミアリーグ順位確認アプリ')
root.geometry('420x280')
root.resizable(False,False)
root.configure(bg="#edecf1")
label = tk.Label(root, text='チーム名を入力してください')
label.pack()
entry = tk.Entry(root)
entry.pack()
def search():
    team_name = entry.get()
    if team_name in teams:
            result_label.config(text=f'{team_name}の最終順位は{teams[team_name]}位です')
    else:
            result_label.config(text='そのチームは存在しません。正しい日本語で入力してください')
button = tk.Button(root, text='検索', command=search)
button.pack()
result_label = tk.Label(root, text='')
result_label.pack()
teams = {'アーセナル':1,'マンチェスターシティ':2,'マンチェスターユナイテッド':3,'アストンヴィラ':4,'リヴァプール':5,'ボーンマス':6,'サンダーランド':7,'ブライトン':8,'ブレントフォード':9,'チェルシー':10,'フラム':11,'ニューカッスル':12,'エヴァートン':13,'リーズ':14,'クリスタルパレス':15,'ノッティンガムフォレスト':16,'トッテナム':17,'ウェストハム':18,'バーンリー':19,'ウルヴス':20}
#print('プレミアリーグ2025-2026シーズンの最終順位を表示します')
#is_team = True
#while is_team == True:
 #   team_name = input('チーム名を入力してください＜＜＜')
  #  if team_name in teams:
   #     print(f'{team_name}の最終順位は{teams[team_name]}位です')
    #else:
     #   print('そのチームは存在しません。正しい日本語で入力してください')
    #key=input('続けて順位を確認しますか？（はい/いいえ）')
    #if key == 'はい':
     #   is_team = True
    #elif key == 'いいえ':
     #   is_team = False
    #else:
     #   print('「はい」か「いいえ」で答えてください')
#print('ご利用ありがとうございました。')
root.mainloop()