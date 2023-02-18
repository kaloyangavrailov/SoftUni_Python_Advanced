from collections import deque

peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,
}

conquered_peaks = []
daily_portions = deque(map(int, input().split(', ')))  # last daily food portion
daily_stamina = deque(map(int, input().split(', ')))  # first daily stamina

while peaks and daily_stamina and daily_portions:
    adventure_value = daily_portions.pop() + daily_stamina.popleft()

    list_peaks = deque(item for item in peaks.keys())

    if adventure_value >= peaks[list_peaks[0]]:
        conquered_peak = list_peaks.popleft()
        conquered_peaks.append(conquered_peak)
        del peaks[conquered_peak]
    else:
        continue

if len(conquered_peaks) == 5:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print(f'Conquered peaks:')
    print(*conquered_peaks, sep='\n')