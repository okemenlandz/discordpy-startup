import random
import math

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
    while True:
        if random.randint(0, 3) != 0:
            break
        cnt += 1
    return cnt

def sim_symphogear():
    flag = True
    normal_cnt = 0
    while flag:
        v = random.randint(0, 19979)
        normal_cnt += 1
        if v > 19879:
            flag = False
    cnt = [0, 1, 0, 0, 0]
    for _ in range(5):
        r_ch = right()
        if r_ch == 0:
            cnt[0] += 1
        elif r_ch == 16:
            cnt[0] = 0; cnt[4] += 1
        else:
            cnt[0] = 0; cnt[int(r_ch/4)] += 1
    if cnt[0] == 5:
        return 370, normal_cnt
    while cnt[0] < 11:
        r_ch = right()
        if r_ch == 0:
            cnt[0] += 1
        elif r_ch == 16:
            cnt[0] = 0; cnt[4] += 1
        else:
            cnt[0] = 0; cnt[int(r_ch/4)] += 1
    return cnt[1]*370+cnt[2]*740+cnt[3]*1120+cnt[4]*1410, normal_cnt

def sim_gen():
    flag = True
    normal_cnt = 0
    while flag:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v > 65329:
            flag = False
    if v > 65411:
        cnt = [0, 1, 0, 0]
        while cnt[0] < 4:
            r_ch = right_g()
            if r_ch == 0:
                cnt[0] += 1
            else:
                cnt[0] = 0; cnt[int(r_ch/3)] += 1
        return cnt[1]*300+cnt[2]*600+cnt[3]*900, normal_cnt
    return 600, normal_cnt

def sim_gen2():
    flag = True
    normal_cnt = 0
    while flag:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 505:
            flag = False
    if v < 283:
        cnt = [0, 1, 0, 0]
        while cnt[0] < 4:
            r_ch = right_g2()
            if r_ch == 0:
                cnt[0] += 1
            elif r_ch == 9:
                cnt[0] = 0; cnt[2] += 1
                if random.randint(0, 9) == 0:
                    cnt[0] = -120
                    while cnt[0] < 6:
                        r2 = right_g2()
                        if r2 == 0:
                            cnt[0] += 1
                        else:
                            cnt[0] = 0; cnt[int((r2+3)/6)] += 1
                    cnt[0] = 3
            else:
                cnt[0] = 0; cnt[1] += 1
        return cnt[1]*210+cnt[2]*630, normal_cnt
    return 210, normal_cnt

def sim_aria():
    flag = True; normal_cnt = 0; normal_total = 0
    st_cnt = 0; charge_cnt = 0; max_cnt = 1
    cnt1500 = 0; cnt3000 = 0; cntover = 0
    while flag:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 164:
            flag = False; normal_total += normal_cnt
        elif v < 340:
            charge_cnt += 1; normal_total += normal_cnt; normal_cnt = 0
    status = left_aria()
    if status == 0: cnt1500 += 1
    elif status == 15: cnt1500 += 1
    elif status == 30: cnt3000 += 1
    elif status == 45: cnt3000 += 1; cntover += 1
    if status == 0:
        flag2 = True
        while flag2:
            st_cnt += 1
            if st_cnt >= 71:
                flag2 = False; break
            if random.randint(0, 65535) < 164:
                flag2 = False
                r = right_aria()
                if r == 1: cnt1500 += 1
                elif r == 2: cnt3000 += 1
                else: cnt3000 += 1; cntover += r-2
                if max_cnt < r: max_cnt = r
                status = 45
    if status in (15, 30):
        flag2 = True
        while flag2:
            st_cnt += 1
            if st_cnt >= 71:
                flag2 = False; break
            if random.randint(0, 65535) < 624:
                flag2 = False
                r = right_aria()
                if r == 1: cnt1500 += 1
                elif r == 2: cnt3000 += 1
                else: cnt3000 += 1; cntover += r-2
                if max_cnt < r: max_cnt = r
                status = 45
    if status == 45:
        while st_cnt < 167:
            st_cnt += 1
            if random.randint(0, 65535) < 624:
                r = right_aria()
                if r == 1: cnt1500 += 1
                elif r == 2: cnt3000 += 1
                else: cnt3000 += 1; cntover += r-2
                if max_cnt < r: max_cnt = r
                st_cnt = 0
    return charge_cnt*420+cnt1500*1400+cnt3000*2800+cntover*1400, normal_total

