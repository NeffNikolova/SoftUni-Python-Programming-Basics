processor_usd = float(input())
videocard_usd = float(input())
ram_usd = float(input())
ram_nr = int(input())
discount = float(input())

price_usd = (processor_usd * (1-discount)) + (videocard_usd * (1 - discount)) + (ram_usd * ram_nr)

price_bgn = price_usd * 1.57

print(f"Money needed - {price_bgn:.2f} leva.")