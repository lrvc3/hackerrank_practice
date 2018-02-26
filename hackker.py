if __name__ == '__main__':
    dicti = {}
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
        dicti[name] = score

    #score_list = [float(i) for i in score]
##
##    print(dicti)
##    print(name_list)
##    print(score_list)
##    print(min(score_list))

    minscore = min(score_list)

    while minscore in score_list:
        score_list.remove(minscore)

    main_list = []

    for i in range(len(dicti)):
        if dicti[name_list[i]] == min(score_list):
            main_list.append(name_list[i])

##    main_list = main_list.sort
##
##    for i in main_list:
##        print(i)

    for x in sorted(main_list):
        print(x)


            
    
##    for x in range(len(name)):
##        dict[name[x]] = score_list[x]
##
##    print(dict)
