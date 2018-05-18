function isPrime(n) {
    let i = 2;
    while (i <= Math.sqrt(n)) {
        if (n % i === 0) {
            return false
        }
        i++
    }
    return true
}

function firstN(nprimes) {
    let res = [];
    let n = 2;
    while (res.length < nprimes) {
        if (isPrime(n)) {
            res.push(n)
        }
        n++
    }
    return res
}

let primes = firstN(500);

function clickedon(pList) {
    let head = document.querySelector("#nextprime");
    let current = head.innerHTML;
    let i = 0;
    while (current > pList[i]) {
        i++
    }
    head.innerHTML = pList[i+1]
}

