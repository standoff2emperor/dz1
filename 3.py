def analyze_scores(*scores):
    if len(scores)==0:
        return 0,0,0
    total=sum(scores)
    count=len(scores)
    average=total/count
    return total, count, average
def print_report(team_name, **info):
    print("Команда:", team_name)
    for k, v in info.items():
        print(f"{k}: {v}")
result1=analyze_scores(8, 10, 7, 9)
print(result1)
result2=analyze_scores(5, 5)
print(result2)
result3=analyze_scores()
print(result3)
print_report("Комета", coach="Иванов", city="Минск")
