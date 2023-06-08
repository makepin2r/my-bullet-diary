$(document).ready(function () {
  show_list();
  today();
  hello();
});
function show_list() {
  $("#Todo-list").empty;
  fetch("/list")
    .then((res) => res.json())
    .then((data) => {
      let rows = data["result"];
      rows.forEach((a) => {
        let todo = a["list"];
        let num = a["num"];
        let isChecked = a["isChecked"];
        let focused = a["focused"];

        let temp_html = ``;
        if (isChecked === 0) {
          temp_html = `<h5 class='temp'>
                                        <input class="form-check-input" onclick='check(${isChecked})' type="checkbox" id="checkboxNoLabel">
                                        <i class="bi bi-star" onclick="focusing(${focused})" id="star"></i>
                                        <p class='today'>${todo}</p>
                                        <i class="bi1 bi-trash3" onclick="del(${num})" ></i>
                                    </h5>`;
        } else {
          temp_html = `<h5 class='temp'>
                                        <p class='today'>${todo} 완료!</p>
                                        <i class="bi1 bi-trash3" onclick="del(${num})" ></i>
                                    </h5>`;
        }
        $("#Todo-list").append(temp_html);
      });
    });
}

function del(num) {
  let formData = new FormData();
  formData.append("num_give", num);

  fetch("/list/delete", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
function save_list() {
  let list = $("#input_box").val();

  let formData = new FormData();
  formData.append("list_give", list);

  fetch("/list", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
function check(isChecked) {
  let formData = new FormData();
  formData.append("check_give", isChecked);

  fetch("/list/isChecked", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
function focusing(focused) {
  let formData = new FormData();
  formData.append("focused_give", focused);

  fetch("/list/focused", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}
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


