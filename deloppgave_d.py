def tell_antall_storre_eller_lik(lst, M):
    liste_storre_eller_lik = [num for num in lst if num >= M]
    return len(liste_storre_eller_lik)