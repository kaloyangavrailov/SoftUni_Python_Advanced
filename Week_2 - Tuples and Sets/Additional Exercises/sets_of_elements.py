n_int, m_int = input().split()
n_set = {int(input()) for x in range(int(n_int))}
m_set = {int(input()) for x in range(int(m_int))}
print(*n_set.intersection(m_set), sep='\n')