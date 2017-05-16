from numpy.random import *
import view as v


class Original(object):
    """型となる親クラス
    """
    suimin_flg = 0
    mahi_flg = 0
    poison_flg = 0
    zyotai = 0
    ref_count = 0
    reflect_flg = 0

    def __init__(self, HP, AT, MP, DE, serihu, name, ziseinoku):
        """コンストラクタ。最初に起動される部分
        """
        self.HP = HP
        self.AT = AT  # 攻撃力
        self.MP = MP  # マジックポイント
        self.DE = DE  # 防御力
        self.serihu = serihu  # 会心の一撃の際の台詞
        self.name = name
        self.ziseinoku = ziseinoku  # 負けた時の台詞

    def status(self):
        """ステータス表示。異常の時だけ表示。
        """
        status_list = ["睡眠", "麻痺", "毒"]

        # 状態異常を文字列化した0, 1のバイナリで表現
        self.zyotai = str(self.suimin_flg) + str(self.mahi_flg) + str(self.poison_flg)

        for num, i in enumerate(status_list):
            if self.zyotai[num] == '1':  # int型だとfor文で回せない
                if num == len(status_list):
                    print(i)
                else:
                    print(i + " ", end='')
        print()




    def ACT(self, target):
        """攻撃コマンド。
        """
        s = randint(10)
        point = round(randint(30, 40) * (1 + (self.AT - target.DE)/100), 0)
        if s == 0:  # 10% の確率で会心の一撃
            point_c = round(point * 1.5, 0)  # 1.4倍
            target.HP -= point_c
            print(self.serihu)
            print("痛恨の一撃！" + target.name + "に" + str(point_c) + "のダメージ!")
        else:
            target.HP -= point
            print(self.name + "の攻撃！" + target.name + "に" + str(point) + "のダメージ！")

    def charge(self):
        """チャージ用の関数
        """
        a_up_point = randint(10, 15)
        self.AT += a_up_point
        print(self.name + "はチャージした！　攻撃力" + str(a_up_point) + "アップ！")

    def heal(self):
        """回復用の関数
        """
        print(self.name + "は回復呪文を唱えた！", end='')
        if self.MP >= 5:
            self.MP -= 5
            re_point = randint(30, 50)
            self.HP += re_point
            print("体力が" + str(re_point) + "回復した！")
        else:
            print("しかしMPが足りない！")

    def special_attack(self, target):
        """キャラによって異なる為、空のまま
        """
        pass


    def mahi(self):
        """麻痺状態
        """
        s1 = randint(5)
        if s1 <= 4:
            print("痺れて何もできない！")
        s = randint(5)
        if s == 0:
            self.mahi_flg = 0  # 5割の確率で治る
            print("麻痺が治った！")

    def suimin(self):
        """睡眠状態
        """
        s = randint(3)
        if s <= 1:  # 2/3で行動不能
            print(self.name + "は眠っている！")
        else:
            self.suimin_flg = 0
            print(self.name + "は目を覚ました！")

    def poison(self):
        """毒状態
        """
        point = 15
        self.HP -= point
        print(self.name + "は毒を受けた！" + str(point) + "のダメージ！")



