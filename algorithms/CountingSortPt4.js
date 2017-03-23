// WEBSITE: HackerRank
// EXERCISE: The Full Counting Sort
// SOURCE: https://www.hackerrank.com/challenges/countingsort4
// LANGUAGE: JavaScript

/* 
RULES: You will be given a list that contains both integers and 
strings. Can you print the strings in order of their accompanying 
integers? If the integers for two strings are equal, ensure that 
they are print in the order they appeared in the original list.

The Twist - Your clients just called with an update. They don't 
want you to print the first half of the original array. Instead, 
they want you to print a dash for any element from the first half.

Input Format 
- n, the size of the list ar. 
- n lines follow, each containing an integer x and a string s.

SAMPLE INPUT: 
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

EXPECTED OUTPUT: 
- - - - - to be or not to be - that is the question - - - -
*/


function processData(input) {
    var minValue = 0;
    var maxValue = 99;
    var lines = input.split('\n');
    var n = parseInt(lines.shift(), 10);

    var data = (
         lines
        .splice(0, n)
        .map(function (s) {
            var arr = s.split(' ');
            return { n:parseInt(arr[0], 10), t:arr[1] };
        })
    );

    var res = new Array(maxValue - minValue + 1);
    for (var i = minValue; i <= maxValue; i++) {
        res[i] = { n:0, t:[] };
    }

    var half = Math.floor(n / 2);
    data.forEach(function (e, idx, arr) {
        if (e.n >= minValue && e.n <= maxValue) {
            res[e.n].n++;
            res[e.n].t.push((idx < half) ? '-' : e.t);
        }
    });

    // var half = Math.floor(n / 2);

    var s = [];
    res.forEach(function (e) {
        s = s.concat(e.t);
    });
    process.stdout.write(s.join(' ') + '\n');
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
