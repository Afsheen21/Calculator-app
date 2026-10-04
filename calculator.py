import streamlit as st
import streamlit.components.v1 as components


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Pink Scientific Calculator",
    page_icon="🎀",
    layout="centered"
)


# =========================================================
# CALCULATOR
# =========================================================

calculator = r"""
<!DOCTYPE html>

<html>

<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background: transparent;
}


/* =====================================================
   CALCULATOR BODY
   ===================================================== */

.calculator {

    max-width: 650px;

    margin: 10px auto;

    padding: 18px;

    border-radius: 30px;

    background: linear-gradient(
        145deg,
        #fff0f6,
        #ffd1e3
    );

    box-shadow:
        0 15px 40px rgba(194, 24, 91, 0.25);

    border: 2px solid #f8bbd0;
}


/* =====================================================
   DISPLAY
   ===================================================== */

.display-area {

    background: #fffafd;

    border-radius: 22px;

    padding: 16px;

    margin-bottom: 14px;

    box-shadow:
        inset 0 3px 10px rgba(150, 50, 90, 0.10);

    position: relative;
}


.mode {

    display: inline-block;

    background: #f48fb1;

    color: white;

    padding: 5px 11px;

    border-radius: 10px;

    font-size: 13px;

    font-weight: bold;

    cursor: pointer;

    margin-bottom: 5px;
}


.display {

    width: 100%;

    height: 80px;

    border: none;

    outline: none;

    background: transparent;

    text-align: right;

    font-size: 36px;

    font-weight: bold;

    color: #8e1745;

}


/* =====================================================
   BUTTON GRID
   ===================================================== */

.buttons {

    display: grid;

    grid-template-columns:
        repeat(5, 1fr);

    gap: 9px;
}


/* =====================================================
   NORMAL BUTTONS
   ===================================================== */

button {

    height: 58px;

    border: none;

    border-radius: 15px;

    font-size: 18px;

    font-weight: bold;

    cursor: pointer;

    background: #fff8fb;

    color: #7a1641;

    box-shadow:
        0 4px 8px rgba(160, 60, 100, 0.15);

    transition: 0.15s;
}


button:hover {

    transform: translateY(-2px);

    background: white;

    box-shadow:
        0 7px 13px rgba(160, 60, 100, 0.22);
}


button:active {

    transform: scale(0.94);
}


/* =====================================================
   SCIENTIFIC BUTTONS
   ===================================================== */

.scientific {

    background: #f8bbd0;

    color: #8e1745;
}


.scientific:hover {

    background: #f48fb1;

    color: white;
}


/* =====================================================
   OPERATORS
   ===================================================== */

.operator {

    background: #f48fb1;

    color: white;
}


.operator:hover {

    background: #ec7099;
}


/* =====================================================
   DELETE
   ===================================================== */

.delete {

    background: #f3c1cd;

    color: #ad1457;
}


/* =====================================================
   CLEAR
   ===================================================== */

.clear {

    background: #d81b60;

    color: white;
}


.clear:hover {

    background: #ad1457;
}


/* =====================================================
   EQUAL
   ===================================================== */

.equal {

    background: #ec407a;

    color: white;

    grid-row: span 2;

    height: 125px;
}


.equal:hover {

    background: #d81b60;
}


/* =====================================================
   ZERO
   ===================================================== */

.zero {

    grid-column: span 2;
}


/* =====================================================
   HISTORY
   ===================================================== */

.history {

    margin-top: 14px;

    background: #fff8fb;

    border-radius: 18px;

    padding: 12px 15px;

    color: #8e1745;

    min-height: 65px;

    box-shadow:
        inset 0 2px 7px rgba(150, 50, 90, 0.08);
}


.history-title {

    font-size: 14px;

    font-weight: bold;

    color: #c2185b;

    margin-bottom: 7px;
}


.history-item {

    font-size: 14px;

    padding: 5px 0;

    border-bottom: 1px solid #f8bbd0;

    cursor: pointer;
}


.history-item:hover {

    color: #d81b60;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 600px) {

    .calculator {

        margin: 5px;

        padding: 12px;

        border-radius: 22px;
    }


    button {

        height: 52px;

        font-size: 15px;

        border-radius: 12px;
    }


    .equal {

        height: 113px;
    }


    .display {

        height: 70px;

        font-size: 30px;
    }

}

</style>

</head>


<body>


<div class="calculator">


    <!-- =================================================
         DISPLAY
         ================================================= -->

    <div class="display-area">

        <div
            class="mode"
            id="mode"
            onclick="toggleMode()">
            DEG
        </div>

        <input
            type="text"
            id="display"
            class="display"
            value="0"
            readonly>

    </div>


    <!-- =================================================
         BUTTONS
         ================================================= -->

    <div class="buttons">


        <!-- ROW 1 -->

        <button
            class="scientific"
            onclick="sin()">
            sin
        </button>

        <button
            class="scientific"
            onclick="cos()">
            cos
        </button>

        <button
            class="scientific"
            onclick="tan()">
            tan
        </button>

        <button
            class="scientific"
            onclick="add('(')">
            (
        </button>

        <button
            class="scientific"
            onclick="add(')')">
            )
        </button>


        <!-- ROW 2 -->

        <button
            class="scientific"
            onclick="asin()">
            sin⁻¹
        </button>

        <button
            class="scientific"
            onclick="acos()">
            cos⁻¹
        </button>

        <button
            class="scientific"
            onclick="atan()">
            tan⁻¹
        </button>

        <button
            class="scientific"
            onclick="add('π')">
            π
        </button>

        <button
            class="scientific"
            onclick="add('e')">
            e
        </button>


        <!-- ROW 3 -->

        <button
            class="scientific"
            onclick="sinh()">
            sinh
        </button>

        <button
            class="scientific"
            onclick="cosh()">
            cosh
        </button>

        <button
            class="scientific"
            onclick="tanh()">
            tanh
        </button>

        <button
            class="scientific"
            onclick="absolute()">
            |x|
        </button>

        <button
            class="scientific"
            onclick="useAns()">
            Ans
        </button>


        <!-- ROW 4 -->

        <button
            class="scientific"
            onclick="log()">
            log
        </button>

        <button
            class="scientific"
            onclick="ln()">
            ln
        </button>

        <button
            class="scientific"
            onclick="sqrt()">
            √
        </button>

        <button
            class="scientific"
            onclick="square()">
            x²
        </button>

        <button
            class="scientific"
            onclick="power()">
            xʸ
        </button>


        <!-- ROW 5 -->

        <button
            class="scientific"
            onclick="reciprocal()">
            1/x
        </button>

        <button
            class="scientific"
            onclick="factorial()">
            n!
        </button>

        <button
            class="scientific"
            onclick="percent()">
            %
        </button>

        <button
            class="delete"
            onclick="backspace()">
            ⌫
        </button>

        <button
            class="clear"
            onclick="clearDisplay()">
            AC
        </button>


        <!-- ROW 6 -->

        <button onclick="add('7')">
            7
        </button>

        <button onclick="add('8')">
            8
        </button>

        <button onclick="add('9')">
            9
        </button>

        <button
            class="operator"
            onclick="add('/')">
            ÷
        </button>

        <button
            class="operator"
            onclick="add('*')">
            ×
        </button>


        <!-- ROW 7 -->

        <button onclick="add('4')">
            4
        </button>

        <button onclick="add('5')">
            5
        </button>

        <button onclick="add('6')">
            6
        </button>

        <button
            class="operator"
            onclick="add('-')">
            −
        </button>

        <button
            class="operator"
            onclick="add('+')">
            +
        </button>


        <!-- ROW 8 -->

        <button onclick="add('1')">
            1
        </button>

        <button onclick="add('2')">
            2
        </button>

        <button onclick="add('3')">
            3
        </button>

        <button
            class="operator"
            onclick="toggleSign()">
            ±
        </button>

        <button
            class="equal"
            onclick="calculate()">
            =
        </button>


        <!-- ROW 9 -->

        <button
            class="zero"
            onclick="add('0')">
            0
        </button>

        <button onclick="add('.')">
            .
        </button>

        <button
            class="scientific"
            onclick="add(',')">
            ,
        </button>


    </div>


    <!-- =================================================
         HISTORY
         ================================================= -->

    <div class="history">

        <div class="history-title">
            History (tap to reuse)
        </div>

        <div id="historyList">
            No calculations yet
        </div>

    </div>


</div>



<script>


// =========================================================
// VARIABLES
// =========================================================

let display =
    document.getElementById("display");

let modeElement =
    document.getElementById("mode");

let historyList =
    document.getElementById("historyList");

let history = [];

let answer = 0;

let degreeMode = true;


// =========================================================
// ADD VALUE
// =========================================================

function add(value) {

    if (
        display.value === "0" ||
        display.value === "Error"
    ) {

        display.value = "";

    }

    display.value += value;
}


// =========================================================
// CLEAR
// =========================================================

function clearDisplay() {

    display.value = "0";
}


// =========================================================
// BACKSPACE
// =========================================================

function backspace() {

    if (
        display.value.length <= 1 ||
        display.value === "Error"
    ) {

        display.value = "0";

    } else {

        display.value =
            display.value.slice(0, -1);

    }
}


// =========================================================
// DEG / RAD
// =========================================================

function toggleMode() {

    degreeMode = !degreeMode;

    modeElement.innerText =
        degreeMode ? "DEG" : "RAD";
}


// =========================================================
// ANGLE CONVERSION
// =========================================================

function toRadians(number) {

    if (degreeMode) {

        return number * Math.PI / 180;

    }

    return number;
}


function fromRadians(number) {

    if (degreeMode) {

        return number * 180 / Math.PI;

    }

    return number;
}


// =========================================================
// PREPARE EXPRESSION
// =========================================================

function prepareExpression(expression) {

    expression =
        expression.replaceAll("π", "Math.PI");

    expression =
        expression.replaceAll("e", "Math.E");

    expression =
        expression.replaceAll("×", "*");

    expression =
        expression.replaceAll("÷", "/");

    /*
       Convert xʸ operator to JavaScript **
    */

    expression =
        expression.replaceAll("^", "**");

    return expression;
}


// =========================================================
// CALCULATE
// =========================================================

function calculate() {

    try {

        let expression =
            display.value;

        let prepared =
            prepareExpression(expression);

        let result =
            eval(prepared);

        if (
            typeof result !== "number" ||
            !isFinite(result)
        ) {

            display.value = "Error";

            return;
        }

        result =
            Number(result.toPrecision(12));

        display.value =
            result.toString();

        answer = result;

        addHistory(
            expression + " = " + result
        );

    }

    catch {

        display.value = "Error";

    }
}


// =========================================================
// SIN
// =========================================================

function sin() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.sin(toRadians(number));

}


// =========================================================
// COS
// =========================================================

function cos() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.cos(toRadians(number));

}


// =========================================================
// TAN
// =========================================================

function tan() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.tan(toRadians(number));

}


// =========================================================
// INVERSE SIN
// =========================================================

function asin() {

    let number =
        parseFloat(display.value);

    if (
        isNaN(number) ||
        number < -1 ||
        number > 1
    ) {

        display.value = "Error";

        return;
    }

    display.value =
        fromRadians(Math.asin(number));

}


// =========================================================
// INVERSE COS
// =========================================================

function acos() {

    let number =
        parseFloat(display.value);

    if (
        isNaN(number) ||
        number < -1 ||
        number > 1
    ) {

        display.value = "Error";

        return;
    }

    display.value =
        fromRadians(Math.acos(number));

}


// =========================================================
// INVERSE TAN
// =========================================================

function atan() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        fromRadians(Math.atan(number));

}


// =========================================================
// HYPERBOLIC SIN
// =========================================================

function sinh() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.sinh(number);

}


// =========================================================
// HYPERBOLIC COS
// =========================================================

function cosh() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.cosh(number);

}


// =========================================================
// HYPERBOLIC TAN
// =========================================================

function tanh() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.tanh(number);

}


// =========================================================
// ABSOLUTE VALUE
// =========================================================

function absolute() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.abs(number);

}


// =========================================================
// SQUARE ROOT
// =========================================================

function sqrt() {

    let number =
        parseFloat(display.value);

    if (
        isNaN(number) ||
        number < 0
    ) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.sqrt(number);

}


// =========================================================
// SQUARE
// =========================================================

function square() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        number ** 2;

}


// =========================================================
// POWER xʸ
// =========================================================

function power() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value += "^";

}


// =========================================================
// RECIPROCAL
// =========================================================

function reciprocal() {

    let number =
        parseFloat(display.value);

    if (
        isNaN(number) ||
        number === 0
    ) {

        display.value = "Error";

        return;
    }

    display.value =
        1 / number;

}


// =========================================================
// FACTORIAL
// =========================================================

function factorial() {

    let number =
        Number(display.value);

    if (
        !Number.isInteger(number) ||
        number < 0 ||
        number > 170
    ) {

        display.value = "Error";

        return;
    }

    let result = 1;

    for (
        let i = 2;
        i <= number;
        i++
    ) {

        result *= i;

    }

    display.value =
        result;

}


// =========================================================
// PERCENT
// =========================================================

function percent() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        number / 100;

}


// =========================================================
// PLUS / MINUS
// =========================================================

function toggleSign() {

    let number =
        parseFloat(display.value);

    if (isNaN(number)) {

        display.value = "Error";

        return;
    }

    display.value =
        -number;

}


// =========================================================
// ANSWER
// =========================================================

function useAns() {

    add(answer.toString());

}


// =========================================================
// LOG
// =========================================================

function log() {

    let number =
        parseFloat(display.value);

    if (
        isNaN(number) ||
        number <= 0
    ) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.log10(number);

}


// =========================================================
// NATURAL LOG
// =========================================================

function ln() {

    let number =
        parseFloat(display.value);

    if (
        isNaN(number) ||
        number <= 0
    ) {

        display.value = "Error";

        return;
    }

    display.value =
        Math.log(number);

}


// =========================================================
// HISTORY
// =========================================================

function addHistory(item) {

    history.unshift(item);

    if (history.length > 5) {

        history.pop();

    }

    historyList.innerHTML = "";

    history.forEach(
        function(item) {

            let div =
                document.createElement("div");

            div.className =
                "history-item";

            div.innerText =
                item;

            div.onclick =
                function() {

                    display.value =
                        item.split(" = ")[1];

                };

            historyList.appendChild(div);

        }
    );

}


// =========================================================
// KEYBOARD SUPPORT
// =========================================================

document.addEventListener(
    "keydown",
    function(event) {

        let key =
            event.key;


        // Numbers

        if (
            key >= "0" &&
            key <= "9"
        ) {

            add(key);

        }


        // Operators

        else if (
            key === "+" ||
            key === "-" ||
            key === "*" ||
            key === "/" ||
            key === "." ||
            key === "(" ||
            key === ")"
        ) {

            add(key);

        }


        // Enter

        else if (
            key === "Enter" ||
            key === "="
        ) {

            calculate();

        }


        // Backspace

        else if (
            key === "Backspace"
        ) {

            backspace();

        }


        // Escape

        else if (
            key === "Escape"
        ) {

            clearDisplay();

        }

    }
);


</script>

</body>

</html>
"""


# =========================================================
# DISPLAY CALCULATOR
# =========================================================

components.html(
    calculator,
    height=1150,
    scrolling=True
)



