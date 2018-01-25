def backtracking(all_answers, possible_answer, candidates, target):
    if target == 0:
        all_answers.append(possible_answer[:])
    for i in candidates:
        if i > target:
            return
        if possible_answer and i < possible_answer[-1]:
            continue
        possible_answer.append(i)
        backtracking(all_answers, possible_answer, candidates, target - i)
        possible_answer.pop()

def solve_coins(coin_candidates, target):
    all_answers = []
    backtracking(all_answers, [], sorted(coin_candidates), target)
    print(len(all_answers))

def main():
    solve_coins([1,2,5,10,20,50, 100,200], 200)

if __name__ == '__main__':
    main()