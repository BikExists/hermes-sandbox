// Calculator logic for Hermes First Calculator
const displayCurrent = document.querySelector('.current-operand');
const displayPrevious = document.querySelector('.previous-operand');
const buttons = document.querySelectorAll('button');

let currentOperand = '';
let previousOperand = '';
let operation = undefined;

// Prevent default context menu on right-click
buttons.forEach(btn => btn.addEventListener('contextmenu', e => e.preventDefault()));

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    const value = btn.dataset.number !== undefined ? btn.dataset.number : 
                  btn.dataset.operator !== undefined ? btn.dataset.operator : 
                  btn.dataset.decimal !== undefined ? btn.dataset.decimal : 
                  btn.textContent;

    if (btn.classList.contains('operator')) {
      handleOperator(value);
    } else if (btn.classList.contains('decimal')) {
      handleDecimal();
    } else if (btn.textContent === 'C') {
      clear();
    } else if (btn.textContent === '←') {
      backspace();
    } else if (btn.textContent === '=' || btn.classList.contains('last')) {
      calculate();
    } else {
      appendNumber(value);
    }

    updateDisplay();
  });
});

function handleOperator(op) {
  if (currentOperand === '' && op !== '±') return;
  if (previousOperand !== '' && operation && currentOperand !== '') {
    calculate();
  }
  operation = op;
  previousOperand = currentOperand;
  currentOperand = '';
  updateDisplayPrevious();
}

function calculate() {
  let computation;
  const prev = parseFloat(previousOperand);
  const current = parseFloat(currentOperand);
  if (isNaN(prev) || isNaN(current)) return;

  switch (operation) {
    case '+':
      computation = prev + current;
      break;
    case '−':
    case '-':
      computation = prev - current;
      break;
    case '×':
      computation = prev * current;
      break;
    case '÷':
      if (current === 0) {
        displayCurrent.textContent = 'Error';
        return;
      }
      computation = prev / current;
      break;
    default:
      return;
  }

  currentOperand = computation;
  operation = undefined;
  previousOperand = '';
  updateDisplay();
}

function appendNumber(number) {
  if (number === '.' && currentOperand.includes('.')) return;
  currentOperand = currentOperand.toString() + number.toString();
}

function clear() {
  currentOperand = '';
  previousOperand = '';
  operation = undefined;
}

function backspace() {
  currentOperand = currentOperand.toString().slice(0, -1);
}

function handleDecimal() {
  if (!currentOperand.includes('.')) {
    currentOperand += '.';
  }
}

function updateDisplay() {
  displayCurrent.textContent = formatNumber(currentOperand);
  if (operation != null) {
    displayPrevious.textContent = `${formatNumber(previousOperand)} ${operation}`;
  } else {
    displayPrevious.textContent = '';
  }
}

function formatNumber(num) {
  const floatNum = parseFloat(num);
  if (isNaN(floatNum)) return '';
  return floatNum.toLocaleString('en');
}