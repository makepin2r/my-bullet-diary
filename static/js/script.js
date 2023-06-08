const clickInputData = () => {
  let todo = document.getElementById("todo_input").value;
  let selc = document.getElementById("input_select").value;

  let formData = new FormData();
  formData.append("todo_give", todo);
  formData.append("selc_give", selc);

  console.log(todo, selc);
  fetch("/inputData", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
};

const today = () => {
  const date = new Date();
  const year = date.getFullYear();
  const month = date.toLocaleString("en-kr", { month: "short" });
  const day = date.getDate();
  const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const week = days[date.getDay()];

  document.getElementById(
    "today_box"
  ).innerHTML = `${month} ${day} ${year} ${week}`;
};

const hello = () => {
  document.getElementById("hello_box").innerHTML = `안녕하세요,님&#128516;`;
};

today();
hello();
