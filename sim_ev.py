import random
import math
import statistics

def right():
    r = random.randint(0, 36)
    if r < 5:
        pl = random.randint(0, 99)
        if pl < 40: return 16
        elif pl < 43: return 12
        elif pl < 50: return 8
        else: return 4
    return 0

def right_g():
    r = random.randint(0, 205)
    if r < 80: return 3
    elif r < 100: return 9
    else: return 0

def right_g2():
    r = random.randint(0, 243)
    if r < 80: return 3
    elif r < 100: return 9
    else: return 0

def left_aria():
    r = random.randint(0, 99)
    if r < 10: return 45
    elif r < 50: return 30
    elif r < 55: return 15
    else: return 0

def right_aria():
    cnt = 1
    while random.randint(0, 3) == 0:
        cnt += 1
    return cnt

def sim_symphogear():
    normal_cnt = 0
    while True:
        v = random.randint(0, 19979)
        normal_cnt += 1
        if v > 19879:
            break
    in_money = math.ceil(normal_cnt / 9.91) * 125
    rest = math.ceil(((0 - (normal_cnt * 2)) % 19.82) * 125 / 19.82)

    cnt = [0, 1, 0, 0, 0]
    for _ in range(5):
        r_ch = right()
        if r_ch == 0: cnt[0] += 1
        elif r_ch == 16: cnt[0] = 0; cnt[4] += 1
        else: cnt[0] = 0; cnt[int(r_ch / 4)] += 1

    if cnt[0] == 5:
        total = 370 + rest
    else:
        while cnt[0] < 11:
            r_ch = right()
            if r_ch == 0: cnt[0] += 1
            elif r_ch == 16: cnt[0] = 0; cnt[4] += 1
            else: cnt[0] = 0; cnt[int(r_ch / 4)] += 1
        total = cnt[1]*370 + cnt[2]*740 + cnt[3]*1120 + cnt[4]*1410 + rest

    return in_money, total

def sim_gen():
    normal_cnt = 0
    while True:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v > 65329:
            break
    in_money = math.ceil(normal_cnt / 10.46) * 125
    rest = math.ceil(((0 - (normal_cnt * 2)) % 20.92) * 125 / 20.92)

    rush = (v > 65411)

    if not rush:
        total = 600 + rest
    else:
        cnt = [0, 1, 0, 0]
        while cnt[0] < 4:
            r_ch = right_g()
            if r_ch == 0: cnt[0] += 1
            else: cnt[0] = 0; cnt[int(r_ch / 3)] += 1
        total = cnt[1]*300 + cnt[2]*600 + cnt[3]*900 + rest

    return in_money, total

def sim_gen2():
    normal_cnt = 0
    while True:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 505:
            break
    in_money = math.ceil(normal_cnt / 8.65) * 125
    rest = math.ceil(((0 - normal_cnt) % 8.65) / 8.65 * 125)

    rush = (v < 283)

    if not rush:
        total = 210 + rest
    else:
        cnt = [0, 1, 0, 0]
        while cnt[0] < 4:
            r_ch = right_g2()
            if r_ch == 0:
                cnt[0] += 1
            elif r_ch == 9:
                cnt[0] = 0
                cnt[2] += 1
                if random.randint(0, 9) == 0:
                    cnt[0] = -120
                    while cnt[0] < 6:
                        r_ch2 = right_g2()
                        if r_ch2 == 0: cnt[0] += 1
                        else: cnt[0] = 0; cnt[int((r_ch2 + 3) / 6)] += 1
                    cnt[0] = 3
            else:
                cnt[0] = 0
                cnt[1] += 1
        total = cnt[1]*210 + cnt[2]*630 + rest

    return in_money, total

def sim_aria():
    normal_cnt = 0
    normal_total = 0
    st_cnt = 0
    charge_cnt = 0
    max_cnt = 1
    cnt1500 = 0
    cnt3000 = 0
    cntover = 0

    while True:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 164:
            normal_total += normal_cnt
            break
        elif v < 340:
            charge_cnt += 1
            normal_total += normal_cnt
            normal_cnt = 0

    in_money = math.ceil(normal_total / 8.43) * 125
    rest = math.ceil(((0 - normal_total) % 8.43) / 8.43 * 125)

    status = left_aria()
    if status == 0: cnt1500 += 1
    elif status == 15: cnt1500 += 1
    elif status == 30: cnt3000 += 1
    elif status == 45: cnt3000 += 1; cntover += 1

    def add_rush_hit():
        nonlocal cnt1500, cnt3000, cntover, max_cnt
        r = right_aria()
        if r == 1: cnt1500 += 1
        elif r == 2: cnt3000 += 1
        else: cnt3000 += 1; cntover += r - 2
        if max_cnt < r: max_cnt = r

    if status == 0:
        hit = False
        while True:
            st_cnt += 1
            if st_cnt >= 71:
                total = charge_cnt*420 + cnt1500*1400 + cnt3000*2800 + cntover*1400 + rest
                return in_money, total
            if random.randint(0, 65535) < 164:
                add_rush_hit()
                status = 45
                hit = True
                break

    if status in (15, 30):
        while True:
            st_cnt += 1
            if st_cnt >= 71:
                total = charge_cnt*420 + cnt1500*1400 + cnt3000*2800 + cntover*1400 + rest
                return in_money, total
            if random.randint(0, 65535) < 624:
                add_rush_hit()
                status = 45
                break

    if status == 45:
        while st_cnt < 167:
            st_cnt += 1
            if random.randint(0, 65535) < 624:
                add_rush_hit()
                st_cnt = 0
        total = charge_cnt*420 + cnt1500*1400 + cnt3000*2800 + cntover*1400 + rest
        return in_money, total

