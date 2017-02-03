window.onload = () => {
  const input = document.getElementById("input");
  input.onkeydown = (event) => {
    const text = input.value;
    if (event.key === "Enter" && text !== "") {
      input.value = "";
      const todoItem = document.createElement("li");
      todoItem.innerHTML = text;
      todoItem.className = "card";

      todoItem.onclick = (_) => items.removeChild(todoItem);

      const items = document.getElementById("items");
      items.appendChild(todoItem);

    }
  }
};
