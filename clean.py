import csv, re, argparse
from datetime import datetime

def norm_key(k):
    k = k.strip().lower()
    k = re.sub(r'[^a-z0-9]+', '_', k)
    return k.strip('_')

def norm_val(v):
    if v is None:
        return ''
    v = str(v).strip()
    if v.lower() in ('n/a', 'na', 'none', 'nan', 'null', '-'):
        return ''
    for fmt in ('%Y/%m/%d', '%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y'):
        try:
            return datetime.strptime(v, fmt).strftime('%Y-%m-%d')
        except ValueError:
            pass
    return v

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('-o', '--output', default='clean_output.csv')
    a = ap.parse_args()

    with open(a.input, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print('空文件')
        return

    keys = [norm_key(k) for k in rows[0].keys()]
    seen, out = set(), []

    for r in rows:
        vals = [norm_val(v) for v in r.values()]
        if not any(vals):
            continue
        sig = tuple(vals)
        if sig in seen:
            continue
        seen.add(sig)
        out.append(dict(zip(keys, vals)))

    with open(a.output, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(out)

    print(f'完成：{len(rows)} 行 -> {len(out)} 行，已保存到 {a.output}')

if __name__ == '__main__':
    main()