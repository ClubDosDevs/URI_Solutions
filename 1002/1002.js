var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

    let A = parseFloat(lines.shift())
    let pi = 3.14159 
    let result = parseFloat((A*A)*pi).toFixed(4)
    console.log('A='+result)