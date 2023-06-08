$(document).ready(function () {
  show_list();
  today();
  hello();
});
function show_list() {
  //$("#Todo-list").empty;
  fetch("/list")
    .then((res) => res.json())
    .then((data) => {
      let rows = data["result"];
      rows.forEach((a) => {
        console.log(a);
        let todo = a["list"];
        let selc = a["selc"];
        let id = a["id"];
        let isChecked = a["isChecked"];
        let isHighlighted = a["isHighlighted"];

        let temp_html = ``;
        if(isHighlighted == 0){
          temp_html = `<li class="todo-elem">
                          <i class="icon star${
                            isHighlighted ? " filled" : ""
                          } " onclick='focusing(${id})'></i>
                          <i class="icon checkbox${
                            isChecked ? " checked" : ""
                          }" onclick='check(${id})' ></i>
                          <p class="text">${todo}.</p>
                          <i class="icon bin" onclick="del(${id})"></i>
                        </li>`;
        }else{
          temp_html = `<li class="todo-elem">
                          <i class="icon star${
                            isHighlighted ? " filled" : ""
                          } " onclick='focusing2(${id})'></i>
                          <i class="icon checkbox${
                            isChecked ? " checked" : ""
                          }" onclick='check(${id})' ></i>
                          <p class="text">${todo}.</p>
                          <i class="icon bin" onclick="del(${id})"></i>
                        </li>`;
        }
        //console.log(temp_html);
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

function check(id, checked) {
  let formData = new FormData();
  formData.append("id_give", id);
  formData.append("check_give", checked);

  fetch("/list/isChecked", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      window.location.reload();
    });
}




const focusing = ( id) => {
  let formData = new FormData();
  formData.append("highlighted_give", 1);
  formData.append("id_give", id);
  console.log(id, 1)
  
  fetch("/list/focused", { method: "POST", body: formData })
    .then((response) =>{ return response.json()})
    .then((response) => {
      alert(response.msg);
      window.location.reload();
    });
};
const focusing2 = ( id) => {
  let formData = new FormData();
  formData.append("highlighted_give", 0);
  formData.append("id_give", id);

  console.log(id, 0)
  
  fetch("/list/focused", { method: "POST", body: formData })
    .then((response) =>{ return response.json()})
    .then((response) => {
      alert(response.msg);
      window.location.reload();
    });
};






const clickInputData = () => {
  let todo = document.getElementById("todo_input").value;
  let selc = document.getElementById("input_select").value;

  let formData = new FormData();
  formData.append("todo_give", todo); // 텍스트
  formData.append("selc_give", selc); // 종류

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
