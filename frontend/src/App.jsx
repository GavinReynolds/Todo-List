import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="bg-indigo-100">
        <h1 className="text-5xl text-center">Hello</h1>
      </div>
    </>
  );
}

export default App;
