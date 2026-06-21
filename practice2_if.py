name=input("あなたの名前を教えてください＞＞")
print(f"{name}さん、こんにちは！")
if name=="田中":
    print("田中さんに会うのが夢でした。")
food=input(f"{name}さんの好きな食べ物は何ですか？＞＞")
if "寿司" in food:
    print("私も寿司が大好きです！特にマグロ！！")
else:
    print(f"私も{food}が好きですよ")