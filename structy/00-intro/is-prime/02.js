const isPrime = (n) => {
  if (n < 2) {
    return false;
  }
  
  for (let i = 2; i <= Math.sqrt(n); i += 1) {
    if (n % i === 0) {
        return false;
    }
  }
  
  return true;
};