class hirano_tentyo(Original):
    """平野店長のクラス。相手を縛って一時的に行動不能にする麻痺技や
        一定のダメージを与える技を持つ。
    """

    def __init__(self):
        super().__init__(HP=600,
                         AT=70,
                         MP=100,
                         DE=80,
                         serihu="「気合はあるか？」",
                         name="平野店長",
                         ziseinoku="「この私が......」")


    def special_attack(self, you):
        """麻痺技。66%の確率で成功。MP10消費
        """
        print(self.name + "の縛道第一歌・呪！")
        if self.MP >= 10:
            self.MP -= 10

            s = randint(3)
            if s <= 1:
                print("「無駄だよ」")
                print(you.name + "は動けなくなった！")
                you.mahi_flg = 1
            else:
                print("しかし失敗した！")
        else:
            print("MPが足りない！")


    def gachi_binta(self, tar):
        """ガチビンタ。相手の残りHPの15%を減らす。
        """
        # v.print_hirano()  # なし
        s = randint(10)
        print(self.name + "のガチビンタ！")
        if s <= 8:  # 命中率90%
            point = round(tar.HP * 0.15)
            tar.HP -= point
            print(tar.name + "に" + str(point) + "のダメージ！")
        else:
            print("しかし、攻撃が外れた！")


    def donuts_reflection(self):
        """3ターンの間だけ防御力を上げる魔法技。
        """
        print(self.name + "のドーナッツ・リフレクション！")
        if self.MP >= 25:
            if self.reflect_flg == 0:
                self.reflect_flg = 1
                self.MP -= 25
                self.DE *= 2
                print(self.name + "は神秘のベールに包まれた！" )
            else:
                print("しかし、すでにかかっている！")
        else:
            print("MPが足りない！(絶望)")






class kasturagi(Original):
    """虐待おじさんのクラス。3割の確率で2回攻撃を繰り出し、
        体力が250以下になると攻撃力が2倍になる。ただし、回復量が少なく、特殊技の命中率も低め。
    """

    kakusei_flg = 0

    def __init__(self):
        super().__init__(HP=700,
                         AT=120,
                         MP=20,
                         DE=80,
                         serihu="「興奮させてくれるねえ！」",
                         name="虐待おじさん",
                         ziseinoku="「全く、困ったもんじゃい......」")


    def heal(self):  # 虐待おじさんは攻撃特化にしたいので魔法能力を弱めに再設定(オーバーライド)する。
        print(self.name + "は回復呪文をと唱えた！")
        if self.MP >= 5:
            self.MP -= 5
            re_point = randint(15, 25)
            self.HP += re_point
            print("体力が" + str(re_point) + "回復した！")
        else:
            print("MPが足りない！")


    def special_attack(self, you):
        print("「真ん中こいよ」")
        point = 30
        self.HP -= point
        meityu_ritu = randint(10)
        if meityu_ritu <= 1:  # 20%で外れる
            print(self.name + "の攻撃は外れた！")
        else:
            self.ACT(you)
            s = randint(3)
            if s <= 1:  # 2/3の確率で2回攻撃
                print("2回目の攻撃！")
                self.ACT(you)
        print("反動で" + str(point) + "のダメージ!")  # 反動でダメージを受ける


# 作るの途中でやめる
class yusaku(Original):
    """ゆうさくのクラス。途中
    """
    name = "ゆうさく"
    serihu = "乳首感じるんでしたよね？"
    DE = 0

    def __init__(self, HP=1000, AT=100, DE=100):
        self.HP = HP
        self.AT = AT
        self.DE = DE


class yazyu(Original):
    """野獣先輩のクラス。毒技、眠り技など多様な攻撃を仕掛ける
    """
    def __init__(self):
        super().__init__(HP=900,
                         AT=100,
                         MP=80,
                         DE=100,
                         serihu="「いいよ！　こいよ！」",
                         name="野獣先輩",
                         ziseinoku="「んああああああああああああああああ！」")


    def special_attack(self, target):
        """眠らせる攻撃
        """
        print(self.name + "の昏睡攻撃！")
        if self.MP < 10:
            print("MPが足りない！")
            return
        self.MP -= 10
        s = randint(10)
        if s <= 6 and target.suimin_flg == 0:
            target.suimin_flg = 1
            print("「アイスティーしかなかったけどいいかな？」")
            print(target.name + "は眠ってしまった！")
        else:
            print("しかし失敗した！")


    def poison_attack(self, target):
        """毒状態にさせる攻撃
        """
        print("ブッチッパ！")
        if self.MP >= 10:
            self.MP -= 10
            s = randint(10)
            if s <= 7 :  # 70%の確率で毒
                target.poison_flg = 1
                print(target.name + "は毒を受けた！")
            else:
                print("しかし失敗した！")
        else:
            print("MPが足りない！")
