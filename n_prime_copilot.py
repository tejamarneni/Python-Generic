def primelist(num):
  prime_list = [2]

  j = 3
  while len(prime_list) < num:
    is_prime = True
    for k in range(3, int(j**0.5) + 1, 2):
      if j % k == 0:
        is_prime = False

    if is_prime:
      prime_list.append(j)
    J += 2

  return prime_list

print(primelist(15))
                    
