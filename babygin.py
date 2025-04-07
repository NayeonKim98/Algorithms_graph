def is_baby_gin(cards):
    count = [0] * 10

    # 카드 담기
    for c in cards:
        count[c] += 1
    
    run = triplet = 0

    i = 0
    while i < 10:
        #triplet
        if count[i] >=3:
            count[i] -= 3
            triplet += 1
            continue  # 다시 검사
        
        # run
        if i <= 7 and count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            run += 1
            continue
        
        i += 1
    
    return run + triplet == 2