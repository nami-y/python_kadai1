
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
# 課題１：簡単な検索ツールの作成

#説明動画：https://youtu.be/fFaErYaPIdk

#この課題はif文などを使用してリストから特定要素を検索して取得するためのものです。
#この課題がクリアできれば主要構文であるif for list は習得できたといえるでしょう。

# 課題
#１．入力したキーワードで、キャラクターリスト(source)を検索して、存在すれば存在する旨を、存在しなければ存在しない旨をPrint文で表示してみましょう
#２．１に追加して結果が存在した場合と、しなかった場合で表示する文言が変わるようにしてみましょう
#３．２に追加して結果が存在しなかった場合に、キャラクターリスト(source)に追加できるようにしてみましょう
#４．３に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう
#５．４に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう


import csv
#import pprint  #表示を見やすくするため
import locale  #エンコードの指定

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅうろう","ぎゆう","げんや","かなお",]
with open('character_name.csv','r',encoding="utf-8") as f: #character_name.csvをｆという名称で置き換えて開く
    for row in csv.reader(f):
        print(f'{row}')
        #print(f'{type(row)}')


### 検索ツール
def search():   
    word = input("鬼滅の登場人物の名前をひらがなで入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in row:
    #print(word + 'はキャラクターリストにありました。')
       print('{}が見つかりました'.format(word))
    else:
       #source.append(word)
       print('{}はリストにありませんでしたので、追加しました。'.format(word))
       words = word.split(',')
       with open('character_name.csv', 'a',encoding="utf-8") as f:
           writer = csv.writer(f) #変数fにcsvファイルとして書き込み、変数writerに代入
           writer.writerow(words)
       
   
search()

