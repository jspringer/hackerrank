// WEBSITE: HackerRank
// EXERCISE: Hash Tables: Ransom Note (Cracking the Coding Interview Section)
// SOURCE: https://www.hackerrank.com/challenges/ctci-ransom-note
// LANGUAGE: JavaScript 

/* 
RULES: Given the words in the magazine and the words in the ransom note, 
print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
otherwise, print No.

The first line contains two space-separated integers describing the respective values 
of m (the number of words in the magazine) and n (the number of words in the ransom note). 
The second line contains m space-separated strings denoting the words present in the magazine. 
The third line contains n space-separated strings denoting the words present in the ransom note.

SAMPLE INPUT: 
6 4
give me one grand today night
give one grand today

EXPECTED OUTPUT:
Yes

Solution using a hash table as requested
*/

if(n > m)
    return console.log('No');
    
var map = {};

while(magazine.length) {
    let word = magazine.shift();

    if(map.hasOwnProperty(word))
        map[word]++;
    else
        map[word] = 1;
}

while(ransom.length) {
    let word = ransom.shift();

    if(!map.hasOwnProperty(word) || map[word] < 1)
        return console.log('No');
    else
        map[word]--;
}

console.log('Yes');