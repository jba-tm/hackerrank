'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getMaxLessThanK(n, k){
    let result = 0
    let counter = 0
    for(let i=1; i<n;i++){
        for(let j=i+1;j<=n;j++){
            counter = i&j
            if(result<counter && counter<k){
                result = counter
            }
        }
    }
    return result
}

function main() {
    const q = 3;

    for (let i = 0; i < q; i++) {
        const [n, k] = [8, 5];
        console.log(getMaxLessThanK(n, k));
    }
}
