import React, { useState } from 'react';

const Calculator = () => {
  const [input, setInput] = useState('');

  const handleClick = (value) => {
    setInput((prev) => prev + value);
  };

  const handleClear = () => {
    setInput('');
  };

  const handleEvaluate = () => {
    try {
      const result = eval(input);
      setInput(result.toString());
    } catch (error) {
      setInput('Error');
    }
  };

  return (
    <div className="calculator-container">
      <h2>Name: <strong>Adrin Dsouza</strong></h2> {/* <-- Change your name here */}
      <h3>UEN: <strong>RTU24101IT009</strong></h3> {/* <-- Change your UEN here */}

      <div className="calculator">
        <div className="calculator-display">{input || '0'}</div>
        <div className="calculator-buttons">
          <div>
            <button onClick={() => handleClick('1')}>1</button>
            <button onClick={() => handleClick('2')}>2</button>
            <button onClick={() => handleClick('3')}>3</button>
            <button onClick={() => handleClick('+')}>+</button>
          </div>
          <div>
            <button onClick={() => handleClick('4')}>4</button>
            <button onClick={() => handleClick('5')}>5</button>
            <button onClick={() => handleClick('6')}>6</button>
            <button onClick={() => handleClick('-')}>-</button>
          </div>
          <div>
            <button onClick={() => handleClick('7')}>7</button>
            <button onClick={() => handleClick('8')}>8</button>
            <button onClick={() => handleClick('9')}>9</button>
            <button onClick={() => handleClick('*')}>*</button>
          </div>
          <div>
            <button onClick={() => handleClick('0')}>0</button>
            <button onClick={() => handleClick('.')}>.</button>
            <button onClick={handleClear}>C</button>
            <button onClick={() => handleClick('/')}>/</button>
          </div>
          <div>
            <button onClick={handleEvaluate}>=</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Calculator;
