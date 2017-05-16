def you_status(you, inp):
    """プレイヤーのステータス処理。
    """
    if you.suimin_flg == 1:  # 睡眠は麻痺より優先される
        inp = 0
        you.suimin()
    if you.mahi_flg == 1  and you.suimin_flg == 0:  # 麻痺
        inp = 0
        you.mahi()
    if you.poison_flg == 1:  # 毒
        you.poison()
    return inp


def you_action(you, tar, inp, ref_count):
    """プレイヤーの行動実行
    """
    if inp == 1:
        you.ACT(tar)
    elif inp == 2:
        you.charge()
    elif inp == 3:
        you.heal()
    elif inp == 4:
        you.special_attack(tar)
    elif inp == 5:  # 分岐
        if you.name == "野獣先輩":
            you.poison_attack(tar)
        elif you.name == "平野店長":
            you.gachi_binta(tar)
    elif inp == 6:
        you.ref_count = ref_count
        you.donuts_reflection()

    # 麻痺。睡眠状態の時に実行
    elif inp == 0:
        pass


def ene_status(a, tar):
    """敵のステータス
    """
    # 睡眠状態の場合
    if tar.suimin_flg == 1:
        a = 0
        tar.suimin()

    # 麻痺状態の場合
    if tar.mahi_flg == 1:
        a = 0
        tar.mahi()

    # 毒状態の場合
    if tar.poison_flg == 1:
        tar.poison()
    else:
        pass
    return a


def ene_action(a, you, tar, ref_count):
    """敵の行動。ランダムに決まる
    """
    if a == 1:
        tar.ACT(you)
    elif a == 2:
        tar.charge()
    elif a == 3:
        tar.heal()
    elif a == 4:
        tar.special_attack(you)
    elif a == 5:
        if tar.name == "野獣先輩":
            tar.poison_attack(you)
        elif tar.name == "平野店長":
            tar.gachi_binta(you)
    elif a == 6:
        tar.ref_count = ref_count
        tar.donuts_reflection()
    elif a == 0:
        pass