def sim_goyoku():
    flag = True; normal_cnt = 0
    cnt1500 = 0; cntover = 0
    while flag:
        v = random.randint(0, 65535)
        normal_cnt += 1
        if v < 188:
            flag = False
    if v > 104:
        cnt1500 = 2; flag = True
        while flag:
            flag = False
            if random.randint(0, 3) == 0:
                flag = True; cnt1500 += 1; cntover += 1
        cnt = [0, 0, 0, 1]
        while cnt[0] < 145:
            rv = random.randint(0, 9999)
            cnt[0] += 1
            if rv < 20:
                cnt[1] += 1
            elif rv < 75:
                cnt[2] += 1
            elif rv < 100:
                cnt[3] += 1; cnt1500 = 2; flag = True
                while flag:
                    flag = False
                    if random.randint(0, 3) == 0:
                        flag = True; cnt1500 += 1; cntover += 1
            else:
                continue
            cnt[0] = 0
        return cnt[1]*280+cnt[2]*1400+cnt[3]*2800+cntover*1400, normal_cnt
    return 1500, normal_cnt

def compute_ev(results, cycle, bps):
    total = 0
    for game_balls, spins in results:
        balls_used = spins * bps
        in_money_balls = math.ceil(balls_used / cycle) * 125
        rest = math.ceil((-balls_used % cycle) * 125 / cycle)
        total += game_balls + rest - in_money_balls
    return total / len(results)

def find_breakeven(results, bps, init_cycle):
    ev0 = compute_ev(results, init_cycle, bps)
    print(f"  EV at cycle={init_cycle}: {ev0:.2f} balls")
    lo, hi = init_cycle * 0.05, init_cycle * 20
    for _ in range(80):
        mid = (lo + hi) / 2
        if compute_ev(results, mid, bps) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

random.seed(12345)
N = 200000

print("=== symphogear ===")
r1 = [sim_symphogear() for _ in range(N)]
be1 = find_breakeven(r1, bps=2, init_cycle=21)
print(f"  break-even cycle={be1:.4f}  spins_per_unit={be1/2:.4f}")

print("=== gen ===")
r2 = [sim_gen() for _ in range(N)]
be2 = find_breakeven(r2, bps=2, init_cycle=21)
print(f"  break-even cycle={be2:.4f}  spins_per_unit={be2/2:.4f}")

print("=== gen2 ===")
r3 = [sim_gen2() for _ in range(N)]
be3 = find_breakeven(r3, bps=1, init_cycle=9)
print(f"  break-even cycle={be3:.4f}  spins_per_unit={be3:.4f}")

print("=== aria (N=100000) ===")
r4 = [sim_aria() for _ in range(100000)]
be4 = find_breakeven(r4, bps=1, init_cycle=8)
print(f"  break-even cycle={be4:.4f}  spins_per_unit={be4:.4f}")

print("=== goyoku (N=100000) ===")
r5 = [sim_goyoku() for _ in range(100000)]
be5 = find_breakeven(r5, bps=2, init_cycle=17)
print(f"  break-even cycle={be5:.4f}  spins_per_unit={be5/2:.4f}")

print()
print("=== Final Summary ===")
all_results = [r1, r2, r3, r4, r5]
configs = [
    ("symphogear", be1, 2, 21),
    ("gen",        be2, 2, 21),
    ("gen2",       be3, 1, 9),
    ("aria",       be4, 1, 8),
    ("goyoku",     be5, 2, 17),
]
for i, (name, be, bps, cur) in enumerate(configs):
    ev_check = compute_ev(all_results[i], be, bps)
    spu = be / bps
    print(f"{name}: cycle {cur} -> {be:.4f}  spins_per_unit: {spu:.4f}  EV@new={ev_check:.3f}")
