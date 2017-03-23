// WEBSITE: HackerRank
// EXERCISE: Queues: A Tale of Two Stacks (Cracking the Coding Interview Section)
// SOURCE: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
// LANGUAGE: JavaScript 

/*
RULES: In this challenge, you must first implement a queue using two stacks. 
Then process  queries, where each query is one of the following  types:
1. Enqueue element x into the end of the queue.
2. Dequeue the element at the front of the queue.
3. Print the element at the front of the queue.

The first line contains a single integer, q, denoting the number of queries. 
Each line i of the q subsequent lines contains a single query in the form described 
in the problem statement above. All three queries start with an integer denoting 
the query type, but only query 1 is followed by an additional space-separated value, x, 
denoting the value to be enqueued.

SAMPLE INPUT:
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2

EXPECTED OUTPUT: 
14
14
*/

class Queue {
  
  constructor() {
    
    this.firstStack = [];
    this.secondStack = [];
  }
  
  enqueue(value) {
    this.firstStack.push(value);
  }
  
  dequeue(value) {
    this.prepareStacks();
    return this.secondStack.pop();
  }
  
  prepareStacks() {
    if(this.secondStack.length === 0) {
      while(this.firstStack.length > 0) {
        this.secondStack.push(this.firstStack.pop());
      }
    }
  }
  
  getHead() {
    this.prepareStacks();
    var value = this.secondStack.pop();
    this.secondStack.push(value);
    return value;
  }
}