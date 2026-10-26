# -*- coding: utf-8 -*-
import math, random, unicodedata

def _disp_width(s):
    w = 0
    for c in s:
        w += 2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1
    return w

def _ljust_w(s, width, fillchar='　'):
    current = _disp_width(s)
    if current >= width:
        return s
    padding = width - current
    fill_w = _disp_width(fillchar)
    return s + fillchar * (padding // fill_w) + ' ' * (padding % fill_w)

# テスト: 桁数が違うケース + 半角混じり名前
args = [
    '山田',     '25000', '0',    '1',
    '中村太郎', '8000',  '0',    '2',
    'キムラ',   '15000', '5000', '1',
    'Aさん',    '10000', '3000', '0',
]

total = 0
dist_list = []
for i in range(0, len(args), 4):
    total += int(args[i+1])
    if int(args[i+2]) != 0:
        total -= int(args[i+2])
    if int(args[i+3]) != 0:
        dist_list.append((i, int(args[i+3])))

total_ratio = sum(r for _, r in dist_list)
shares = {}
for i, ratio in dist_list:
    shares[i] = math.floor(total * ratio / total_ratio)

amari = total - sum(shares.values())
if amari > 0:
    for idx in random.sample([i for i, _ in dist_list], amari):
        shares[idx] += 1

rows = []
for i in range(0, len(args), 4):
    name = args[i]
    score = int(args[i+1])
    payment = int(args[i+2])
    ratio = int(args[i+3])
    if ratio != 0:
        receive = shares[i] + payment
        diff = receive - score
    else:
        receive = payment
        diff = payment - score
    rows.append((name, score, receive, diff))

w1 = max(len(str(r[1])) for r in rows)
w2 = max(len(str(r[2])) for r in rows)
w3 = max(len(str(r[3])) for r in rows)

print('=== nori-rate 出力 ===')
out = '```\n'
for name, score, receive, diff in rows:
    out += f'{_ljust_w(name,10)} {str(score).rjust(w1)} {str(receive).rjust(w2)} {str(diff).rjust(w3)}\n'
print(out + '```')
print(f'列幅: score={w1}, receive={w2}, diff={w3}')
