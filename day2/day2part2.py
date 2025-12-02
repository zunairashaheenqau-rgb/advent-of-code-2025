#!/usr/bin/env python3

def parse_ranges(s):
    parts = [p.strip() for p in s.split(',') if p.strip()]
    out = []
    for p in parts:
        if '-' in p:
            a, b = p.split('-', 1)
            out.append((int(a), int(b)))
    return out

def sum_invalid(ranges):
    found = set()
    if not ranges:
        return 0
    max_b = max(b for _, b in ranges)
    max_digits = len(str(max_b))

    for a, b in ranges:
        for digits in range(1, max_digits):
            s_min = 10**(digits - 1)
            s_max = 10**digits - 1

            for reps in range(2, max_digits // digits + 1):
                mult = sum(10**(digits * i) for i in range(reps))
                low = max(s_min, (a + mult - 1) // mult)
                high = min(s_max, b // mult)

                if low <= high:
                    for s in range(low, high + 1):
                        n = s * mult
                        if a <= n <= b:
                            found.add(n)

    return sum(found)

def main():
    s = "52-75,71615244-71792700,89451761-89562523,594077-672686,31503-39016,733-976,1-20,400309-479672,458-635,836793365-836858811,3395595155-3395672258,290-391,5168-7482,4545413413-4545538932,65590172-65702074,25-42,221412-256187,873499-1078482,118-154,68597355-68768392,102907-146478,4251706-4487069,64895-87330,8664371543-8664413195,4091-5065,537300-565631,77-115,83892238-83982935,6631446-6694349,1112-1649,7725-9776,1453397-1493799,10240-12328,15873-20410,1925-2744,4362535948-4362554186,3078725-3256936,710512-853550,279817-346202,45515-60928,3240-3952"
    ranges = parse_ranges(s)
    print(sum_invalid(ranges))

if __name__ == "__main__":
    main()
