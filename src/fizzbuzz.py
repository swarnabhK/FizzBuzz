def fizzbuzz(endRange):
  result = []
  for number in range(1,endRange+1):
    if(number%3==0 and number%5==0):
      result.append('FizzBuzz')
    elif(number%3==0):
      result.append('Fizz')
    elif(number%5==0):
      result.append('Buzz')
    else:
      result.append(number)
  return result

