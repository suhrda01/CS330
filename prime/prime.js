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

function clickedon() {
    let tab = document.querySelector("#primetab");
    tab.innerHTML = "";
    let input = document.querySelector("#numprimes");
    let primes = firstN(input.value);
    for (let item of primes) {
        let row = tab.appendChild(document.createElement("tr"));
        let data = row.appendChild(document.createElement("td"));
        data.innerHTML = item;
    }
}

