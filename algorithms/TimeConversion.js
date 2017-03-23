// WEBSITE: HackerRank
// EXERCISE: Time Conversion
// SOURCE: https://www.hackerrank.com/challenges/time-conversion
// LANGUAGE: JavaScript 

/* 

RULES: Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input Format
A single string containing a time in 12-hour clock format 
(i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12 and 00 <= mm, ss <= 59.

SAMPLE INPUT:
07:05:45PM

EXPECTED OUTPUT:
19:05:45

*/

function main() {
    var time = readLine();
    var amPM = '';
    var militaryTime = ''; 
    var militaryTimeArr = time.split(":");
    amPM = militaryTimeArr[2].slice(2, 4);
    militaryTimeArr[2] = militaryTimeArr[2].slice(0, 2);
    var militaryTimeArrInt = militaryTimeArr.map(function(str) { return parseInt(str); });
    if (amPM == 'PM') {
        if (militaryTimeArrInt[0] < 12) {
            militaryTimeArrInt[0] += 12;
        }
    } else {
        if (militaryTimeArrInt[0] == 12) {
            militaryTimeArrInt[0] = 0;
        }
    }
    for (var i = 0; i < militaryTimeArrInt.length; i++) {
        if (militaryTimeArrInt[i] < 10) {
            militaryTimeArrInt[i] = '0' + militaryTimeArrInt[i];
        }
    } 
    militaryTime = militaryTimeArrInt.join(":");
    console.log(militaryTime);
}
