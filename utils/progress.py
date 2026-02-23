import math, time

def progress(current, total, start):
    percent = current * 100 / total
    elapsed = time.time() - start
    speed = current / elapsed if elapsed else 0
    eta = (total-current)/speed if speed else 0
    bar = "█" * int(percent/10) + "░" * (10-int(percent/10))
    return f"{bar} {percent:.2f}% | ETA: {int(eta)}s"
