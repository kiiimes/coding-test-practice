def solution(today, terms, privacies):
    answer = []
    dic = {}

    today_date = list(map(int, today.split('.')))
    td = today_date[0]*12*28 + today_date[1]*28 + today_date[2]
    
    for t in terms:
        data = t.split(' ')
        dic[data[0]] = int(data[1])
        
        
    for i in range(len(privacies)):
        p_date_info = privacies[i].split(' ')
        p_date = list(map(int,p_date_info[0].split('.')))
        pd = p_date[0]*12*28 + p_date[1]*28 + p_date[2]

        if td >= (pd + dic[p_date_info[1]]*28):
            answer.append(i+1)
            
    return answer
