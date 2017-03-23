// WEBSITE: HackerRank
// EXERCISE: Stacks: Balanced Brackets (Cracking the Coding Interview Section)
// SOURCE: https://www.hackerrank.com/challenges/ctci-balanced-brackets
// LANGUAGE: JavaScript 

/* RULES: Given  strings of brackets, determine whether each sequence of brackets is balanced. 
If a string is balanced, print YES on a new line; otherwise, print NO on a new line.
 
The first line contains a single integer, n, denoting the number of strings. 
Each line i of the n subsequent lines consists of a single string, s, 
denoting a sequence of brackets.

SAMPLE INPUT:
3
{[()]}
{[(])}
{{[[(())]]}}

EXPECTED OUTPUT: 
YES
NO
YES */

function is_balanced(expression) {
    let stack = []; 
    // convert expression input string into array split by character
    expArray = expression.split(''); 
    
    // loop through expArray, adding matching right brackets to stack 
    // once right brackets reached in expArray, compare current index with top of stack
    // if match, pop top off stack and loop to next index
    for (let i = 0; i < expArray.length; i++) {
        if (expArray[i] === '{') {
            stack.push('}');
        } else if (expArray[i] === '[') {
            stack.push(']');
        } else if (expArray[i] === '(') {
            stack.push(')');
        } else {
            if ((stack.length === 0) || expArray[i] !== stack[stack.length-1]) {
                return false;
            }
            stack.pop();
        }
    };

    // if reaches this point, stack should be empty and return true
    return (stack.length === 0);
}