let a = Math.floor(Math.random() * 100);
console.log(`Исходное a = ${a}`);

//if...else
let resultIf;
// Первое условие: (a > 10 ? a : a * 2) > 5
let temp = a > 10 ? a : a * 2;
if (temp > 5) {
    resultIf = 2 * a + 1;
} else {
    // Второе условие: (a < 3 ? 1 : 2 * (a - 2)) > 4 ? 5 : (a % 2 == 0 ? 6 : 7)
    let temp2 = a < 3 ? 1 : 2 * (a - 2);
    if (temp2 > 4) {
        resultIf = 5;
    } else {
        resultIf = (a % 2 === 0) ? 6 : 7;
    }
}
console.log(`Результат (if...else): ${resultIf}`);

//switch (true)
let resultSwitch;
switch (true) {
    case (a > 10 ? a : a * 2) > 5:
        resultSwitch = 2 * a + 1;
        break;
    case (a < 3 ? 1 : 2 * (a - 2)) > 4:
        resultSwitch = 5;
        break;
    default:
        resultSwitch = (a % 2 === 0) ? 6 : 7;
}
console.log(`Результат (switch): ${resultSwitch}`);