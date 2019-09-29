def shipWithinDays(weights, D) -> int:
    min_weight = max(weights)

    while True:
        shipping_days = [0] * D
        current_day = 0
        finished = True
        small_weight = 999999999
        for elm in weights:
            if (shipping_days[current_day] + elm <= min_weight):
                shipping_days[current_day] += elm
            elif current_day+1 < D:
                if shipping_days[current_day] + elm < small_weight:
                    small_weight = shipping_days[current_day] + elm
                current_day += 1
                shipping_days[current_day] += elm
            else:
                if shipping_days[current_day] + elm < small_weight:
                    small_weight = shipping_days[current_day] + elm
                min_weight = small_weight
                finished = False
                break

        if finished:
            return min_weight

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 1))