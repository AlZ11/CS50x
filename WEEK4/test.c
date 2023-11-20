#include <stdio.h>

int main() {
    cm_grows, no_poppies, events_observed = map(int, input().split())
    lst = map(int, input().split())
    prev_day, returns = 0, []
    for i in range(events_observed):
        data = list(map(int, input().split()))
        if data[0] > prev_day:
            lst = [x + ((data[0] - prev_day) * cm_grows) for x in lst]

        if data[1] == 1:
            lst.append(data[2])

        elif data[1] == 0:
            elem = max(lst)
            returns.append(elem)
            lst.remove(elem)
        prev_day = data[0]

    while arr

    return 0;
}