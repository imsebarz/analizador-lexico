import { useState } from "react";
import "./App.css";
import Token from "./Token";

function App() {
  const [tokens, setTokens] = useState([]);
  const [input, setInput] = useState("");

  const handleInput = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const source = {
      source: input,
    };

    fetch("http://localhost:8000/process", {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(source),
    })
      .then((response) => response.json())
      .then((data) => setTokens(data.data));
  };
  return (
    <div className="App">
      <h1>Analizador Léxico</h1>
      <form action="" onSubmit={handleSubmit}>
        <textarea
          name="input"
          placeholder="Ingresa aqui la expresión a analizar"
          onChange={handleInput}
        />
        <button>Analizar</button>
      </form>
      <div className="tokens-container">
        <h2>
          Tokens <span>{`[${tokens.length}]`}</span>
        </h2>
        {tokens.map((token) => (
          <Token
            type={token.type}
            literal={token.literal}
            key={tokens.indexOf(token)}
            id={tokens.indexOf(token) + 1}
          ></Token>
        ))}
      </div>
    </div>
  );
}

export default App;
