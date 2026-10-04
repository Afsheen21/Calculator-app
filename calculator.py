
import streamlit as st
import streamlit.components.v1 as components

# Page settings
st.set_page_config(
    page_title="Pink Scientific Calculator",
    page_icon="🎀",
    layout="centered"
)

# Calculator
calculator = """
<!DOCTYPE html>
<html>
<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: transparent;
}

/* Calculator box */
.calculator {
    max-width: 430px;
    margin: 20px auto;
    padding: 25px;
    border-radius: 28px;

    background: linear-gradient(
        145deg,
        #fff0f6,
        #ffd6e7
    );

    box-shadow:
        0 15px 35px rgba(190, 70, 120, 0.25);

    border: 1px solid #ffc1d8;
}

/* Title */
.title {
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    color: #c2185b;
    margin-bottom: 18px;
}

/* Display */
.display {
    width: 100%;
    height: 75px;

    border: none;
    border-radius: 18px;

    padding: 12px 18px;

    font-size: 30px;
    font-weight: bold;
    text-align: right;

    color: #8e1745;
    background: white;

    box-shadow:
        inset 0 3px 8px rgba(150, 50, 90, 0.12),
        0 5px 12px rgba(150, 50, 90, 0.12);

    margin-bottom: 18px;
}

/* Button grid */
.buttons {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

/* Normal buttons */
button {
    height: 58px;

    border: none;
    border-radius: 16px;

    font-size: 20px;
    font-weight: bold;

    cursor: pointer;

    color: #7a1641;
    background: white;

    box-shadow:
        0 5px 10px rgba(160, 60, 100, 0.15);

    transition: 0.15s;
}

/* Hover */
button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 8px 15px rgba(160, 60, 100, 0.22);

    background: #fff7fa;
}

/* Click effect */
button:active {
    transform: scale(0.94);
}

/* Operators */
.operator {
    background: #f48fb1;
    color: white;
}

.operator:hover {
    background: #ec7099;
}

/* Scientific buttons */
.scientific {
    background: #f8bbd0;
    color: #8e1745;
}

.scientific:hover {
    background: #f48fb1;
    color: white;
}

/* Clear button */
.clear {
    background: #d81b60;
    color: white;
}

.clear:hover {
    background: #ad1457;
}

/* Equal button */
.equal {
    background: #c2185b;
    color: white;
}

.equal:hover {
    background: #ad1457;
}

/* Special button */
.special {
    background: #fce4ec;
    color: #ad1457;
}

/* Mobile */
@media (max-width: 450px) {

    .calculator {
        margin: 10px;
        padding: 18px;
    }

    button {
        height: 52px;
        font-size: 18px;
    }

    .display {
        height: 65px;
        font-size: 25px;
    }

}

</style>

</head>

<body>

<div class="calculator">

    <div class="title">
        🎀 Scientific Calculator
    </div>

    <input
        type="text"
        id="display"
        class="display"
        readonly
    >

    <div class="buttons">

        <!-- Row 1 -->

        <button
            class="clear"
            onclick="clearDisplay()">
            C
        </button>

        <button
            class="special"
            onclick="backspace()">
            ⌫
        </button>

        <button
            class="scientific"
            onclick="sqrt()">
            √
        </button>

        <button
            class="operator"
            onclick="add('/')">
            ÷
        </button>


        <!-- Row 2 -->

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
            onclick="add('*')">
            ×
        </button>


        <!-- Row 3 -->

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


        <!-- Row 4 -->

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
            onclick="add('+')">
            +
        </button>


        <!-- Row 5 -->

        <button onclick="add('0')">
            0
        </button>

        <button onclick="add('.')">
            .
        </button>

        <button
            class="scientific"
            onclick="square()">
            x²
        </button>

        <button
            class="equal"
            onclick="calculate()">
            =
        </button>


        <!-- Scientific functions -->

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
            onclick="log()">
            log
        </button>

    </div>

</div>


<script>

let display = document.getElementById("display");


/* Add value */

function add(value) {

    display.value += value;

}


/* Clear */

function clearDisplay() {

    display.value = "";

}


/* Backspace */

function backspace() {

    display.value =
        display.value.slice(0, -1);

}


/* Calculate */

function calculate() {

    try {

        let expression =
            display.value;

        let result =
            eval(expression);

        if (!isFinite(result)) {

            display.value = "Error";

        } else {

            display.value = result;

        }

    }

    catch {

        display.value = "Error";

    }

}


/* Square root */

function sqrt() {

    try {

        let number =
            parseFloat(display.value);

        if (number < 0) {

            display.value = "Error";
            return;

        }

        display.value =
            Math.sqrt(number);

    }

    catch {

        display.value = "Error";

    }

}


/* Square */

function square() {

    try {

        let number =
            parseFloat(display.value);

        display.value =
            number * number;

    }

    catch {

        display.value = "Error";

    }

}


/* Sine */

function sin() {

    try {

        let number =
            parseFloat(display.value);

        display.value =
            Math.sin(
                number * Math.PI / 180
            );

    }

    catch {

        display.value = "Error";

    }

}


/* Cosine */

function cos() {

    try {

        let number =
            parseFloat(display.value);

        display.value =
            Math.cos(
                number * Math.PI / 180
            );

    }

    catch {

        display.value = "Error";

    }

}


/* Tangent */

function tan() {

    try {

        let number =
            parseFloat(display.value);

        display.value =
            Math.tan(
                number * Math.PI / 180
            );

    }

    catch {

        display.value = "Error";

    }

}


/* Log */

function log() {

    try {

        let number =
            parseFloat(display.value);

        if (number <= 0) {

            display.value = "Error";
            return;

        }

        display.value =
            Math.log10(number);

    }

    catch {

        display.value = "Error";

    }

}


/* Keyboard support */

document.addEventListener(
    "keydown",
    function(event) {

        let key = event.key;


        /* Numbers */

        if (
            key >= "0" &&
            key <= "9"
        ) {

            add(key);

        }


        /* Operators */

        else if (
            key === "+" ||
            key === "-" ||
            key === "*" ||
            key === "/" ||
            key === "."
        ) {

            add(key);

        }


        /* Enter */

        else if (
            key === "Enter" ||
            key === "="
        ) {

            calculate();

        }


        /* Backspace */

        else if (
            key === "Backspace"
        ) {

            backspace();

        }


        /* Escape */

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

# Display calculator
components.html(
    calculator,
    height=620,
    scrolling=False
)


