
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Scientific Calculator - Afsheen Fatima",
    page_icon="\U0001F9EE",
    layout="centered",
)

# Pink page background; hide Streamlit's own header and footer.
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(160deg, #ffe3ea, #f8bfd0); }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { max-width: 480px; padding-top: 0.5rem; padding-bottom: 0; }
    iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

CALCULATOR_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Scientific Calculator - Afsheen Fatima</title>

<style>
  /* ---------- Colour tokens (light theme, dark theme below) ---------- */
  :root {
    --bg1: #ffe3ea;  --bg2: #f8bfd0;  --body: #f7a8c0;
    --lcd: #d9e4cf;  --lcd-text: #1b231a;
    --key: #ffffff;  --key-text: #5a1230;
    --fn: #ffd3df;   --fn-text: #7a0f33;
    --mod: #ff7aa8;  --red: #e5384f;  --eq: #c2185b;
    --ink: #8a1538;  --panel: #fff3f6;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg1: #2a1018;  --bg2: #4a1a2c;  --body: #8a3556;
      --lcd: #b9c7ad;  --lcd-text: #142013;
      --key: #3a2530;  --key-text: #ffe3ea;
      --fn: #6e2a45;   --fn-text: #ffd3df;
      --mod: #d81b60;  --red: #c62839;  --eq: #d81b60;
      --ink: #ffc2d4;  --panel: #3a2530;
    }
  }
  :root[data-theme="dark"] {
    --bg1: #2a1018;  --bg2: #4a1a2c;  --body: #8a3556;
    --lcd: #b9c7ad;  --lcd-text: #142013;
    --key: #3a2530;  --key-text: #ffe3ea;
    --fn: #6e2a45;   --fn-text: #ffd3df;
    --mod: #d81b60;  --red: #c62839;  --eq: #d81b60;
    --ink: #ffc2d4;  --panel: #3a2530;
  }

  /* ---------- Page ---------- */
  :root {
    box-sizing: border-box;
    padding-top: env(safe-area-inset-top, 0px);
    padding-bottom: env(safe-area-inset-bottom, 0px);
  }
  html { scroll-padding-top: env(safe-area-inset-top, 0px); }
  *, *::before, *::after { box-sizing: inherit; }

  body {
    margin: 0;
    min-height: 100vh;
    padding: 14px;
    display: flex;
    justify-content: center;
    background-color: var(--bg1);
    background-image: linear-gradient(160deg, var(--bg1), var(--bg2));
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  .wrap { width: 100%; max-width: 400px; }

  h1 {
    margin: 4px 0 0;
    text-align: center;
    font-size: 30px;
    letter-spacing: 0.5px;
    color: var(--ink);
  }
  .model {
    margin: 2px 0 10px;
    text-align: center;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--ink);
    opacity: 0.8;
  }

  /* ---------- Calculator body and screen ---------- */
  .calc {
    padding: 14px;
    border-radius: 22px;
    background: var(--body);
    box-shadow: 0 12px 30px rgba(120, 20, 60, 0.35), inset 0 2px 0 rgba(255, 255, 255, 0.4);
  }
  .lcd {
    padding: 8px 12px;
    border-radius: 12px;
    background: var(--lcd);
    color: var(--lcd-text);
    font-family: "Courier New", monospace;
    box-shadow: inset 0 3px 8px rgba(0, 0, 0, 0.35);
  }
  .status {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    min-height: 16px;
    font-size: 11px;
    font-weight: 700;
  }
  .status span {
    padding: 0 5px;
    border-radius: 3px;
    background: var(--lcd-text);
    color: var(--lcd);
  }
  #expr {
    width: 100%;
    padding: 4px 0;
    border: 0;
    outline: 0;
    background: transparent;
    color: inherit;
    caret-color: var(--lcd-text);
    font: 600 22px "Courier New", monospace;
  }
  #res {
    min-height: 40px;
    overflow-x: auto;
    white-space: nowrap;
    text-align: right;
    font-size: 30px;
    font-weight: 800;
  }
  #res.err { color: #b00020; font-size: 24px; }

  /* ---------- Keys ---------- */
  .grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
    margin-top: 12px;
  }
  button {
    height: 44px;
    padding: 0;
    border: 0;
    border-radius: 12px;
    background: var(--fn);
    color: var(--fn-text);
    font: 700 15px system-ui, sans-serif;
    box-shadow: 0 3px 0 rgba(0, 0, 0, 0.25);
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
  }
  button:active { transform: translateY(2px); box-shadow: 0 1px 0 rgba(0, 0, 0, 0.25); }
  button.num { background: var(--key); color: var(--key-text); font-size: 18px; }
  button.op  { font-size: 18px; }
  button.mod.on { background: var(--mod); color: #fff; }
  button.red { background: var(--red); color: #fff; }
  button.eq  { background: var(--eq);  color: #fff; font-size: 22px; }

  /* ---------- Help text and history ---------- */
  .help { margin: 10px 2px 0; font-size: 12px; line-height: 1.5; color: var(--ink); }
  .hist {
    max-height: 150px;
    margin-top: 10px;
    padding: 6px 10px;
    overflow-y: auto;
    border-radius: 12px;
    background: var(--panel);
  }
  .hist:empty { display: none; }
  .hist div {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding: 5px 2px;
    border-bottom: 1px dashed rgba(138, 21, 56, 0.25);
    color: var(--key-text);
    font: 13px "Courier New", monospace;
    cursor: pointer;
  }
  .hist div:last-child { border: 0; }
</style>
</head>

<body>
<div class="wrap">
  <h1>Afsheen Fatima</h1>
  <div class="model">SCIENTIFIC CALCULATOR</div>

  <div class="calc">
    <div class="lcd">
      <div class="status" id="stat"></div>
      <input id="expr" type="text" inputmode="none" autocomplete="off"
             autocapitalize="off" spellcheck="false" aria-label="Expression" autofocus>
      <div id="res"></div>
    </div>
    <div class="grid" id="grid"></div>
  </div>

  <div class="help">
    <b>Keyboard:</b> type numbers and functions (e.g. <code>sin(30)</code>,
    <code>sqrt(16)</code>, <code>5!</code>, <code>2^10</code>) ·
    <b>Enter</b> = result · <b>Backspace</b> deletes one character ·
    <b>← →</b> move the cursor · <b>Esc</b> clears ·
    click a history line to reuse it.
  </div>
  <div class="hist" id="hist"></div>
</div>

<script>
/* =====================================================================
   Scientific Calculator - Afsheen Fatima
   1. State            4. Editing helpers
   2. Evaluator        5. Keypad
   3. Result display   6. Physical keyboard and history
   ===================================================================== */

const inp  = document.getElementById('expr');
const res  = document.getElementById('res');
const grid = document.getElementById('grid');

/* ---------- 1. State ---------- */
let angle   = 'DEG';    // DEG | RAD | GRAD
let shift   = false;    // SHIFT key pressed: next key uses its second function
let hyp     = false;    // hyp key pressed: next trig key is hyperbolic
let ans     = 0;        // last answer
let mem     = 0;        // memory value
let fresh   = false;    // a result is showing: next key starts a new calculation
let lastVal = null;     // last result, used by the S<=>D key
let mode    = 'dec';    // result display: dec | frac | mixed | dms
let entries = [];       // [expression, result] pairs shown in the history list

/* ---------- 2. Expression evaluator (no eval) ---------- */

/** Turns display symbols into plain text the tokenizer understands. */
function normalise(text) {
  return text
    // degrees-minutes-seconds: 30°15′10″ -> (30+15/60+10/3600)
    .replace(/(\d+\.?\d*)°(?:(\d+\.?\d*)′)?(?:(\d+\.?\d*)″)?/g,
             (m, d, min, sec) => `(${d}+${min || 0}/60+${sec || 0}/3600)`)
    .replace(/×/g, '*')
    .replace(/÷/g, '/')
    .replace(/[−–]/g, '-')
    .replace(/π/g, 'pi')
    .replace(/ˣ√/g, '#')                       // nth-root operator
    .replace(/√/g, 'sqrt')
    .replace(/∛/g, 'cbrt')
    .replace(/(sinh|cosh|tanh|sin|cos|tan)⁻¹/g, 'a$1')   // inverse functions
    .replace(/²/g, '^2')
    .replace(/³/g, '^3')
    .replace(/\s+/g, '');
}

/** Splits text into number (n), word (w) and operator (o) tokens. */
function tokenize(text) {
  const tokens = [];
  let i = 0;
  while (i < text.length) {
    const number = /(\d+\.?\d*|\.\d+)(E[+-]?\d+)?/y;
    number.lastIndex = i;
    let m = number.exec(text);
    if (m) {
      tokens.push({ t: 'n', v: parseFloat(m[0]) });
      i = number.lastIndex;
      continue;
    }
    const word = /[A-Za-z]+/y;
    word.lastIndex = i;
    m = word.exec(text);
    if (m) {
      tokens.push({ t: 'w', v: m[0] });
      i = word.lastIndex;
      continue;
    }
    if ('+-*/^()!%#'.includes(text[i])) {
      tokens.push({ t: 'o', v: text[i] });
      i++;
      continue;
    }
    throw new Error('Syntax ERROR');
  }
  return tokens;
}

const hasKey = (obj, key) => Object.prototype.hasOwnProperty.call(obj, key);

/** Evaluates an expression. Returns a number, or null for empty input. */
function evaluate(source) {
  const tokens = tokenize(normalise(source));
  if (!tokens.length) return null;

  let pos = 0;
  const peek = () => tokens[pos];
  const next = () => tokens[pos++];
  const isOp = (v) => peek() && peek().t === 'o' && peek().v === v;
  const fail = (message) => { throw new Error(message); };
  const mathError = () => fail('Math ERROR');

  // angle conversions
  const toRad = (x) => angle === 'DEG' ? x * Math.PI / 180 : angle === 'GRAD' ? x * Math.PI / 200 : x;
  const fromRad = (x) => angle === 'DEG' ? x * 180 / Math.PI : angle === 'GRAD' ? x * 200 / Math.PI : x;
  const tidy = (x) => Math.abs(x) < 1e-15 ? 0 : x;       // sin(180°) -> 0, not 1e-16

  const functions = {
    sin: (x) => tidy(Math.sin(toRad(x))),
    cos: (x) => tidy(Math.cos(toRad(x))),
    tan: (x) => {
      const r = toRad(x);
      if (Math.abs(Math.cos(r)) < 1e-14) mathError();   // tan(90°)
      return tidy(Math.tan(r));
    },
    asin: (x) => { if (Math.abs(x) > 1) mathError(); return tidy(fromRad(Math.asin(x))); },
    acos: (x) => { if (Math.abs(x) > 1) mathError(); return tidy(fromRad(Math.acos(x))); },
    atan: (x) => tidy(fromRad(Math.atan(x))),
    sinh: Math.sinh,
    cosh: Math.cosh,
    tanh: Math.tanh,
    asinh: Math.asinh,
    acosh: (x) => { if (x < 1) mathError(); return Math.acosh(x); },
    atanh: (x) => { if (Math.abs(x) >= 1) mathError(); return Math.atanh(x); },
    log:  (x) => { if (x <= 0) mathError(); return Math.log10(x); },
    ln:   (x) => { if (x <= 0) mathError(); return Math.log(x); },
    sqrt: (x) => { if (x < 0) mathError(); return Math.sqrt(x); },
    cbrt: Math.cbrt,
    abs:  Math.abs,
  };
  const constants = { pi: Math.PI, e: Math.E, Ans: ans, M: mem };

  function factorial(n) {
    if (n < 0 || n !== Math.floor(n) || n > 170) mathError();
    let result = 1;
    for (let i = 2; i <= n; i++) result *= i;
    return result;
  }

  function raisePower(base, exponent) {
    if (base === 0 && exponent <= 0) mathError();
    if (base < 0 && exponent !== Math.floor(exponent)) mathError();
    return Math.pow(base, exponent);
  }

  function nthRoot(index, value) {
    if (index === 0) mathError();
    if (value < 0) {
      if (Number.isInteger(index) && index % 2 !== 0) return -Math.pow(-value, 1 / index);
      mathError();
    }
    return Math.pow(value, 1 / index);
  }

  function combination(kind, n, r) {
    const valid = n === Math.floor(n) && r === Math.floor(r) && n >= 0 && r >= 0 && r <= n && n <= 1000;
    if (!valid) mathError();
    let result = 1;
    if (kind === 'nPr') {
      for (let i = 0; i < r; i++) result *= n - i;
    } else {
      r = Math.min(r, n - r);
      for (let i = 1; i <= r; i++) result = result * (n - r + i) / i;
      result = Math.round(result);
    }
    return result;
  }

  // Can the next token begin a value? (used for implicit multiplication: 2π, 3(4+1))
  function startsValue() {
    const t = peek();
    return t && (t.t === 'n' || (t.t === 'w' && t.v !== 'nPr' && t.v !== 'nCr') || (t.t === 'o' && t.v === '('));
  }

  // Grammar, lowest to highest precedence:
  // expression -> term -> unary -> permutation -> power -> postfix -> primary
  function expression() {
    let value = term();
    while (isOp('+') || isOp('-')) {
      const op = next().v;
      const right = term();
      value = op === '+' ? value + right : value - right;
    }
    return value;
  }

  function term() {
    let value = unary();
    for (;;) {
      if (isOp('*') || isOp('/')) {
        const op = next().v;
        const right = unary();
        if (op === '/') {
          if (right === 0) mathError();
          value /= right;
        } else {
          value *= right;
        }
      } else if (startsValue()) {
        value *= unary();
      } else {
        return value;
      }
    }
  }

  function unary() {
    if (isOp('-')) { next(); return -unary(); }
    if (isOp('+')) { next(); return unary(); }
    return permutation();
  }

  function permutation() {
    let value = power();
    while (peek() && peek().t === 'w' && (peek().v === 'nPr' || peek().v === 'nCr')) {
      const kind = next().v;
      value = combination(kind, value, power());
    }
    return value;
  }

  function power() {
    const base = postfix();
    if (isOp('^')) {
      next();
      return raisePower(base, exponentOperand());
    }
    if (isOp('#')) {
      next();
      return nthRoot(base, postfix());
    }
    return base;
  }

  function exponentOperand() {
    if (isOp('-')) { next(); return -exponentOperand(); }
    if (isOp('+')) { next(); return exponentOperand(); }
    return power();
  }

  function postfix() {
    let value = primary();
    for (;;) {
      if (isOp('!')) { next(); value = factorial(value); }
      else if (isOp('%')) { next(); value /= 100; }
      else return value;
    }
  }

  // Parses "( ... )"; a missing closing bracket at the end is accepted.
  function group() {
    const value = expression();
    if (isOp(')')) next();
    else if (peek()) fail('Syntax ERROR');
    return value;
  }

  function primary() {
    const token = next();
    if (!token) fail('Syntax ERROR');

    if (token.t === 'n') return token.v;
    if (token.t === 'o' && token.v === '(') return group();

    if (token.t === 'w') {
      if (hasKey(constants, token.v)) return constants[token.v];
      if (hasKey(functions, token.v)) {
        let argument;
        if (isOp('(')) {
          next();
          argument = group();
        } else {                                  // sin30, sqrt9 without brackets
          let sign = 1;
          while (isOp('-')) { next(); sign = -sign; }
          argument = sign * postfix();
        }
        return functions[token.v](argument);
      }
    }
    return fail('Syntax ERROR');
  }

  const value = expression();
  if (pos < tokens.length) fail('Syntax ERROR');
  if (typeof value !== 'number' || !isFinite(value)) mathError();
  return value;
}

/* ---------- 3. Result display ---------- */

/** Normal display: 12 significant digits, scientific form for very large/small. */
function format(value) {
  if (value === 0) return '0';
  const abs = Math.abs(value);
  if (abs >= 1e10 || abs < 1e-6) {
    let [mantissa, exponent] = value.toExponential(9).split('e');
    if (mantissa.includes('.')) mantissa = mantissa.replace(/0+$/, '').replace(/\.$/, '');
    return `${mantissa}×10^${parseInt(exponent)}`;
  }
  return String(parseFloat(value.toPrecision(12)));
}

/** Decimal -> fraction using continued fractions. Returns null if not a neat fraction. */
function toFraction(value) {
  if (Number.isInteger(value) || Math.abs(value) > 1e9) return null;
  const x = Math.abs(value);
  let h1 = 1, h0 = 0, k1 = 0, k0 = 1, rest = x;
  for (let i = 0; i < 40; i++) {
    const a = Math.floor(rest);
    [h1, h0] = [a * h1 + h0, h1];
    [k1, k0] = [a * k1 + k0, k1];
    if (Math.abs(x - h1 / k1) < 1e-11 * Math.max(1, x) || k1 > 1e5) break;
    rest = 1 / (rest - a);
  }
  if (Math.abs(x - h1 / k1) > 1e-9 * Math.max(1, x) || k1 === 1) return null;
  const sign = value < 0 ? '-' : '';
  if (mode === 'mixed' && h1 > k1) return `${sign}${Math.floor(h1 / k1)} ${h1 % k1}/${k1}`;
  return `${sign}${h1}/${k1}`;
}

/** Decimal degrees -> degrees, minutes, seconds. */
function toDMS(value) {
  const sign = value < 0 ? '-' : '';
  value = Math.abs(value);
  let d = Math.floor(value + 1e-12);
  let m = Math.floor((value - d) * 60 + 1e-9);
  let s = Math.round(((value - d) * 60 - m) * 60 * 1000) / 1000;
  if (s >= 60) { s = 0; m++; }
  if (m >= 60) { m = 0; d++; }
  return `${sign}${d}°${m}′${s}″`;
}

/** Shows a value in the current display mode (S<=>D key). */
function show(value) {
  if (mode === 'frac' || mode === 'mixed') {
    const fraction = toFraction(value);
    if (fraction) return fraction;
  }
  if (mode === 'dms') return toDMS(value);
  return format(value);
}

/* ---------- 4. Editing helpers ---------- */
const STARTS_WITH_OPERATOR = /^[+\-*\/^×÷−²³!%]/;

function showResult(value) {
  res.classList.remove('err');
  res.textContent = format(value);
}

function showError(message) {
  res.textContent = message;
  res.classList.add('err');
}

function clearResult() {
  res.textContent = '';
  res.classList.remove('err');
}

/** After a result: an operator continues from Ans, anything else starts fresh. */
function startNewIfFresh(isOperator) {
  if (!fresh) return;
  fresh = false;
  inp.value = isOperator ? 'Ans' : '';
  inp.setSelectionRange(inp.value.length, inp.value.length);
}

function insertText(text) {
  startNewIfFresh(STARTS_WITH_OPERATOR.test(text));
  clearResult();
  inp.focus();
  inp.setRangeText(text, inp.selectionStart, inp.selectionEnd, 'end');
}

function backspace() {
  fresh = false;
  clearResult();
  inp.focus();
  let start = inp.selectionStart;
  const end = inp.selectionEnd;
  if (start === end) {
    if (start === 0) return;
    start--;
  }
  inp.setRangeText('', start, end, 'end');
}

function moveCursor(step) {
  fresh = false;
  inp.focus();
  const from = step < 0 ? inp.selectionStart : inp.selectionEnd;
  const pos = Math.max(0, Math.min(inp.value.length, from + step));
  inp.setSelectionRange(pos, pos);
}

function clearAll() {
  fresh = false;
  inp.value = '';
  clearResult();
  inp.focus();
}

function calculate() {
  const text = inp.value;
  if (!text.trim()) return;
  try {
    const value = evaluate(text);
    if (value === null) return;
    ans = value;
    lastVal = value;
    mode = 'dec';
    showResult(value);
    entries.unshift([text, format(value)]);
    entries = entries.slice(0, 15);
    fresh = true;
    renderHistory();
    inp.setSelectionRange(text.length, text.length);
  } catch (error) {
    showError(/^(Syntax|Math) ERROR$/.test(error.message) ? error.message : 'Math ERROR');
    fresh = false;
  }
}

/** M+ (sign = 1) and M- (sign = -1): adds the current value to memory. */
function memoryAdd(sign) {
  try {
    const text = inp.value.trim();
    let value = text ? evaluate(text) : null;
    if (value === null) value = ans;
    mem += sign * value;
    ans = value;
    lastVal = value;
    mode = 'dec';
    showResult(value);
    fresh = true;
  } catch (error) {
    showError('Syntax ERROR');
  }
  renderStatus();
}

/* ---------- 5. Keypad ---------- */

// Trig key: label and inserted text depend on SHIFT (inverse) and hyp.
const trigKey = (name) => {
  const label = () => name + (hyp ? 'h' : '') + (shift ? '⁻¹' : '');
  return { label, insert: () => label() + '(', cls: '' };
};

// Normal key: shows `shiftLabel` / inserts `shiftInsert` while SHIFT is on.
const key = (label, cls, insert, shiftLabel, shiftInsert) => ({
  label: () => (shift && shiftLabel ? shiftLabel : label),
  insert: () => (shift && shiftInsert !== undefined ? shiftInsert : (insert === undefined ? label : insert)),
  cls,
});

// Action key: runs a named action instead of inserting text.
const action = (label, name, cls) => ({ label: typeof label === 'function' ? label : () => label, action: name, cls });

const keys = [
  // row 1: modes
  action('SHIFT', 'shift', 'mod'),
  action('hyp', 'hyp', 'mod'),
  action(() => angle, 'angle', 'mod'),
  key('Ans', ''),
  action('AC', 'clear', 'red'),
  // row 2: trigonometry and brackets
  trigKey('sin'), trigKey('cos'), trigKey('tan'),
  key('(', 'op'), key(')', 'op'),
  // row 3: logs, roots, powers
  key('log', '', 'log(', '10ˣ', '10^('),
  key('ln', '', 'ln(', 'eˣ', 'e^('),
  key('√', '', '√(', '∛', '∛('),
  key('x²', '', '²', 'x³', '³'),
  key('xʸ', '', '^'),
  // row 4
  key('x!', '', '!'),
  key('1/x', '', '^(-1)'),
  key('|x|', '', 'abs('),
  key('nPr', ''),
  key('nCr', ''),
  // row 5: constants and memory
  key('π', ''),
  key('e', ''),
  key('EXP', '', 'E'),
  action(() => (shift ? 'MC' : 'MR'), 'memRecall', ''),
  action(() => (shift ? 'M−' : 'M+'), 'memAdd', ''),
  // row 6: nth root, degrees-minutes-seconds, fraction toggle
  key('ˣ√', ''), key('°', ''), key('′', ''), key('″', ''),
  action('S⇔D', 'display', ''),
  // rows 7-10: digits and basic operators
  key('7', 'num'), key('8', 'num'), key('9', 'num'), key('÷', 'op'), action('⌫', 'backspace', 'red'),
  key('4', 'num'), key('5', 'num'), key('6', 'num'), key('×', 'op'), key('%', 'op'),
  key('1', 'num'), key('2', 'num'), key('3', 'num'), key('−', 'op'), key('+', 'op'),
  key('0', 'num'), key('.', 'num'),
  action('◀', 'left', 'op'), action('▶', 'right', 'op'),
  action('=', 'equals', 'eq'),
];

function renderKeys() {
  grid.innerHTML = keys.map((k, index) => {
    const active = (k.action === 'shift' && shift) || (k.action === 'hyp' && hyp);
    return `<button data-n="${index}" class="${k.cls || ''}${active ? ' mod on' : ''}">${k.label()}</button>`;
  }).join('');
  renderStatus();
}

function renderStatus() {
  const flags = [angle];
  if (shift) flags.push('SHIFT');
  if (hyp) flags.push('hyp');
  if (mem !== 0) flags.push('M');
  document.getElementById('stat').innerHTML = flags.map((f) => `<span>${f}</span>`).join('');
}

function cycleAngle() {
  angle = angle === 'DEG' ? 'RAD' : angle === 'RAD' ? 'GRAD' : 'DEG';
}

function cycleDisplayMode() {
  const showing = lastVal !== null && res.textContent && !res.classList.contains('err');
  if (!showing) return;
  mode = { dec: 'frac', frac: 'mixed', mixed: 'dms', dms: 'dec' }[mode];
  res.textContent = show(lastVal);
}

grid.addEventListener('mousedown', (e) => e.preventDefault());   // keep the cursor in the screen

grid.addEventListener('click', (e) => {
  const button = e.target.closest('button');
  if (!button) return;
  const k = keys[Number(button.dataset.n)];

  if (k.action) {
    switch (k.action) {
      case 'shift':     shift = !shift; renderKeys(); return;
      case 'hyp':       hyp = !hyp; renderKeys(); return;
      case 'angle':     cycleAngle(); renderKeys(); return;
      case 'clear':     clearAll(); break;
      case 'backspace': backspace(); break;
      case 'equals':    calculate(); break;
      case 'left':      moveCursor(-1); break;
      case 'right':     moveCursor(1); break;
      case 'display':   cycleDisplayMode(); return;
      case 'memRecall':
        if (shift) { mem = 0; shift = false; renderKeys(); }
        else insertText('M');
        return;
      case 'memAdd':
        memoryAdd(shift ? -1 : 1);
        shift = false;
        renderKeys();
        return;
    }
  } else {
    insertText(k.insert());
    if (shift || hyp) { shift = false; hyp = false; renderKeys(); }
  }
  inp.focus();
});

/* ---------- 6. Physical keyboard and history ---------- */
inp.addEventListener('keydown', (e) => {
  if (e.key === 'Enter')  { e.preventDefault(); calculate(); return; }
  if (e.key === 'Escape') { e.preventDefault(); clearAll(); return; }
  if (e.ctrlKey || e.metaKey || e.altKey) return;

  if (e.key.length === 1) {                                   // a typed character
    startNewIfFresh(STARTS_WITH_OPERATOR.test(e.key));
    clearResult();
  } else if (e.key === 'Backspace' || e.key === 'Delete') {
    fresh = false;
    clearResult();
  } else if (e.key.startsWith('Arrow') || e.key === 'Home' || e.key === 'End') {
    fresh = false;
  }
});

inp.addEventListener('paste', () => { fresh = false; clearResult(); });

// Typing anywhere on the page goes to the screen.
document.addEventListener('keydown', (e) => {
  const typing = e.key.length === 1 || e.key === 'Backspace' || e.key === 'Enter';
  if (document.activeElement !== inp && typing && !e.ctrlKey && !e.metaKey && !e.altKey) {
    inp.focus();
    inp.setSelectionRange(inp.value.length, inp.value.length);
  }
});

function renderHistory() {
  const list = document.getElementById('hist');
  list.innerHTML = '';
  entries.forEach(([expression, result]) => {
    const row = document.createElement('div');
    const left = document.createElement('span');
    const right = document.createElement('b');
    left.textContent = expression;
    right.textContent = `= ${result}`;
    row.append(left, right);
    row.onclick = () => {
      fresh = false;
      inp.value = expression;
      clearResult();
      inp.focus();
      inp.setSelectionRange(expression.length, expression.length);
    };
    list.appendChild(row);
  });
}

renderKeys();
inp.focus();
</script>
</body>
</html>
"""

components.html(CALCULATOR_HTML, height=820, scrolling=True)