def sim_goyoku():
    normal_cnt = 0
    cnt1500_val = 0
    cntover = 0
    bonus_max = 3000

    while True:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 188:
            break

    in_money = math.ceil(normal_cnt / 9.25) * 125
    rest = math.ceil(((0 - (normal_cnt * 2)) % 18.50) * 125 / 18.50)

    if v <= 104:
        total = 1500 + rest
        return in_money, total

    cnt = [0, 0, 0, 1]
    cnt1500_val = 2
    flag = True
    while flag:
        flag = False
        if random.randint(0, 3) == 0:
            flag = True
            cnt1500_val += 1
            cntover += 1

    while cnt[0] < 145:
        right_val = random.randint(0, 9999)
        cnt[0] += 1
        if right_val < 20:
            cnt[1] += 1
            cnt[0] = 0
        elif right_val < 75:
            cnt[2] += 1
            cnt[0] = 0
        elif right_val < 100:
            cnt[3] += 1
            cnt1500_val = 2
            flag = True
            while flag:
                flag = False
                if random.randint(0, 3) == 0:
                    flag = True
                    cnt1500_val += 1
                    cntover += 1
            if cnt1500_val * 1500 > bonus_max:
                bonus_max = cnt1500_val * 1500
            cnt[0] = 0

    total = cnt[1]*280 + cnt[2]*1400 + cnt[3]*2800 + cntover*1400 + rest
    return in_money, total

def sim_madoka3():
    normal_cnt = 0
    while True:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 205:
            break
    in_money = math.ceil(normal_cnt / 9.86) * 125
    rest = math.ceil(((0 - normal_cnt) % 9.86) / 9.86 * 125)

    total_balls = 0
    enter_usr = False

    j = random.randint(0, 99)
    if j == 0:
        total_balls += 1400
        enter_usr = True
    elif j < 31:
        total_balls += 420
    else:
        total_balls += 420
        walp_cnt = 0
        while walp_cnt < 100:
            walp_cnt += 1
            if random.randint(0, 65535) < 447:
                total_balls += 1400
                enter_usr = True
                break

    if enter_usr:
        usr_cnt = 0
        while usr_cnt < 130:
            usr_cnt += 1
            if random.randint(0, 65535) < 795:
                total_balls += 700 if random.randint(0, 3) == 0 else 2800
                usr_cnt = 0

    total = total_balls + rest
    return in_money, total

def sim_takt(exchange=20.7):
    normal_cnt = 0
    normal_total = 0
    total_net = 0

    while True:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 47:
            normal_total += normal_cnt
            break
        elif v < 188:
            total_net += 280
            normal_total += normal_cnt
            normal_cnt = 0

    in_money = math.ceil(normal_total / exchange) * 500
    rest = math.ceil(((0 - normal_total) % exchange) / exchange * 125)

    total_net += 1400

    if random.randint(0, 1) == 1:
        for _ in range(5):
            r = random.randint(0, 999)
            if r < 237:
                total_net += 1400
            else:
                total_net += 280

        while True:
            rush_hit = False
            for i in range(144):
                if random.randint(0, 65535) < 656:
                    rush_hit = True
                    break
            if rush_hit:
                for _ in range(5):
                    r2 = random.randint(0, 999)
                    if r2 < 237:
                        total_net += 1400
                    else:
                        total_net += 280
            else:
                break

    return in_money, (total_net + rest) * 4


machines = [
    ('m-symphogear', sim_symphogear),
    ('m-gen',        sim_gen),
    ('m-gen2',       sim_gen2),
    ('m-aria',       sim_aria),
    ('m-goyoku',     sim_goyoku),
    ('m-madoka3',    sim_madoka3),
]

N = 100000
print(f"{'機種':<14} {'平均投資':>9} {'平均回収':>9} {'平均収支':>10} {'回収率':>7}  (N={N})")
print("-" * 58)
for name, sim in machines:
    data = [sim() for _ in range(N)]
    inv = statistics.mean(d[0] for d in data)
    rec = statistics.mean(d[1] for d in data)
    diff = rec - inv
    rate_pct = rec / inv * 100
    print(f"{name:<14} {inv:>9.0f}円 {rec:>9.0f}円 {diff:>+10.0f}円 {rate_pct:>6.2f}%")
