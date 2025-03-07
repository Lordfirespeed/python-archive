metricPrefixes = {"Kilo": 3, "Mega": 6, "Giga": 9, "Tera": 12, "Peta": 15, "Exa": 18, "Zetta": 21, "Yotta": 24}
ibiPrefixes = {"Kibi": 10, "Mebi": 20, "Gibi": 30, "Tebi": 40, "Pebi": 50, "Exbi": 60, "Zebi": 70, "Yobi": 80}


def print_prefix_comparison(metricPrefix, metricPower, ibiPrefix, ibiPower):
    metricSize = 10 ** metricPower
    ibiSize = 2 ** ibiPower
    sizeDifferenceDecimal = (ibiSize - metricSize) / metricSize
    sizeDifferencePercentage = round(sizeDifferenceDecimal * 100, 2)
    print(f"{metricPrefix:>5}byte: {metricSize:,} bytes")
    print(f"{ibiPrefix:>5}byte: {ibiSize:,} bytes")
    print(f"Effective size difference {sizeDifferencePercentage}%")
    print()


if __name__ == "__main__":
    for metrixPrefixInfo, ibiPrefixInfo in zip(metricPrefixes.items(), ibiPrefixes.items()):
        print_prefix_comparison(*metrixPrefixInfo, *ibiPrefixInfo)
