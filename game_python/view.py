import character as c

def print_self_select():
    print("誰を選びますか")
    print("平野店長 : 1")
    print("野獣先輩 : 2")
    print("葛　　城 : 3")
    inp_self = int(input())
    if inp_self == 1:
        y = c.hirano_tentyo()
    elif inp_self == 2:
        y = c.yazyu()
    elif inp_self == 3:
        y = c.kasturagi()
    return y


def print_target_select():
    print("対戦相手を選ぼう(提案)")
    print("平野店長 : 1")
    print("野獣先輩 : 2")
    print("葛　　城 : 3")
    inp_ene = int(input())
    if inp_ene == 1:
        t = c.hirano_tentyo()
    elif inp_ene == 2:
        t = c.yazyu()
    elif inp_ene == 3:
        t = c.kasturagi()
    return t


def print_command_select(y, t):
    print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
    print("　　　　　　     HP    MP      AT     DE")
    print(y.name + "　"*(6-(len(y.name))), "  ", + y.HP,  "  ",  y.MP, "  " ,y.AT, "  ", y.DE)
    y.status()
    print(t.name + "　"*(6-(len(t.name))), "  " , t.HP, "  " , t.MP, "  " , t.AT, "  ", t.DE)
    t.status()
    print("1 : 攻撃\n2 : チャージ\n3 : 回復\n4 : 特殊攻撃\n", end='')
    if y.name == "野獣先輩":
        print("5 : 毒技")
    if y.name == "平野店長":
        print("5 : ガチビンタ\n6 : リフレクション")
    inp = int(input("好きなコマンドを入力しよう(提案) : "))
    print("---------------------------------------------")
    return inp


def ozisan_kakusei(you, tar):
    if you.name == "虐待おじさん" and you.HP <= 250 and you.kakusei_flg == 0:
        you.AT *= 1.5
        you.kakusei_flg = 1
        print("おじさんのこと本気で怒らせちゃったね！")
        print("おじさんは覚醒した！")

    if tar.name == "虐待おじさん" and tar.HP <= 250 and tar.kakusei_flg == 0:
        tar.AT *= 1.5
        tar.kakusei_flg = 1
        print("おじさんのこと本気で怒らせちゃったね！")
        print("おじさんは覚醒した！")

def print_win(tar):
    print(tar.ziseinoku)
    if tar.name == "野獣先輩":
        print_yazyu()
    print("You WIN!!")




def print_lose(you):
    print(you.ziseinoku)
    if you.name == "野獣先輩":
        print_yazyu()

    print("You LOSE...")


def print_yazyu():
    print("　　　　　　　　　　　　　 ,,,z=~’ﾞ’+”ｯ彡ｯ,､")
    print("　　　　　　　　　　　　,ｨ´ 　　　　　 “‘:’;:;ｯ;,")
    print("　　　　　　　　 ,　’ ﾞ´`ﾞﾐﾞｯ,　　　　　　　 “‘,`,")
    print("　　　　　　 ,／ 　　　 `､ﾞミ　　　　　　　　 ﾞ:;:,")
    print("　　　　　 /　　　　　 _ =ヾ､ﾞｼｼ=;,z,、　　　 ﾞ;ｼ::ﾐ")
    print("　　　　 /　　　　 ,ｒ,´　　 /　´`ヽ ゛ﾞ`　 　　,ﾞ彡:ﾐ")
    print("　　　 / 　　　, ‘-､_`ヽ_/,　　　　　　　 　 ﾐ;::彡;:")
    print("　　 ,’　　　,ｼ´｀｀ ヽ`i｀!　　　　　　　　 ,,彡;::ｼ:彡　")
    print("　　;i　　､（´ ￣`ヽ / ‘　　　　　　　　シ:ｼ;:ﾐ::ｼ”")
    print("　ノ:!､　 ヽ｀`ｰ =;ｨ’　　　　　　　　,,ｼ:;彡;ｼﾞ")
    print("´:::::.ヾ. 　　　￣´　　　　　　　　’ `,ｼﾐﾞ")
    print(":::::::::::::.`:ヽ､_　　　　　　　…:;’＿,ソ’ﾞ”")
    print("::::::::::::::::｀::::::::::-=””／")

# def print_hirano():
#    print("        ■     ■■      ■             ■■            ■            ■■      ")
#    print("        ■■     ■       ■             ■■            ■■           ■■     ")
#    print("        ■■     ■       ■             ■            ■■■           ■      ")
#    print("        ■■ ■   ■■■     ■         ■  ■■■■ ■      ■■■            ■■      ")
#    print("        ■   ■■■■■      ■         ■■■■  ■  ■■    ■              ■       ")
#    print("        ■      ■       ■            ■  ■   ■    ■             ■        ")
#    print("        ■ ■    ■       ■           ■■  ■   ■■   ■  ■■■■      ■■■■■     ")
#    print("        ■■     ■       ■           ■   ■ ■■■■   ■■■    ■     ■■  ■     ")
#    print("        ■■     ■      ■■      ■   ■■   ■        ■■     ■    ■■   ■   ■■")
#    print("        ■■    ■■       ■     ■    ■   ■■        ■      ■    ■    ■   ■ ")
#    print("        ■■    ■■       ■   ■■    ■■ ■ ■               ■■   ■■    ■  ■■ ")
#    print("         ■   ■■        ■■■■■     ■   ■■             ■■■    ■■    ■■■■  ")
#    print("                                                  ■■                   ")
