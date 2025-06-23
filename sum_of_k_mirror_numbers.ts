function kMirror(k: number, n: number): number {
    let ans = 0
    let count = 0
    let currentNum = 1

    while (count < n) {
        if (isRev(currentNum.toString()) && isRev(translateToBaseN(k, currentNum))) {
            ans += currentNum
            count++
        }
        currentNum++
    }

    return ans
};

function translateToBaseN(base: number, n: number): string {
    let res: string = ""
    while (n > 0) {
        const rem: number = n % base
        res = rem.toString() + res
        n = Math.floor(n / base)
    }

    return res
}

function isRev(n: string): boolean {
    return n === n.split("").reverse().join("")
}
