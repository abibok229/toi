function manyChecksIfElse() {
    let a = Math.floor(Math.random() * 20) + 1;
    console.log(`a = ${a}`);

    let result = "";

    // Первая часть: a > 10 ? 'a is bigger than 10' : 'a is less than or equal to 10 ' + (a === 5 ? 'an example of a special case' : '')
    if (a > 10) {
        result += 'a is bigger than 10';
    } else {
        result += 'a is less than or equal to 10 ';
        if (a === 5) {
            result += 'an example of a special case';
        }
    }

    // Вторая часть: (a === 15 ? 'but a is not 15' : '')
    if (a === 15) {
        result += ' but a is not 15';
    }

    // Третья часть: (a > 5 ? 'and a is greater than 5' : 'and a is less than or equal to 5 ')
    if (a > 5) {
        result += ' and a is greater than 5';
    } else {
        result += ' and a is less than or equal to 5 ';
    }

    // Четвертая часть: (a % 2 ? ' and a is odd' : ' and a is even ')
    if (a % 2) {
        result += ' and a is odd';
    } else {
        result += ' and a is even';
    }

    return result;
}

//switch (true)
function manyChecksSwitch() {
    let a = Math.floor(Math.random() * 20) + 1;
    console.log(`a = ${a}`);

    let result = "";

    switch (true) {
        case a > 10:
            result += 'a is bigger than 10';
            break;
        default:
            result += 'a is less than or equal to 10 ';
            if (a === 5) result += 'an example of a special case';
    }

    if (a === 15) result += 'but a is not 15';

    switch (true) {
        case a > 5:
            result += ' and a is greater than 5';
            break;
        default:
            result += ' and a is less than or equal to 5 ';
    }

    switch (true) {
        case a % 2 !== 0:
            result += ' and a is odd';
            break;
        default:
            result += ' and a is even';
    }

    return result;
}

console.log("--- if...else ---");
console.log(manyChecksIfElse());
console.log("--- switch ---");
console.log(manyChecksSwitch());